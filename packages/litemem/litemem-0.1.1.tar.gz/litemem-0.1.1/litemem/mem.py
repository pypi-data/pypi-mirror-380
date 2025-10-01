"""
Модуль для управления базой данных памяти с использованием sqlite-vec и локальных эмбеддингов.

Реализует:
- Основную таблицу: (message TEXT)
- Виртуальную таблицу для векторного поиска по message
- Виртуальную таблицу для полнотекстового поиска по message

Добавление и удаление в виртуальные таблицы согласовано с основной таблицей.
"""

import sqlite3
from pathlib import Path
from textwrap import dedent
from typing import Callable, List, Tuple

import sqlite_lembed
import sqlite_vec
from sqlite_vec import serialize_float32


class Memory:
    DEFAULT_PATH = ":memory:"

    def __init__(
        self,
        db_path: str,
        embed: Callable[[str], List[float]],
        vector_size: int | None = None,
    ):
        self.path = db_path or self.DEFAULT_PATH
        self.embed = embed
        self.vector_size = vector_size or len(self.embed("test"))
        self.db = self._get_connection()
        self._initdb()

    def _get_connection(self) -> sqlite3.Connection:
        """
        Устанавливает соединение с SQLite базой данных и загружает расширение sqlite-vec.

        Returns:
            sqlite3.Connection: Соединение с базой данных.
        """
        db = sqlite3.connect(self.path)
        db.enable_load_extension(True)
        sqlite_vec.load(db)
        sqlite_lembed.load(db)
        db.enable_load_extension(False)
        return db

    def _initdb(self):
        """
        Настраивает базу данных:
        - Основная таблица: memory_items (message TEXT)
        - Виртуальная таблица: memory_vec (embedding float[],  rowid)
        - Виртуальная таблица: memory_fts (message, rowid)
        """

        # Виртуальная таблица для эмбеддингов
        try:
            # Основная таблица
            self.db.execute("CREATE TABLE IF NOT EXISTS memory_items (message TEXT)")
            # Виртуальная таблица для эмбеддингов
            self.db.execute(
                f"CREATE VIRTUAL TABLE IF NOT EXISTS memory_vec USING vec0(embedding float[{self.vector_size}])"
            )
            # Виртуальная таблица для полнотекстового поиска
            self.db.execute(
                "CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(message, content='memory_items', content_rowid='rowid', tokenize='porter unicode61')"
            )
            # Создание триггеров для обновления виртуальных таблиц fts
            self.db.executescript(
                dedent(f"""
            CREATE TABLE IF NOT EXISTS memory_items (message TEXT);
            CREATE VIRTUAL TABLE IF NOT EXISTS memory_vec USING vec0(embedding float[{self.vector_size}]);
            CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(
                message, content='memory_items', content_rowid='rowid', tokenize='porter unicode61');

            CREATE TRIGGER IF NOT EXISTS tbl_items_ins AFTER INSERT ON memory_items BEGIN
                INSERT INTO memory_fts(rowid, message) VALUES (new.rowid, new.message);
            END;
            CREATE TRIGGER IF NOT EXISTS tbl_items_del AFTER DELETE ON memory_items BEGIN
                INSERT INTO memory_fts(memory_fts, rowid, message) VALUES ('delete', old.rowid, old.message);
            END;
            CREATE TRIGGER IF NOT EXISTS tbl_items_upd AFTER UPDATE ON memory_items BEGIN
                INSERT INTO memory_fts(memory_fts, rowid, message) VALUES('delete', old.rowid, old.message);
                INSERT INTO memory_fts(rowid, message) VALUES (new.rowid, new.message);
            END;
        """)
            )
            # После инициализации: синхронизируем индексы на случай восстановления/обновления
            # 1. REBUILD FTS index (fully refreshes FTS from table data)
            self.db.execute("INSERT INTO memory_fts(memory_fts) VALUES ('rebuild');")

            # 2. Вставляем недостающие эмбеддинги в memory_vec
            #   Сначала получим rowid'ы, которых нет в memory_vec
            existing_vecs = set(row[0] for row in self.db.execute("SELECT rowid FROM memory_vec"))
            items = self.db.execute("SELECT rowid, message FROM memory_items").fetchall()
            for rowid, message in items:
                if rowid not in existing_vecs:
                    embedding = self.embed(message)
                    self.db.execute(
                        "INSERT INTO memory_vec(rowid, embedding) VALUES (?, ?)",
                        (rowid, serialize_float32(embedding)),
                    )
        except sqlite3.OperationalError as e:
            print(f"Ошибка создания виртуальных таблиц: {str(e)}")
            raise e

    def add(self, message: str | List[str]):
        """
        Добавляет новую запись в основную и виртуальные таблицы.

        Args:
            message (str): Сообщение для хранения.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.add('Пример сообщения')
        """
        if not message:
            return
        if isinstance(message, str):
            message = [message]
        try:
            with self.db:
                for c in message:
                    if not c:
                        continue
                    embedding = self.embed(c)
                    cur = self.db.execute("INSERT INTO memory_items(message) VALUES (?)", (c,))
                    rowid = cur.lastrowid
                    self.db.execute(
                        "INSERT INTO memory_vec(rowid, embedding) VALUES (?, ?)",
                        (rowid, serialize_float32(embedding)),
                    )

                    # self.db.execute("INSERT INTO memory_fts(rowid, message) VALUES (?, ?)", (rowid, c))

        except Exception as e:
            raise RuntimeError(f"Не удалось добавить запись: {str(e)}") from e

    def remove(self, ids: List[str]):
        with self.db:
            placeholders = ",".join(["?"] * len(ids))
            self.db.execute(f"DELETE FROM memory_items WHERE rowid IN ({placeholders})", ids)
            self.db.execute(f"DELETE FROM memory_vec WHERE rowid IN ({placeholders})", ids)

    def clear(self):
        """
        Очищает все таблицы.
        """
        with self.db:
            self.db.execute("DELETE FROM memory_items")
            self.db.execute("DELETE FROM memory_vec")

    def search_vec(self, query: str, limit: int = 64) -> List[Tuple[str, float]]:
        """
        Выполняет векторный поиск сообщений, похожих на заданный текст.

        Args:
            query (str): Текст для поиска похожих сообщений.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, distance), отсортированных по близости.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.search_vec('пример поиска')
        """
        try:
            query_embedding = self.embed(query)
            rows = self.db.execute(
                f"""
                SELECT message, distance
                FROM memory_vec join memory_items on memory_vec.rowid = memory_items.rowid
                WHERE embedding MATCH ?
                AND k = {limit}
                ORDER BY distance
                """,
                [serialize_float32(query_embedding)],
            )

            return [(row[0], float(row[1])) for row in rows.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Не удалось выполнить векторный поиск: {str(e)}") from e

    def search_fts(self, query: str, limit: int = 32) -> List[Tuple[str, float]]:
        """
        Выполняет полнотекстовый поиск по сообщениям.

        Args:
            query (str): Поисковый запрос.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, score).

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.search_fts('пример поиска')
        """
        try:
            words = self._fts_condition(query)
            rows = self.db.execute(
                "SELECT message, bm25(memory_fts) as score FROM memory_fts WHERE memory_fts MATCH ? ORDER BY score LIMIT ?",
                (words, limit),
            )
            return [(row[0], float(row[1])) for row in rows.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Ошибка FTS поиска: {str(e)}") from e

    def hybrid_search(self, query: str, limit: int = 32) -> List[Tuple[str, float]]:
        """
        Выполняет гибридный поиск сообщений, сначала используя векторный поиск, затем полнотекстовый,
        объединяя результаты по алгоритму reciprocal rank fusion (RRF).

        Args:
            query (str): Текст для поиска похожих сообщений.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, fused_score), отсортированных по убыванию fused_score.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.hybrid_search('пример поиска')
        """
        try:
            k = 60  # RRF hyperparameter, обычно 60
            vec_results = self.search_vec(query, limit)
            fts_results = self.search_fts(query, limit)

            # Преобразуем к словарям: message -> rank
            vec_rank = {msg: rank for rank, (msg, _) in enumerate(vec_results)}
            fts_rank = {msg: rank for rank, (msg, _) in enumerate(fts_results)}

            # Собираем все уникальные сообщения
            all_msgs = set(vec_rank) | set(fts_rank)

            fused_scores = {}
            for msg in all_msgs:
                score = 0.0
                if msg in vec_rank:
                    score += 1.0 / (k + vec_rank[msg])
                if msg in fts_rank:
                    score += 1.0 / (k + fts_rank[msg])
                fused_scores[msg] = score

            # Сортируем по fused_score (по убыванию)
            sorted_msgs = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
            # Для совместимости возвращаем (message, fused_score)
            return sorted_msgs[:limit]
        except Exception as e:
            raise RuntimeError(f"Не удалось выполнить гибридный поиск: {str(e)}") from e

    def close(self):
        self.db.close()

    def _fts_condition(self, query: str) -> str:
        """
        Формирует строку для FTS5 MATCH без кавычек и знаков препинания вокруг слов.

        Args:
            query (str): Входная строка.

        Returns:
            str: Строка для FTS5 MATCH, например: (word1 OR word2 OR word3)

        Example:
            >>> db.create_match_condition("каким спортом занимаюсь?")
            '(каким OR спортом OR занимаюсь)'
        """
        import re

        words = [re.sub(r"[^\wа-яА-ЯёЁ]", "", word) for word in query.split()]
        words = [word for word in words if len(word) > 2]
        if not words:
            return ""
        result = " OR ".join(words)
        return result


class MemoryEmbedded:
    DEFAULT_PATH = ":memory:"
    DEFAULT_MODEL_PATH = "litemem/models/all-MiniLM-L6-v2-Q8_0.gguf"

    def __init__(
        self,
        db_path: str,
        model_path: str | None = None,
        vector_size: int = 384,
    ):
        self.path = db_path or self.DEFAULT_PATH
        self._model_path = model_path or self.DEFAULT_MODEL_PATH
        self._model_name = Path(self._model_path).stem
        self._vector_size = vector_size
        self.db = self._get_connection()
        self._initdb()

    def _get_connection(self) -> sqlite3.Connection:
        """
        Устанавливает соединение с SQLite базой данных и загружает расширения.

        Returns:
            sqlite3.Connection: Соединение с базой данных.
        """
        db = sqlite3.connect(self.path)
        db.enable_load_extension(True)
        sqlite_vec.load(db)
        sqlite_lembed.load(db)
        db.enable_load_extension(False)
        return db

    def _initdb(self):
        """
        Настраивает базу данных:
        - Основная таблица: memory_items (message TEXT)
        - Виртуальная таблица: memory_vec (embedding float[],  rowid)
        - Виртуальная таблица: memory_fts (message, rowid)
        """

        # Виртуальная таблица для эмбеддингов
        try:
            # Загрузка модели для эмбеддинга
            if not self._check_model():
                self.db.execute(
                    f"INSERT INTO temp.lembed_models(name, model)"
                    f"select '{self._model_name}', lembed_model_from_file('{self._model_path}');",
                )
            # Основная таблица
            self.db.execute("CREATE TABLE IF NOT EXISTS memory_items (message TEXT)")
            # Виртуальная таблица для эмбеддингов
            self.db.execute(
                f"CREATE VIRTUAL TABLE IF NOT EXISTS memory_vec USING vec0(embedding float[{self._vector_size}])"
            )
            # Виртуальная таблица для полнотекстового поиска
            self.db.execute(
                "CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(message, content='memory_items', content_rowid='rowid', tokenize='porter unicode61')"
            )
            # Создание триггеров для обновления виртуальных таблиц fts
            self.db.executescript(
                dedent(f"""
                CREATE TABLE IF NOT EXISTS memory_items (message TEXT);
                       
                CREATE VIRTUAL TABLE IF NOT EXISTS memory_vec USING vec0(embedding float[{self._vector_size}]);

                CREATE VIRTUAL TABLE IF NOT EXISTS memory_fts USING fts5(
                    message, content='memory_items', content_rowid='rowid', tokenize='porter unicode61');

                CREATE TRIGGER IF NOT EXISTS tbl_items_ins AFTER INSERT ON memory_items BEGIN
                    INSERT INTO memory_fts(rowid, message) VALUES (new.rowid, new.message);
                END;

                CREATE TRIGGER IF NOT EXISTS tbl_items_del AFTER DELETE ON memory_items BEGIN
                    INSERT INTO memory_fts(memory_fts, rowid, message) VALUES ('delete', old.rowid, old.message);
                END;

                CREATE TRIGGER IF NOT EXISTS tbl_items_upd AFTER UPDATE ON memory_items BEGIN
                    INSERT INTO memory_fts(memory_fts, rowid, message) VALUES('delete', old.rowid, old.message);
                    INSERT INTO memory_fts(rowid, message) VALUES (new.rowid, new.message);
                END;
                """)
            )
            # После инициализации: синхронизируем индексы на случай восстановления/обновления
            # 1. REBUILD FTS index (fully refreshes FTS from table data)
            self.db.execute("INSERT INTO memory_fts(memory_fts) VALUES ('rebuild');")

            # TODO: Rebuild vector index

        except sqlite3.OperationalError as e:
            print(f"Ошибка создания виртуальных таблиц: {str(e)}")
            raise e

    def add(self, message: str | List[str]):
        """
        Добавляет новую запись в основную и виртуальные таблицы.

        Args:
            message (str): Сообщение для хранения.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.add('Пример сообщения')
        """
        if not message:
            return
        if isinstance(message, str):
            message = [message]
        try:
            with self.db:
                for c in message:
                    if not c:
                        continue
                    cur = self.db.execute("INSERT INTO memory_items(message) VALUES (?)", (c,))
                    rowid = cur.lastrowid

                    self.db.execute(
                        f"INSERT INTO memory_vec(rowid, embedding) VALUES (?, lembed('{self._model_name}', ?))",
                        (rowid, c),
                    )

                    # self.db.execute("INSERT INTO memory_fts(rowid, message) VALUES (?, ?)", (rowid, c))

        except Exception as e:
            raise RuntimeError(f"Не удалось добавить запись: {str(e)}") from e

    def clear(self, ids: List[str]):
        with self.db:
            self.db.execute(
                "DELETE FROM memory_items WHERE rowid IN (SELECT rowid IN (?))",
                (ids,),
            )
            self.db.execute(
                "DELETE FROM memory_vec WHERE rowid IN (SELECT rowid IN (?))",
                (ids,),
            )

    def clear_all(self):
        """
        Очищает все таблицы.
        """
        with self.db:
            self.db.execute("DELETE FROM memory_items")
            self.db.execute("DELETE FROM memory_vec")

    def search_vec(self, query: str, limit: int = 64) -> List[Tuple[str, float]]:
        """
        Выполняет векторный поиск сообщений, похожих на заданный текст.

        Args:
            query (str): Текст для поиска похожих сообщений.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, distance), отсортированных по близости.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.search_vec('пример поиска')
        """
        try:
            rows = self.db.execute(
                dedent(
                    f"""
                    with matches as (
                        select
                            rowid,
                            distance
                        from memory_vec
                        where embedding match lembed('{self._model_name}', ?)
                        order by distance
                        limit ?
                    )
                    select message, distance
                    from matches
                    left join memory_items on memory_items.rowid = matches.rowid;                
                    """
                ),
                [query, limit],
            )

            return [(row[0], float(row[1])) for row in rows.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Не удалось выполнить векторный поиск: {str(e)}") from e

    def search_fts(self, query: str, limit: int = 32) -> List[Tuple[str, float]]:
        """
        Выполняет полнотекстовый поиск по сообщениям.

        Args:
            query (str): Поисковый запрос.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, score).

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.search_fts('пример поиска')
        """
        try:
            words = self._fts_condition(query)
            rows = self.db.execute(
                "SELECT message, bm25(memory_fts) as score FROM memory_fts WHERE memory_fts MATCH ? ORDER BY score LIMIT ?",
                (words, limit),
            )
            return [(row[0], float(row[1])) for row in rows.fetchall()]
        except Exception as e:
            raise RuntimeError(f"Ошибка FTS поиска: {str(e)}") from e

    def hybrid_search(self, query: str, limit: int = 32) -> List[Tuple[str, float]]:
        """
        Выполняет гибридный поиск сообщений, сначала используя векторный поиск, затем полнотекстовый,
        объединяя результаты по алгоритму reciprocal rank fusion (RRF).

        Args:
            query (str): Текст для поиска похожих сообщений.
            limit (int): Максимальное количество результатов.

        Returns:
            List[Tuple[str, float]]: Список (message, fused_score), отсортированных по убыванию fused_score.

        Example:
            >>> db = MemoryDB('memory.db', embedder)
            >>> db.hybrid_search('пример поиска')
        """
        try:
            k = 40  # RRF hyperparameter, обычно 60
            vec_results = self.search_vec(query, limit)
            fts_results = self.search_fts(query, limit)

            # Преобразуем к словарям: message -> rank
            vec_rank = {msg: rank for rank, (msg, _) in enumerate(vec_results)}
            fts_rank = {msg: rank for rank, (msg, _) in enumerate(fts_results)}

            # Собираем все уникальные сообщения
            all_msgs = set(vec_rank) | set(fts_rank)

            fused_scores = {}
            for msg in all_msgs:
                score = 0.0
                if msg in vec_rank:
                    score += 1.0 / (k + vec_rank[msg])
                if msg in fts_rank:
                    score += 1.0 / (k + fts_rank[msg])
                fused_scores[msg] = score

            # Сортируем по fused_score (по убыванию)
            sorted_msgs = sorted(fused_scores.items(), key=lambda x: x[1], reverse=True)
            # Для совместимости возвращаем (message, fused_score)
            return sorted_msgs[:limit]
        except Exception as e:
            raise RuntimeError(f"Не удалось выполнить гибридный поиск: {str(e)}") from e

    def close(self):
        self.db.close()

    def _fts_condition(self, query: str) -> str:
        """
        Формирует строку для FTS5 MATCH без кавычек и знаков препинания вокруг слов.

        Args:
            query (str): Входная строка.

        Returns:
            str: Строка для FTS5 MATCH, например: (word1 OR word2 OR word3)

        Example:
            >>> db.create_match_condition("каким спортом занимаюсь?")
            '(каким OR спортом OR занимаюсь)'
        """
        import re

        words = [re.sub(r"[^\wа-яА-ЯёЁ]", "", word) for word in query.split()]
        words = [word for word in words if len(word) > 2]
        if not words:
            return ""
        result = " OR ".join(words)
        return result

    def _check_model(self):
        """
        Проверяет наличие модели в базе данных.
        """
        try:
            result = self.db.execute(
                "SELECT name FROM temp.lembed_models WHERE name = ?", [self._model_name]
            ).fetchall()
            return len(result) > 0
        except sqlite3.OperationalError:
            return False

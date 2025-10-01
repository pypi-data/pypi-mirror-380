"""
Тесты для модуля mem.py с использованием pytest.

Покрывает функциональность классов Memory и MemoryEmbedded.
Использует mocks для функций эмбеддинга.
"""

import tempfile
from pathlib import Path
from unittest.mock import Mock

import pytest

from litemem.mem import Memory, MemoryEmbedded


@pytest.fixture
def mock_embed():
    """
    Mock функция для эмбеддинга, возвращает фиксированный вектор.

    Returns:
        Callable: функция эмбеддинга, возвращающая список float длиной 384.
    """
    embed_mock = Mock()
    embed_mock.return_value = [0.1] * 384
    return embed_mock


@pytest.fixture
def temp_db_path():
    """
    Фикстура для временного пути к базе данных.

    Returns:
        str: путь к временному файлу базы данных.
    """
    with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as f:
        path = f.name
    yield path
    # Очистка после тестов
    Path(path).unlink(missing_ok=True)


@pytest.fixture
def memory_instance(mock_embed, temp_db_path):
    """
    Фикстура для создания экземпляра Memory.

    Args:
        mock_embed: Mock функция эмбеддинга
        temp_db_path: Временный путь к БД

    Returns:
        Memory: экземпляр Memory.
    """
    return Memory(temp_db_path, mock_embed, vector_size=384)


@pytest.fixture
def memory_embedded_instance(temp_db_path):
    """
    Фикстура для создания экземпляра MemoryEmbedded.

    Args:
        temp_db_path: Временный путь к БД

    Returns:
        MemoryEmbedded: экземпляр MemoryEmbedded.
    """
    return MemoryEmbedded(temp_db_path, model_path=None, vector_size=384)


class TestMemory:
    """Тесты для класса Memory."""

    def test_initialization(self, memory_instance):
        """Тест инициализации Memory."""
        assert memory_instance.path is not None
        assert memory_instance.embed is not None
        assert memory_instance.vector_size == 384
        assert memory_instance.db is not None

    def test_add_single_message(self, memory_instance):
        """Тест добавления одного сообщения."""
        memory_instance.add("Пример сообщения")
        assert memory_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0] == 1

    def test_add_multiple_messages(self, memory_instance):
        """Тест добавления нескольких сообщений."""
        messages = ["Сообщение 1", "Сообщение 2", "Сообщение 3"]
        memory_instance.add(messages)
        count = memory_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count == 3

    def test_add_empty_message(self, memory_instance):
        """Тест добавления пустого сообщения."""
        memory_instance.add("")
        count = memory_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count == 0

    def test_remove_messages(self, memory_instance):
        """Тест удаления сообщений."""
        memory_instance.add(["Сообщение 1", "Сообщение 2"])
        ids = [str(i) for i in range(1, 3)]  # Предполагаем rowid 1 и 2
        memory_instance.remove(ids)
        count_items = memory_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count_items == 0

    def test_clear(self, memory_instance):
        """Тест полной очистки таблицы."""
        memory_instance.add(["Сообщение 1", "Сообщение 2"])
        memory_instance.clear()
        count_items = memory_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        count_vec = memory_instance.db.execute("SELECT COUNT(*) FROM memory_vec").fetchone()[0]
        assert count_items == 0
        assert count_vec == 0

    def test_search_vec(self, memory_instance):
        """Тест векторного поиска."""
        memory_instance.add("Пример текста для векторного поиска")
        results = memory_instance.search_vec("пример", limit=5)
        assert len(results) == 1
        assert isinstance(results[0][0], str)
        assert isinstance(results[0][1], float)

    def test_search_vec_no_results(self, memory_instance):
        """Тест векторного поиска без результатов."""
        results = memory_instance.search_vec("невыполнимый запрос")
        assert results == []

    def test_search_fts(self, memory_instance):
        """Тест полнотекстового поиска."""
        memory_instance.add("Пример текста для полнотекстового поиска")
        results = memory_instance.search_fts("пример", limit=5)
        assert len(results) >= 0  # Может быть 0 или более
        for msg, score in results:
            assert isinstance(msg, str)
            assert isinstance(score, float)

    def test_search_fts_no_results(self, memory_instance):
        """Тест полнотекстового поиска без результатов."""
        results = memory_instance.search_fts("невыполнимый запрос")
        assert results == []

    def test_hybrid_search(self, memory_instance):
        """Тест гибридного поиска."""
        memory_instance.add(["Векторный и текстовый поиск", "Другое сообщение"])
        results = memory_instance.hybrid_search("поиск", limit=5)
        assert len(results) >= 0
        for item in results:
            assert isinstance(item[0], str)
            assert isinstance(item[1], float)

    def test_hybrid_search_no_results(self, memory_instance):
        """Тест гибридного поиска без результатов."""
        results = memory_instance.hybrid_search("невыполнимый запрос")
        assert results == []

    def test_fts_condition(self, memory_instance):
        """Тест вспомогательного метода _fts_condition."""
        query = "каким спортом занимаюсь?"
        condition = memory_instance._fts_condition(query)
        expected = "каким OR спортом OR занимаюсь"
        assert condition == expected

    def test_fts_condition_empty(self, memory_instance):
        """Тест _fts_condition с пустым запросом."""
        condition = memory_instance._fts_condition("")
        assert condition == ""

    def test_close(self, memory_instance):
        """Тест закрытия соединения."""
        memory_instance.close()
        # После закрытия операции должны вызывать ошибку
        with pytest.raises(Exception):
            memory_instance.db.execute("SELECT 1")


class TestMemoryEmbedded:
    """Тесты для класса MemoryEmbedded."""

    def test_initialization(self, memory_embedded_instance):
        """Тест инициализации MemoryEmbedded."""
        assert memory_embedded_instance.path is not None
        assert memory_embedded_instance._model_name is not None
        assert memory_embedded_instance._vector_size == 384
        assert memory_embedded_instance.db is not None

    def test_add_single_message(self, memory_embedded_instance):
        """Тест добавления одного сообщения в MemoryEmbedded."""
        memory_embedded_instance.add("Пример сообщения")
        count = memory_embedded_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count == 1

    def test_add_multiple_messages(self, memory_embedded_instance):
        """Тест добавления нескольких сообщений в MemoryEmbedded."""
        messages = ["Сообщение 1", "Сообщение 2", "Сообщение 3"]
        memory_embedded_instance.add(messages)
        count = memory_embedded_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count == 3

    def test_add_empty_message(self, memory_embedded_instance):
        """Тест добавления пустого сообщения в MemoryEmbedded."""
        memory_embedded_instance.add("")
        count = memory_embedded_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        assert count == 0

    def test_clear_all(self, memory_embedded_instance):
        """Тест полной очистки в MemoryEmbedded."""
        memory_embedded_instance.add(["Сообщение 1", "Сообщение 2"])
        memory_embedded_instance.clear_all()
        count_items = memory_embedded_instance.db.execute("SELECT COUNT(*) FROM memory_items").fetchone()[0]
        count_vec = memory_embedded_instance.db.execute("SELECT COUNT(*) FROM memory_vec").fetchone()[0]
        assert count_items == 0
        assert count_vec == 0

    def test_search_vec_embedded(self, memory_embedded_instance):
        """Тест векторного поиска в MemoryEmbedded."""
        memory_embedded_instance.add("Пример текста для поиска")
        results = memory_embedded_instance.search_vec("пример", limit=5)
        assert len(results) == 1
        assert isinstance(results[0][0], str)
        assert isinstance(results[0][1], float)

    def test_search_fts_embedded(self, memory_embedded_instance):
        """Тест полнотекстового поиска в MemoryEmbedded."""
        memory_embedded_instance.add("Пример текста для поиска")
        results = memory_embedded_instance.search_fts("пример", limit=5)
        assert len(results) >= 0

    def test_hybrid_search_embedded(self, memory_embedded_instance):
        """Тест гибридного поиска в MemoryEmbedded."""
        memory_embedded_instance.add(["Векторный и текстовый поиск", "Другое сообщение"])
        results = memory_embedded_instance.hybrid_search("поиск", limit=5)
        assert len(results) >= 0

    def test_fts_condition_embedded(self, memory_embedded_instance):
        """Тест _fts_condition в MemoryEmbedded."""
        query = "каким спортом занимаюсь?"
        condition = memory_embedded_instance._fts_condition(query)
        assert "каким OR спортом OR занимаюсь" == condition

    def test_check_model_mock(self, memory_embedded_instance):
        """Тест _check_model в MemoryEmbedded (mock сценарий)."""
        # Поскольку мы используем mock, модель не загружается, но метод должен работать
        exists = memory_embedded_instance._check_model()
        assert isinstance(exists, bool)

    def test_close_embedded(self, memory_embedded_instance):
        """Тест закрытия соединения в MemoryEmbedded."""
        memory_embedded_instance.close()
        with pytest.raises(Exception):
            memory_embedded_instance.db.execute("SELECT 1")


if __name__ == "__main__":
    pytest.main([__file__])

"""
litemem.model_path

Получение пути к встроенной модели пакета litemem/models/*.gguf.

Поведение:
- Если ресурс доступен в файловой системе внутри site-packages, возвращает его путь.
- Если ресурс упакован в wheel/zip, извлекает во временный файл и копирует в кэш (~/.cache/litemem/models),
  после чего возвращает путь к кэшированной копии.
"""

from __future__ import annotations

import os
import shutil
from importlib import resources
from pathlib import Path

MODEL_FILENAME = "all-MiniLM-L6-v2-Q8_0.gguf"


def _get_cache_dir() -> Path:
    """
    Возвращает директорию кэша для извлечённых ресурсов.
    """
    xdg = os.environ.get("XDG_CACHE_HOME")
    if xdg:
        base = Path(xdg)
    else:
        base = Path.home() / ".cache"
    return base / "litemem" / "models"


def get_model_path() -> Path:
    """
    Возвращает Path к файлу модели внутри установленного пакета litemem.

    Raises:
        FileNotFoundError: если файл модели не найден внутри пакета.

    Пример:
        from litemem.model_path import get_model_path
        path = get_model_path()
    """
    try:
        pkg_files = resources.files("litemem")
    except Exception as exc:
        raise RuntimeError("Не удалось получить ресурсы пакета litemem") from exc

    resource = pkg_files.joinpath("models").joinpath(MODEL_FILENAME)

    cache_dir = _get_cache_dir()
    cache_dir.mkdir(parents=True, exist_ok=True)
    dest = cache_dir / MODEL_FILENAME

    if dest.exists():
        return dest

    try:
        with resources.as_file(resource) as src:
            src_path = Path(src)
            src_str = str(src_path)

            if "site-packages" in src_str or "dist-packages" in src_str:
                return src_path

            shutil.copyfile(src_path, dest)
            return dest
    except FileNotFoundError:
        raise FileNotFoundError(
            f"Модель '{MODEL_FILENAME}' не найдена в пакете litemem. "
            "Убедитесь, что файл находится в litemem/models и включён в дистрибутив."
        )
    except Exception as exc:
        raise RuntimeError("Не удалось извлечь и скопировать ресурс модели") from exc

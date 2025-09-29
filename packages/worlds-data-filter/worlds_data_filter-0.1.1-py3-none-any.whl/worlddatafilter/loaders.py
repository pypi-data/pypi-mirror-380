from __future__ import annotations

import csv
import glob
import os

import orjson

from .types import Item


def load_jsonl(
    path: str,
    *,
    id_field: str = "id",
    text_field: str | None = None,
) -> list[Item]:
    items: list[Item] = []
    with open(path, "rb") as handle:
        for line in handle:
            if not line.strip():
                continue
            obj = orjson.loads(line)
            item_id = str(obj.get(id_field, len(items)))
            text = str(obj.get(text_field, "")) if text_field else None
            items.append(Item(id=item_id, text=text, meta=obj))
    return items


def load_csv(
    path: str,
    *,
    id_field: str = "id",
    text_field: str | None = None,
) -> list[Item]:
    items: list[Item] = []
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for idx, row in enumerate(reader):
            item_id = str(row.get(id_field, idx))
            text = str(row.get(text_field, "")) if text_field else None
            items.append(Item(id=item_id, text=text, meta=row))
    return items


def load_txt_dir(path: str) -> list[Item]:
    items: list[Item] = []
    for item_path in sorted(glob.glob(os.path.join(path, "*.txt"))):
        with open(item_path, encoding="utf-8", errors="ignore") as handle:
            text = handle.read()
        items.append(
            Item(id=os.path.basename(item_path), text=text, meta={"path": item_path}),
        )
    return items

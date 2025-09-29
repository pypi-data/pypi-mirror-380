from __future__ import annotations

import csv
from pathlib import Path

import orjson
import typer

from .core import WorldDataFilter
from .loaders import load_csv, load_jsonl, load_txt_dir
from .types import Item, ItemScore

app = typer.Typer(
    add_completion=False,
    help="The World's Data Filter — find the most valuable data, first.",
)


def _emit_scores_csv(path: Path, rows: list[ItemScore]) -> None:
    fieldnames = [
        "id",
        "value_score",
        "coverage_gain",
        "novelty",
        "quality",
        "combined",
    ]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "id": row.id,
                    "value_score": row.value_score,
                    "coverage_gain": row.coverage_gain,
                    "novelty": row.novelty,
                    "quality": row.quality,
                    "combined": row.combined,
                }
            )


def _emit_selected_jsonl(
    path: Path,
    items: list[Item],
    scores: list[ItemScore],
    explain: bool,
) -> None:
    score_by_id = {score.id: score for score in scores}
    with path.open("wb") as handle:
        for item in items:
            score = score_by_id[item.id]
            record = {
                "id": item.id,
                "score": {
                    "value_score": score.value_score,
                    "coverage_gain": score.coverage_gain,
                    "novelty": score.novelty,
                    "quality": score.quality,
                    "combined": score.combined,
                },
            }
            if explain and score.explain:
                record["explain"] = score.explain
            if item.text is not None:
                record["text"] = item.text
            if item.meta is not None:
                record["meta"] = item.meta
            handle.write(orjson.dumps(record) + b"\n")


def _load(
    path: str,
    jsonl: bool,
    csv_in: bool,
    text_field: str | None,
    id_field: str,
    dir_in: bool,
) -> list[Item]:
    if dir_in:
        items = load_txt_dir(path)
    elif jsonl or path.endswith(".jsonl"):
        items = load_jsonl(path, id_field=id_field, text_field=text_field)
    elif csv_in or path.endswith(".csv"):
        items = load_csv(path, id_field=id_field, text_field=text_field)
    else:
        raise typer.BadParameter(
            "Provide --jsonl/--csv/--dir or use file extension .jsonl/.csv",
        )
    if not items:
        raise typer.Exit(code=1)
    return items


@app.command()
def score(
    path: str = typer.Argument(..., help="Path to .jsonl / .csv / directory"),
    out: str = typer.Option("scores.csv", help="Where to write the scores CSV"),
    jsonl: bool = typer.Option(False, "--jsonl", help="Treat input as JSONL"),
    csv_in: bool = typer.Option(False, "--csv", help="Treat input as CSV"),
    dir_in: bool = typer.Option(False, "--dir", help="Treat input as directory of .txt"),
    text_field: str | None = typer.Option(None, help="Text field name (JSONL/CSV)"),
    id_field: str = typer.Option("id", help="ID field name (JSONL/CSV)"),
    w_cov: float = typer.Option(0.7, help="Weight: coverage"),
    w_nov: float = typer.Option(0.2, help="Weight: novelty"),
    w_qual: float = typer.Option(0.1, help="Weight: quality"),
) -> None:
    items = _load(path, jsonl, csv_in, text_field, id_field, dir_in)
    wdf = WorldDataFilter()
    weights = {"cov": w_cov, "nov": w_nov, "qual": w_qual}
    scores = wdf.score(items, weights=weights)
    _emit_scores_csv(Path(out), scores)
    typer.echo(f"Wrote {out} ({len(scores)} rows)")


@app.command()
def filter(
    path: str = typer.Argument(..., help="Path to .jsonl / .csv / directory"),
    k: int = typer.Option(50, help="How many items to keep"),
    out: str = typer.Option("selected.jsonl", help="Write selected items (JSONL)"),
    jsonl: bool = typer.Option(False, "--jsonl", help="Treat input as JSONL"),
    csv_in: bool = typer.Option(False, "--csv", help="Treat input as CSV"),
    dir_in: bool = typer.Option(False, "--dir", help="Treat input as directory of .txt"),
    text_field: str | None = typer.Option(None, help="Text field name (JSONL/CSV)"),
    id_field: str = typer.Option("id", help="ID field name (JSONL/CSV)"),
    criterion: str = typer.Option(
        "value_score",
        help="value_score|coverage_gain|novelty|quality",
    ),
    w_cov: float = typer.Option(0.7, help="Weight: coverage"),
    w_nov: float = typer.Option(0.2, help="Weight: novelty"),
    w_qual: float = typer.Option(0.1, help="Weight: quality"),
    explain: bool = typer.Option(
        True,
        "--explain/--no-explain",
        help="Include explain fields in JSONL output",
        show_default=True,
    ),
) -> None:
    items = _load(path, jsonl, csv_in, text_field, id_field, dir_in)
    wdf = WorldDataFilter()
    weights = {"cov": w_cov, "nov": w_nov, "qual": w_qual}
    criterion_alias = {"value_score": "combined"}
    resolved_criterion = criterion_alias.get(criterion, criterion)
    selected_scores = wdf.select(
        items,
        k=k,
        criterion=resolved_criterion,
        weights=weights,
        explain=explain,
    )
    # preserve original items order when outputting details
    selected_ids = {score.id for score in selected_scores}
    selected_items = [item for item in items if item.id in selected_ids]
    _emit_selected_jsonl(Path(out), selected_items, selected_scores, explain)
    typer.echo(f"Wrote {out} ({len(selected_items)} items by {criterion})")


app.command(
    "select",
    help="Select the highest-value subset (alias for filter).",
)(filter)

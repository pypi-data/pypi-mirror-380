import pytest

from worlddatafilter import WorldDataFilter
from worlddatafilter.types import Item


def test_basic_scoring_and_selection():
    items = [
        Item(id="1", text="alpha beta gamma"),
        Item(id="2", text="alpha alpha alpha"),
        Item(id="3", text="delta epsilon zeta"),
        Item(id="4", text="beta gamma delta"),
    ]
    wdf = WorldDataFilter()
    scores = wdf.score(items)
    assert len(scores) == 4
    # value_score (combined) in [0,1-ish]; coverage gain normalized
    assert all(0.0 <= s.coverage_gain <= 1.0 for s in scores)
    assert all(s.value_score == s.combined for s in scores)
    sel = wdf.select(items, k=2)
    assert len(sel) == 2
    # top 2 unique ids
    ids = {s.id for s in sel}
    assert len(ids) == 2


def test_value_score_alias_and_validation():
    items = [Item(id="1", text="alpha"), Item(id="2", text="beta")]
    wdf = WorldDataFilter()
    sel = wdf.select(items, k=1, criterion="value_score")
    assert len(sel) == 1
    with pytest.raises(ValueError):
        wdf.select(items, criterion="bogus")

import pytest

@pytest.mark.skip
def test_skipped1():
    assert False


@pytest.mark.skip
def test_skipped2():
    assert False
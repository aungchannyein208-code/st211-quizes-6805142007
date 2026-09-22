import pytest
@pytest.mark.nonexistent_marker
def test_bad_marker():
    assert True
PY
pytest test_strict.py 2>&1 I grep -i "unknown\Ierror" I head -2 II echo "strict-markers caught the undeclared marker"
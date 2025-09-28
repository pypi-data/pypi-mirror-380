from myproject import sample

def test_max():
    assert sample.max(1, 2) == 2
    assert sample.max(5, 3) == 5
    assert sample.max(-1, -5) == -1
from queuelab.formulas import mm1_metrics

def test_mm1_math():
    result = mm1_metrics(5,8)
    assert round(result["avg_wait_time_system"],3) == 0.333
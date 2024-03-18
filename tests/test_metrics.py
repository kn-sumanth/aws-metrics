from aws_metrics import metrics


def test_flow():
    metrics.init_client()
    metrics.init_metrics('TestNamespace')
    metrics.set_common_dimension('TestDimension', 'TestValue')
    metrics.set_context('TestContext', 'TestValue')
    metrics.get_context('_init_mono_time')
    metrics.add_metric('TestMetric', 10, 'Count', {'TestDimension': 'TestValue'})
from aws_metrics.metrics import init_client, init_metrics, add_metric


def test_flow():
    init_client()
    init_metrics('TestNamespace')
    add_metric('TestMetric', 10, 'Count', {'TestDimension': 'TestValue'})
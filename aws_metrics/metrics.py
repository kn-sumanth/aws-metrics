import boto3
from typing import Any
_client = None

# individual metrics
_metrics = []

# Namespace for all the metrics
_namespace = 'Unknown'

# Dimenions common for all metrics
_dimensions = {}

def init_client():
    global _client
    _client = boto3.client('cloudwatch')


def init_metrics(namespace: str):
    global _metrics
    global _namespace
    global _dimensions
    _metrics = list()
    _namespace = namespace
    _dimensions = dict()

def add_metric(name: str, value: Any, unit: str, dimensions: dict = None):
    _metrics.append({
        'name': name,
        'value': value,
        'unit': unit,
        'dimensions': dimensions
    })

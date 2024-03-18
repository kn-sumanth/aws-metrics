import boto3
from typing import Any
import time

_client = None

# individual metrics
_metrics = []

# Namespace for all the metrics
_namespace = 'unknown'

# Dimenions common for all metrics
_dimensions = {}

# Context related to the metrics
_context = {}

def init_client():
    global _client
    _client = boto3.client('cloudwatch')

def init_metrics(namespace: str):
    global _metrics
    global _namespace
    global _dimensions
    global _context
    _metrics = list()
    _namespace = namespace
    _dimensions = dict()
    _context = dict()
    _context['_init_mono_time'] = time.monotonic()

def set_common_dimension(key: str, value: str):
    _dimensions[key] = value

def set_common_dimensions(dimensions: dict):
    _dimensions.update(dimensions)

def set_context(key: str, value: Any):
    _context[key] = value

def get_context(key: str, default: Any = None):
    return _context.get(key, default)

def add_metric(name: str, value: Any, unit: str, dimensions: dict = None):
    _metrics.append({
        'name': name,
        'value': value,
        'unit': unit,
        'dimensions': dimensions
    })

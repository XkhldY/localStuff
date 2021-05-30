from collections import defaultdict
from django.apps import apps


class BulkContextManager:

    def __init__(self, size=50):
        self.bulk = defaultdict(list)
        self.chunk_size = size
        print('init method called')

    def __enter__(self):

        print('inside with statement')
        return self

    def _commit(self, model_class):
        model_key = model_class._meta.label
        model_class.objects.bulk_create(self.bulk[model_key])
        self.bulk[model_key] = []

    def add(self, obj):
        model_class = type(obj)
        model_key = model_class._meta.label
        self.bulk[model_key].append(obj)

        if len(self.bulk[model_key]) >= self.chunk_size:
            self._commit(model_class)

    def __exit__(self, exc_type, exc_val, exc_tb):
        for model_name, objs in self.bulk.items():
            if len(objs) > 0:
                self._commit(apps.get_model(model_name))


from dataclasses import dataclass

@dataclass
class tst:
    name: str
    number: float
    is_ok: False

import datetime

from haystack import indexes

from Employee.models import Employee


class EmployeeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    full_name = indexes.CharField(model_attr='full_name')
    designation = indexes.CharField(model_attr='designation')
    address = indexes.CharField(model_attr='address')

    def get_model(self):
        return Employee

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

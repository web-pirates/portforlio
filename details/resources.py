from import_export import resources
from .models import Inquery, News

class PersonResource(resources.ModelResource):
    class Meta:
        model = Inquery

class NewsResource(resources.ModelResource):
    class Meta:
        model = News
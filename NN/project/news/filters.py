from django_filters import FilterSet, ModelMultipleChoiceFilter, DateTimeFilter
from .models import Post, PostCategory

class PostFilter(FilterSet):
    datetime = DateTimeFilter(
        field_name= 'dataCreation',
        lookup_expr= 'gt',
        widget = DateTimeFilter(
            format = '%Y-%m-%d',
            attrs = {'type': 'date'}
        )
    )

    category = ModelMultipleChoiceFilter(
        field_name = 'category_cat',
        queryset= PostCategory.objects.all(),
        label = 'Category',
        conjoined = True,
    )
    class Meta:
        model = Post
        field = {
            'name': ['icontains'],
            'date' : ['gt']
        }
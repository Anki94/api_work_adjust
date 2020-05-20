from django_filters import FilterSet, CharFilter , DateFilter
from django.db.models import Sum
from apiapp.models import Dataset

class UserFilter(FilterSet):
    channel = CharFilter(lookup_expr='icontains')
    country = CharFilter(lookup_expr='icontains')
    os = CharFilter(lookup_expr='icontains')
    after_date = DateFilter(field_name='date',lookup_expr='gt')
    before_date = DateFilter(field_name='date',lookup_expr='gt')
    date = DateFilter(field_name='date',lookup_expr='exact')

    group_by=CharFilter(method='group_by_filter')

    def group_by_filter(self,queryset,name,value):
        params=[val.strip() for val in value.split(',')]
        return queryset.values(*params).annotate(clicks=Sum('clicks'),imperessions=Sum('impressions'),installs=Sum('installs'),revenue=Sum('revenue'),spend=Sum('spend'))

    date_sort=CharFilter(method='date_filter')
    channel_sort=CharFilter(method='channel_filter')
    country_sort=CharFilter(method='country_filter')
    os_sort=CharFilter(method='os_filter')
    impressions_sort=CharFilter(method='imperessions_filter')
    clicks_sort=CharFilter(method='clicks_filter')
    installs_sort=CharFilter(method='installs_filter')
    spend_sort=CharFilter(method='spend_filter')
    revenue_sort=CharFilter(method='revenue_filter')
    cpi_sort=CharFilter(method='cpi_filter')



    def date_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-date')
        else:
            return queryset.order_by('date')

    def channel_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-channel')
        else:
            return queryset.order_by('channel')

    def country_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-country')
        else:
            return queryset.order_by('country')

    def os_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-os')
        else:
            return queryset.order_by('os')

    def impressions_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-imperessions')
        else:
            return queryset.order_by('impressions')

    def clicks_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-clicks')
        else:
            return queryset.order_by('clicks')

    def installs_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-installs')
        else:
            return queryset.order_by('install')

    def spend_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-spend')
        else:
            return queryset.order_by('spend')

    def revenue_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-revenue')
        else:
            return queryset.order_by('revenue')

    def cpi_filter(self,queryset,name,value):
        if value=='desc':
            return queryset.order_by('-cpi')
        else:
            return queryset.order_by('cpi')


    class Meta:
        model=Dataset
        fields = ['date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue']
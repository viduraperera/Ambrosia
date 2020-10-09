import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class OrderFilter(django_filters.FilterSet):
    nic = CharFilter(field_name="nic")
    date = DateFilter(field_name="rec_Date")
    # time = TimeFilter(field_name="rec_Time")

    class Meta:
        model = LeafStock
        fields = '__all__'
        exclude = ['weight', 'rec_Date', 'rec_Time']


class OrderFilterSup(django_filters.FilterSet):

    class Meta:
        model = Registration
        # fields = '__all__'
        fields = ['nicNo', 'route', 'sup_scale', 'pay_Type', 'bank']

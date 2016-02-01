import django_tables2 as tables
from django_tables2.utils import A
from profiles.models import Order

class OrderModerationTable(tables.Table):
    app_name = tables.LinkColumn('edit_status', args=[A('pk')])

    class Met:
        model = Order
        attrs = {'class': 'table no-margin'} 
        
      

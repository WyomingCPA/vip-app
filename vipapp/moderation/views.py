from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from profiles.models import Order
from django_tables2   import RequestConfig
from moderation.tables  import OrderModerationTable
from .forms import ModeratorForm


def index(request):
    table = OrderModerationTable( Order.objects.filter(status='moderation'))
    RequestConfig(request).configure(table)

    return render(request, 'moderation/index.html', {'list_check_order_moderation': table})
    
def edit_status(request, id): 
    instance = get_object_or_404(Order, id=id)
    form = ModeratorForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        return redirect('next_view')
    return render(request, 'moderation/edit_status.html', {'form': form})  


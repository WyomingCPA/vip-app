from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.template import RequestContext
from .models import Ticket
from .forms import CreateOrder, CreateSupport
from .models import Order



@login_required(login_url='/accounts/signin/')
def index(request):
    
    permissionCheck = request.user.groups.all()
    for item in permissionCheck:
        if (item.name == 'advertiser'):
            assert isinstance(request, HttpRequest)
            return render(
                request,
                    'profiles/index_profile.html',
                     context_instance = RequestContext(request,
                    {
                        'user_item': request.user,
                    })
                )


    assert isinstance(request, HttpRequest)
    return render(request, 'profiles/access_denied.html')
    

@login_required(login_url='/accounts/login/')
def buglist(request):
    permissionCheck = request.user.groups.all()
    for item in permissionCheck:
        if (item.name == 'advertiser'):
            assert isinstance(request, HttpRequest)
            return render(
                request,
                    'profiles/bug_list.html',
                     context_instance = RequestContext(request,
                    {
                        'bug_list': Ticket.objects.filter(user=request.user),
                    })
                )

    assert isinstance(request, HttpRequest)
    return render(request, 'profiles/access_denied.html')

@login_required(login_url='/accounts/login/')
def create_support(request):
    if request.method == 'POST':
        form = CreateSupport(request.POST)
        if form.is_valid():
            form.instance.user = request.user            
            form.save()
    else:
        form = CreateSupport()
         
    form.instance.user = request.user
    return render(
                request,
                    'profiles/create_support.html',
                     context_instance = RequestContext(request,
                    {
                        'user_item': request.user,
                        'form': form, 
                    })
                )

    assert isinstance(request, HttpRequest)
    return render(request, 'profiles/access_denied.html')

@login_required(login_url='/accounts/login/')
def index_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_index.html',
        context_instance = RequestContext(request,
        {
            'user_item': request.user,
        })
    )    



@login_required(login_url='/accounts/login/')
def create_order(request):
    if request.method == 'POST':
        form = CreateOrder(request.POST)
        if form.is_valid():
            form.instance.user = request.user       
            form.save()

    else:
        form = CreateOrder()
         
    form.instance.user = request.user

    return render(
        request,
        'profiles/create_order.html',
        context_instance = RequestContext(request,
        {
            'user_item': request.user,
            'form' : form,
        })
    )


@login_required(login_url='/accounts/login/')
def moderation_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_moderation.html',
        context_instance = RequestContext(request,
        {
            'moderation_order': Order.objects.filter(user=request.user, status = 'moderation'),
        })
    )


@login_required(login_url='/accounts/login/')
def pause_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_pause.html',
        context_instance = RequestContext(request,
        {
            'pause_order': Order.objects.filter(user=request.user, status = 'pause'),
        })
    )


@login_required(login_url='/accounts/login/')
def finished_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_finished.html',
        context_instance = RequestContext(request,
        {
            'finished_order': Order.objects.filter(user=request.user, status = 'finished'),
        })
    )


@login_required(login_url='/accounts/login/')
def foul_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_foul.html',
        context_instance = RequestContext(request,
        {
            'foul_order': Order.objects.filter(user=request.user, status = 'foul'),
        })
    )



@login_required(login_url='/accounts/login/')
def activ_order(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/order_activ.html',
        context_instance = RequestContext(request,
        {
            'activ_order': Order.objects.filter(user=request.user, status = 'activ'),
        })
    )


@login_required(login_url='/accounts/login/')
def refill_payments(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'profiles/refill_payments.html',
        context_instance = RequestContext(request,
        {
            
        })
    )

from django.conf.urls import patterns, url, include



urlpatterns = patterns('',
    url(r'^$', 'profiles.views.index', name='index'),
    url(r"^referrals/$", include("pinax.referrals.urls")),
    url(r'^order/$', 'profiles.views.index_order', name='index_order'),
    url(r'^support/$', 'profiles.views.buglist', name='buglist'),
    url(r'^createsupport/$', 'profiles.views.create_support', name='createsupport'),
    url(r'^createorder/$', 'profiles.views.create_order', name='createorder'),
    url(r'^moderationorder/$', 'profiles.views.moderation_order', name='moderationorder'),
    url(r'^pauseorder/$', 'profiles.views.pause_order', name='pauseorder'),
    url(r'^finishedorder/$', 'profiles.views.finished_order', name='finishedorder'),
    url(r'^foulorder/$', 'profiles.views.foul_order', name='foulorder'),
    url(r'^activorder/$', 'profiles.views.activ_order', name='activorder'),
    url(r'^refill_payments/$', 'profiles.views.refill_payments', name='refill_payments'),
) 


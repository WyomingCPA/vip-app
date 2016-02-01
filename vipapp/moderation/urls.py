from django.conf.urls import patterns, url, include



urlpatterns = patterns('',
     url(r'^$', 'moderation.views.index', name='index'),
     url(r'(\d+)/', 'moderation.views.edit_status', name='edit_status'),
) 

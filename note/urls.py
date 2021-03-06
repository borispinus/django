from django.conf.urls import include, url

urlpatterns = [
    url(r'^all/$', 'note.views.all'),
    url(r'^(?P<note_id>\d+)/$', 'note.views.get'),
    url(r'^new/$', 'note.views.new'),
    url(r'^delete/(?P<note_id>\d+)$', 'note.views.delete'),
    url(r'^edit/(?P<note_id>\d+)/$', 'note.views.edit'),
    url(r'^favorite/(?P<note_id>\d+)$', 'note.views.favorite'),
]

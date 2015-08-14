from django.conf.urls import include, url

urlpatterns = [
    url(r'^all/$', 'note.views.all'),
    url(r'^(?P<note_id>\d+)/$', 'note.views.get'),
    url(r'^new/$', 'note.views.new'),
    url(r'^filter/category$', 'note.views.filter_category'),
    url(r'^delete/(?P<note_id>\d+)$', 'note.views.delete'),
    url(r'^favorite/(?P<note_id>\d+)$', 'note.views.favorite'),
]

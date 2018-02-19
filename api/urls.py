from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^values/$', views.SnippetList.as_view()),
    url(r'^values/(?P<pk>[\w-]+)',views.SnippetDetail.as_view()),
    #url(r'^stores/(?P<pk>[0-9]+)/$', views.StoreDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

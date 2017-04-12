from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^noticias/$', views.NoticiaList.as_view(), name='list_noticia'),
    url(r'^noticias/(?P<pk>\d+)/$', views.NoticiaDetail.as_view(), name='detail_noticia'),
]

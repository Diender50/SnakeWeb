from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
    url(r'^article/(?P<id>\d+)-(?P<slug>.+)$', views.lire, name='lire'),
    url(r'^test$', views.test),

]

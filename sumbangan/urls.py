from django.conf.urls import url
from . import views

app_name = 'sumbangan'

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /beri/
    url(r'^beri/$', views.beri, name='beri'),

    # /minta/
    url(r'^minta/$', views.minta, name='minta'),
]

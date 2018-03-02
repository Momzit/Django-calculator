from django.conf.urls import url

from calculator import views

app_name = 'calculator'

urlpatterns = [

        url(r'^$', views.PrevResults.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.ShowResults.as_view(), name='show'),
        url(r'^inputform$', views.inputform, name='inputform'),
]

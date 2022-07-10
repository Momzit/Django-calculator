from django.urls import path
from calculator import views

app_name = 'calculator'

urlpatterns = [

        path('', views.PrevResults.as_view(), name='index'),
        path('(<int:pk>)/', views.ShowResults.as_view(), name='show'),
        path('inputform/', views.inputform, name='inputform'),
]

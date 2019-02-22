from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('all/', views.getall, name = "all"),
    path('hello/<str:person>', views.hello, name ="hello"),
    path('times2/<int:number>', views.times2, name ="times2"),
    path('total/<int:number>', views.total, name ="total"),
]
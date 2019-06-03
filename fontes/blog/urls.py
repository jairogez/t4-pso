from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path('', views.index,name ='index'),
    path('<int:produto_id>/', views.detail, name='detail'),
    path('<int:produto_id>/content/', views.content , name='content'),
]

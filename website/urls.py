from django.urls import path
from website import views

urlpatterns = [
    path('index.html/', views.index, name='index'),

]

from django.urls import path
from .views import home_view, detail_view, list_view

app_name = 'tweet'

urlpatterns = [
    path('', home_view, name='home'),
    path('list', list_view, name='list'),
    path('details/<int:pk>', detail_view, name='details'),


]

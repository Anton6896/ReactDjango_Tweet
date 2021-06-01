from django.urls import path
from .views import home_view, detail_view, list_view, crete_view

app_name = 'tweet'

urlpatterns = [
    path('', home_view, name='home'),
    path('list', list_view, name='list'),
    path('create', crete_view, name='crete'),
    path('details/<int:pk>', detail_view, name='details'),

]

from django.urls import path
from .views import home_view, detail_view

app_name = 'tweet'

urlpatterns = [
    path('', home_view, name='home'),
    path('details/<int:pk>/', detail_view, name='details'),


]

from django.urls import path
from .views import home, dashboard, DeleteItem, update

urlpatterns = [
    path('', home, name="home"),
    path('dashboard', dashboard, name="dashboard"),
    path('update/', update, name="update"),
    path('delete/<pk>', DeleteItem.as_view(), name="delete"),
]

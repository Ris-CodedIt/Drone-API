from django.urls import  path
from . import views

urlpatterns = [
    path('', views.register),
    path('available/', views.check_available),
    path('load/<did>/<mid>/', views.load_drone),
    path('check_med/<id>/', views.check_med),
    path('check_battery/<id>/', views.check_battery),
]
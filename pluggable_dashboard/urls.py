from django.urls import path
from . import views

app_name = 'pluggable_dashboard'

urlpatterns = [
    path('', views.dashboard_home_view, name='dashboard_home'),
    # Add other dashboard URLs here as needed
]

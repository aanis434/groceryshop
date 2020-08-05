from django.contrib.auth.decorators import login_required
from django.urls import path

from clients import views

app_name = 'clients'

urlpatterns = [
    path('', login_required(views.IndexView.as_view(), login_url='client:login'), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
    ]

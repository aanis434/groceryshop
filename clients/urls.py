from django.urls import include, path

from clients import views

app_name = 'clients'

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    ]

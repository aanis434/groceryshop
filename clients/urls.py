from django.contrib.auth.decorators import login_required
from django.urls import path

from clients import views

app_name = 'clients'

dashboard_urlpatterns = [
    path('', login_required(views.IndexView.as_view(), login_url='client:login'), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
]

brand_urlpatterns = [
    path('brand/', login_required(views.BrandListView.as_view(), login_url='client:login'), name='brand'),
    path('brand/create/', login_required(views.BrandCreateView.as_view(), login_url='client:login'), name='brandCreate'),
    path('brand/edit/<pk>', login_required(views.BrandUpdateView.as_view(), login_url='client:login'), name='brandEdit'),
    path('brand/delete/<pk>', login_required(views.BrandDeleteView.as_view(), login_url='client:login'), name='brandDelete'),
]

urlpatterns = dashboard_urlpatterns + brand_urlpatterns


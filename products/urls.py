from django.urls import path, re_path
from django.views.generic import TemplateView

from products import views

app_name = 'products'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<slug>/', views.FilterByCategoryView.as_view(), name='categories'),
    re_path(r"^(.*/)?(?P<slug>[A-Za-z0-9-]+)/$", views.FilterByCategoryView.as_view(), name='sub_categories'),
]

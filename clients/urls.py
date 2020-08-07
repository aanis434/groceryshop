from django.contrib.auth.decorators import login_required
from django.urls import path

from clients import views

app_name = 'clients'

dashboard_urlpatterns = [
    path('', login_required(views.IndexView.as_view(),
                            login_url='client:login'), name='dashboard'),
    path('login/', views.LoginView.as_view(), name='login'),
]

brand_urlpatterns = [
    path('brand/', login_required(views.BrandListView.as_view(),
                                  login_url='client:login'), name='brand'),
    path('brand/create/', login_required(views.BrandCreateView.as_view(),
                                         login_url='client:login'), name='brandCreate'),
    path('brand/edit/<pk>', login_required(views.BrandUpdateView.as_view(),
                                           login_url='client:login'), name='brandEdit'),
    path('brand/delete/<pk>', login_required(views.BrandDeleteView.as_view(),
                                             login_url='client:login'), name='brandDelete'),
]

category_urlpatterns = [
    path('category/', login_required(views.CategoryListView.as_view(),
                                     login_url='client:login'), name='category'),
    path('category/create/', login_required(views.CategoryCreateView.as_view(),
                                            login_url='client:login'), name='categoryCreate'),
    path('category/edit/<pk>', login_required(views.CategoryUpdateView.as_view(),
                                              login_url='client:login'), name='categoryEdit'),
    path('category/delete/<pk>', login_required(views.CategoryDeleteView.as_view(),
                                                login_url='client:login'), name='categoryDelete'),
]

product_urlpatterns = [
    path('product/', login_required(views.ProductListView.as_view(),
                                    login_url='client:login'), name='product'),

    path('product/create/', login_required(views.ProductCreateView.as_view(),
                                           login_url='client:login'), name='productCreate'),
    path('product/edit/<pk>', login_required(views.ProductUpdateView.as_view(),
                                             login_url='client:login'), name='productEdit'),
    path('product/delete/<pk>', login_required(views.ProductDeleteView.as_view(),
                                               login_url='client:login'), name='productDelete'),
]

urlpatterns = dashboard_urlpatterns + brand_urlpatterns + \
    category_urlpatterns + product_urlpatterns

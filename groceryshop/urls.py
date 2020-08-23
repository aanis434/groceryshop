"""groceryshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', include('products.urls', namespace='product')),
    path('cart/', TemplateView.as_view(template_name='cart.html')),
    path('checkout/', TemplateView.as_view(template_name='checkout.html')),
    path('my-account/', TemplateView.as_view(template_name='login_register.html')),
    path('contact-us/', TemplateView.as_view(template_name='contact.html')),
    path('shop/', TemplateView.as_view(template_name='shop_sidebar.html')),
    path('categories/', TemplateView.as_view(template_name='categories_sidebar.html')),
    path('track-order/', TemplateView.as_view(template_name='track_order.html')),
    path('it-admin/', admin.site.urls),
    path('admin/', include('clients.urls', namespace='client')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

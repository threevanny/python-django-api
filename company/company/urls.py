"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import include,path
from .views import HomePageView
from django.views.generic.base import TemplateView # new
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    # display Custom Admin Login  page
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(),name='home'), # display home page 
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),  # display about page
    path('services/', TemplateView.as_view(template_name='services.html'), name='services'),  # display services page
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),  # display contact page
    path('accounts/', include('accounts.urls'), name='accounts'),  # display Sign up page
    path('', include('employee.urls')),  # displays all employee app pages
]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



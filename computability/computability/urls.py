"""computability URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf.urls.static import static
from comp import views
from computability import settings

urlpatterns = [
    url(r'^$', views.almaty2018),
    url(r'^problems$', views.index),
    url(r'^workshop$', views.almaty2018),
    url(r'^workshop/venue$', views.almaty2018venue),
    url(r'^workshop/abstracts', views.almaty2018abstracts),
    url(r'^workshop/participants', views.almaty2018participants),
    url(r'^workshop/program', views.almaty2018program),
    url(r'^workshop/orgcom', views.almaty2018orgcom),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

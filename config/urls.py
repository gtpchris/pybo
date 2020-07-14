"""config URL Configuration
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
from django.contrib import admin
from django.urls import include, path

from config.views import HomeView
# from pybo.views import base_views

import logging
logger = logging.getLogger(__name__)

logger.info("config urlpatterns 진입")
urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # '/' 에 해당되는 path
    path('admin/', admin.site.urls),
    path('common/', include('common.urls')),  # http://localhost:8000/common/ 으로 시작하는 URL은 common/urls.py를 참조
    path('pybo/', include('pybo.urls')),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
]

# handler404 = 'common.views.page_not_found'

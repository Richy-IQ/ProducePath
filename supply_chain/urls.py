"""
URL configuration for supply_chain project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include("core.urls")),
#     # path('api/v1/tracking', include("tracking.urls")),
#     # path('api/v1/authentication', include("authentication.urls")),
    
# ]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),        # Users app
    path('api/v1/', include('product.urls')),  # Products app
    path('api/v1/', include('order.urls')),      # Orders app
    path('api/v1/', include('notifications.urls')),  # Notifications app
    # path('api/v1/', include('tracking.urls')),  # Tracking app
]

from django.contrib import admin
from django.urls import path, include
from .views import HomePageView
from .views import AboutPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
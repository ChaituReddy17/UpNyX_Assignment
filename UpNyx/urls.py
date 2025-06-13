from django.contrib import admin
from django.urls import path
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', views.register),
    path('api/login/', views.login_view),
    path('api/chat/', views.chat),
    path('api/tokens/', views.get_tokens),
]

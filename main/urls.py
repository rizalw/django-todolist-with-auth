from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.index, name='index'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", views.login_user, name="login"),
]
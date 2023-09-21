from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

app_name = "todos"

urlpatterns = [
    path("", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("login/", auth_view.LoginView.as_view(template_name="todos/login.html"), name="login"),
    path("logout/", auth_view.LogoutView.as_view(template_name="todos/login.html"), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
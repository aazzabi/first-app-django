from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import path
from . import views

urlpatterns = [
    path('login/', view= LoginView.as_view(template_name="account/login.html" ), name="login"),
    path('register/', views.signup),
    path('logout/', views.logout_view, name="logout"),
]

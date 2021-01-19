from . import views
from django.urls import path

app_name='woodshophome'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('forgotpass/',views.forgot_password, name='forgot_password' ),
    path('capturepass/',views.capture_password, name='capture_password'),
    path('signup/',views.signup, name="signup"),
]

from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUp, Profile
from .views import login_page_view

from .views import UserAPIView, RegisterUserAPIView

app_name = 'accounts'


urlpatterns = [
    path('sign-up/', SignUp.as_view(), name='sign_up'),
    path('profile/', Profile.as_view(), name='profile'),
    path('login/',
         auth_views.LoginView.as_view(template_name='accounts/login.html'), 
        name='login'
        ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('new-login/', login_page_view, name='new_login'),
    path('users/', UserAPIView.as_view(), name='user_api'),
    path('register',RegisterUserAPIView.as_view(), name='register-api'),
]

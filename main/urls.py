from django.urls import path

from accounts.views import ThanksPage
from .views import (HomePage, AboutPage)

app_name = 'main'

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about/", AboutPage.as_view(), name="about"),
    path("thanks/", ThanksPage.as_view(), name="thanks"),
]

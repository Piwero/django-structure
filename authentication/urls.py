from django.contrib import admin
from django.urls import path, include
from .views import signup, secret_page, SecretPage


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('accounts/', include("django.contrib.auth.urls")),
    path('secret/', secret_page, name='secret'),
    path('secret2/', SecretPage.as_view(), name='secret2'),

]



from django.urls import path
from users.views import *
urlpatterns = [
    path('profile/', profile_view, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('onboarding/', profile_edit, name='profile_onboarding'),
    path('settings/', profile_settings, name='profile_settings'),
    path('settings/', profile_settings, name='profile_settings'),
    path('emailchange/', profile_emailchange, name='profile_emailchange'),
    path('emailverify/', profile_emailverify, name='profile_emailverify'),
    path('delete/', profile_delete_view, name="profile_delete"),






]

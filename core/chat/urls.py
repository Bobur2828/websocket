from django.urls import path

from chat.views import * 
urlpatterns = [
    path('', chat_view, name="home"),
]

from django.urls import path
from chatdb.views import Home


urlpatterns = [
    path('', Home.as_view(), name='home'),
]
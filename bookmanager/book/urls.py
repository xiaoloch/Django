from django.urls import path
from book.views import index,GetUrl

urlpatterns = [
    path('<para2>/',GetUrl),
]
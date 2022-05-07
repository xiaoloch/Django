from django.urls import path
from book.views import index,GetUrl

urlpatterns = [
    path('<int:para2>/',GetUrl),
]
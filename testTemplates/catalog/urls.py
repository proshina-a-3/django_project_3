from django.urls import path
from .views import *

urlpatterns = [
    path('', state_page),
    path('add_comment/', add_comment_page),
    path('thaks/', thaks_page, name="thaks_page"),
]

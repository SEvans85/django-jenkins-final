from django.urls import path
from .views import postit_list
from . import views

from . import views

urlpatterns = [
    # path("", views.index, name="index"),
    path('', views.postit_list, name='postit_list'),
]







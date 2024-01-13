from django.urls import path
from test_app import views


urlpatterns = [
    path("get-image/", views.index, name="index"),
]
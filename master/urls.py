from django.urls import path, re_path
from .views import MyView

urlpatterns = [
    re_path(r'(?P<pk>\d+)/', MyView.as_view())
]
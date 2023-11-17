from django.urls import include, path
from demo.views import RegisterView

urlpatterns = [
    path('users/', RegisterView.as_view()),
]
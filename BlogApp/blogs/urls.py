from django.urls import path
from .views import BlogsTemplete, BlogCreateView, BlogView, AutherLoginView, BlogUploadView

urlpatterns=[
    path('basepage/',BlogsTemplete.as_view()),
    path("createauther/",BlogCreateView.as_view(),name="createauther"),
    path("blogpage/",BlogView.as_view()),
    path("login/",AutherLoginView.as_view()),
    path("login/",BlogUploadView.as_view())
]
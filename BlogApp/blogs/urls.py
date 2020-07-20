from django.urls import path, reverse_lazy
from django.contrib.auth.views import(
    LoginView,
    LogoutView,
)
from .views import BlogsTemplete, BlogView, BlogUploadView, AutherCreateView

urlpatterns=[
    path('basepage/',BlogsTemplete.as_view()),

    path("createauther/",AutherCreateView.as_view(),name="createauther"),
    path("blogpage/",BlogView.as_view()),
    path("createblog/",BlogUploadView.as_view()),
    path("login/",LoginView.as_view(template_name="blogs/login.html"),name="login"),
    path("logout/",LogoutView.as_view(next_page=reverse_lazy('login')),name="logout")
]
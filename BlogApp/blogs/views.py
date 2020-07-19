from django.shortcuts import render

from blogs.models import AutherRegistration, BlogModel

from django.views.generic import TemplateView, CreateView
from blogs.forms import AutherRegistrationForm,LoginForm
from django.contrib.auth import authenticate


# Create your views here.

class BlogsTemplete(TemplateView):
    template_name='blogs/base.html'

class BlogView(TemplateView):
    template_name='blogs/blogpage.html'


class BlogCreateView(CreateView):
    form_class=AutherRegistrationForm
    template_name="blogs/createauther.html"
    success_url="/blogs/blogpage/"

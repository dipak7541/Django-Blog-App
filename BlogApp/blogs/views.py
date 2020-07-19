from django.shortcuts import render

from blogs.models import AutherRegistration, BlogModel

from django.views.generic import TemplateView, CreateView
from blogs.forms import AutherRegistrationForm,LoginForm

# Create your views here.

class BlogsTemplete(TemplateView):
    template_name='blogs/base.html'

class BlogView(TemplateView):
    template_name='blogs/blogpage.html'


class BlogCreateView(CreateView):
    form_class=AutherRegistrationForm
    template_name="blogs/createauther.html"
    success_url="/blogs/blogpage/"

""" class AutherLoginView(LoginView):
    template_name = 'bolgs/login.html'
    from_class = forms.LoginForm """
    

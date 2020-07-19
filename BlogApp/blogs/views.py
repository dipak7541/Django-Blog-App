from django.shortcuts import render

from blogs.models import AutherRegistration, BlogModel

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from blogs.forms import AutherRegistrationForm,LoginForm, BlogDataForm
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

class AutherLoginView(TemplateView):
    template_name='blogs/login.html'
    success_url="blogs/blogpage.html"

    
    def form_valid(self, form):
        data = form.process()
        return super(AutherLoginView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(AutherLoginView, self).get_context_data(**kwargs)
        form = LoginForm(self.request.POST or None)
        context["form"] = form
        #context["latest_article"] = latest_article

        return context

class BlogUploadView(TemplateView):
    template_name='blogs/blogupload.html'
    success_url="blogs/blogpage/"

    
    def form_valid(self, form):
        data = form.process()
        return super(BlogUploadView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(BlogUploadView, self).get_context_data(**kwargs)
        form = BlogDataForm(self.request.POST or None)
        context["form"] = form
        #context["latest_article"] = latest_article
        return context
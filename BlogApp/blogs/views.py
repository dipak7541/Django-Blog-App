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


class AutherCreateView(CreateView):
    form_class=AutherRegistrationForm
    template_name="blogs/createauther.html"
    success_url="/blogs/blogpage/"


class BlogUploadView(CreateView):
    template_name='blogs/blogupload.html'
    form_class=BlogDataForm
    success_url="/blogs/blogpage/"

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.auther_id=self.request.user.id
        self.object.save()
        return super().form_valid(form)

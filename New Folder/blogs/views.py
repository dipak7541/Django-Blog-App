from django.shortcuts import render

from blogs.models import AutherRegistration, BlogModel

from django.views.generic import TemplateView, CreateView
from django.contrib.auth.views import LoginView
from blogs.forms import AutherRegistrationForm,LoginForm, BlogDataForm
from django.contrib.auth import authenticate

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


# Create your views here.

class BlogsTemplete(TemplateView):
    template_name='blogs/base.html'

class BlogView(TemplateView):
    template_name='blogs/blogpage.html'
 
    def get_context_data(self, **kwargs):
        context = super(BlogView, self).get_context_data(**kwargs)
        # here's the difference:
        context['blogs'] = BlogModel.objects.all()
        return context


class AutherCreateView(CreateView):
    form_class=AutherRegistrationForm
    template_name="blogs/createauther.html"
    success_url="/blogs/blogpage/"

@method_decorator(login_required,name="dispatch")
class BlogUploadView(CreateView):
    template_name='blogs/blogupload.html'
    form_class=BlogDataForm
    success_url="/blogs/blogpage/"

    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.auther_id=self.request.user.id
        self.object.save()
        return super().form_valid(form)

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import files
from django.contrib.auth.models import User
import operator
from django.urls import reverse_lazy
from django.contrib.staticfiles.views import serve

from django.db.models import Q

# Create your views here.





def Home(request):
    context={
        'files':files.objects.all()
    }
    return render(request,'File/Home.html',context)


def search(request):
    template='File/home.html'

    query=request.GET.get('q')

    result=files.objects.filter(Q(FileName__icontains=query) | Q(author__username__icontains=query) | Q(content__icontains=query))
    paginate_by=2
    context={ 'files':result }
    return render(request,template,context)
   


def getfile(request):
   return serve(request, 'File')

class PostListView(ListView):
    model=files
    template_name='File/home.html'
    context_object_name='files'
    ordering=['-date_upload']
    paginate_by=2
   
    


class UserPostListView(ListView):
    model=files
    template_name='File/user_posts.html'
    context_object_name='files'
    #ordering=['-date_upload']
    paginate_by=2

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
     
        
        return files.objects.filter(author=user).order_by('-date_upload')


class PostDetailView(DetailView):
    model=files
    template_name='File/file_detail.html'
   
class PostCreateView(LoginRequiredMixin,CreateView):
    model=files
    template_name='File/file_form.html'
    fields=['FileName','content','file']
    #success_url=reverse_lazy('file-detail')

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)
    
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=files
    template_name='File/file_form.html'
    fields=['FileName','content','file']

    def form_valid(self,form):
        form.instance.author =self.request.user
        return super().form_valid(form)

    def test_func(self):
        file=self.get_object()
        if self.request.user == file.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=files
    success_url='/'
    template_name='File/file_confim_delete.html'
    def test_func(self):
        file=self.get_object()
        if self.request.user == file.author:
            return True
        return False

def About(request):
    return render(request,'File/About.html')


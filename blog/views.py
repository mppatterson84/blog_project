from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post
from blog.forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    form_class = PostForm
    login_url = '/admin/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
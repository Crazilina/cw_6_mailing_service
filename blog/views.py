from django.views.generic import ListView, DetailView
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogposts'


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'blogpost'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views += 1
        post.save()
        return post

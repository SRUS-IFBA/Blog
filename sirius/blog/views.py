from django.shortcuts import render,render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from models import Post

class indexView(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 3


class detalhePost(DetailView):
    model = Post
    template_name = "post.html"




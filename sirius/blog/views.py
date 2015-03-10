from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
#from django.template import RequestContext
from models import Post

class indexView(ListView):
    model = Post
    template_name = "index.html"
    paginate_by = 2

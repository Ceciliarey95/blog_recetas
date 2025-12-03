from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from apps.posts.models import Categoria, Post

# Create your views here.

# ----- Categoria -----

class AgregarCategoria(CreateView):
    model = Categoria
    fields = ["nombre"]
    template_name = "posts/agregar_categoria.html"
    success_url = reverse_lazy("index")

# ----- Posts -----
class AgregarPost(CreateView):
    model = Post
    fields = ['titulo', 'categoria', 'descripcion', 'imagen']
    template_name = "posts/agregar_post.html"
    success_url = reverse_lazy("index")

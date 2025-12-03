from django.urls import path

from .views import AgregarCategoria, AgregarPost

app_name = "apps.posts"

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name='agregar_categoria'),
    path("agregar_post/", AgregarPost.as_view(), name="agregar_post")
]
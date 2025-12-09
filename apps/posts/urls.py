from django.urls import path

from .views import AgregarCategoria, AgregarPost, ActualizarPost, EliminarPost, ListarPosts, listar_post_por_categoria, ordenar_por

app_name = "apps.posts"

urlpatterns = [
    path("agregar_categoria/", AgregarCategoria.as_view(), name='agregar_categoria'),
    path("agregar_post/", AgregarPost.as_view(), name="agregar_post"),
    path("actualizar_post/<int:pk>", ActualizarPost.as_view() , name="actualizar_post" ),
    path("eliminar_post/<int:pk>", EliminarPost.as_view(), name="eliminar_post"),
    path("listar_posts/", ListarPosts.as_view(), name="listar_posts"),
    path("listar_por_categoria/<str:categoria>", listar_post_por_categoria, name="listar_por_categoria"),
    path("ordenar_por", ordenar_por , name="ordenar_por"),
]
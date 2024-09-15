import debug_toolbar  # type: ignore # Importa o debug_toolbar
from bookstore import views  # Importa as views do projeto 'bookstore'
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token

# Definição dos padrões de URL para o projeto
urlpatterns = [
    # Rota para o debug_toolbar, que será usada para depuração
    path("__debug__/", include(debug_toolbar.urls)),

    # Rota para o administrador do Django
    path("admin/", admin.site.urls),

    # Rota que inclui as URLs dos apps "order" e "product", versionadas como v1 ou v2
    re_path("bookstore/(?P<version>(v1|v2))/", include("order.urls")),
    re_path("bookstore/(?P<version>(v1|v2))/", include("product.urls")),

    # Rota para autenticação via token do Django Rest Framework
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),

    # Rota para a função update (atualização do código)
    path("update_server/", views.update, name="update"),

    # Rota para a view hello_world
    path("hello/", views.hello_world, name="hello_world"),

    # Rota para a página inicial (se quiser uma view inicial, como exemplo)
    path("", views.home, name="home"),
]

from django.urls import path
from .views import produto_lista, produto_novo, produto_altera, produto_exclui, home, deslogar

urlpatterns = [
    path('', home, name = 'home'),
    path('lista/', produto_lista, name = 'produto_lista'),
    path('novo/', produto_novo, name = 'produto_novo'),
    path('altera/<int:id>', produto_altera, name = 'produto_altera'),
    path('exclui/<int:id>/', produto_exclui, name = 'produto_exclui'),
    path('logout/', deslogar, name="logout"),
]
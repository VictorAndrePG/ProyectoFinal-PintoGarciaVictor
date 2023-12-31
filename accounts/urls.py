from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts.views import register_request, editar_request, registro_exitoso, Login, editar_avatar_request, \
    logout_view, MensajeCreate, MensajeDelete, MensajeList

urlpatterns = [
    path('login/', Login.as_view(), name="login"),
    path('logout/', logout_view, name="logout"),
    path('registro/', register_request, name="Registro"),
    path('editar/', editar_request, name="Editar"),
    path('registro_exitoso/', registro_exitoso, name="registro_exitoso"),
    path('avatar/', editar_avatar_request, name="Avatar"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),


]

# path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.views.generic import CreateView, ListView, DeleteView
from pyexpat.errors import messages

from accounts.forms import UserRegisterForm, UserUpdateForm, AvatarUpdateForm
from accounts.models import Avatar, Mensaje


class Login(LoginView):
    next_page = reverse_lazy('home')
    template_name = 'accounts/login.html'

def register_request(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirige a la página de confirmación después de un registro exitoso
            return redirect('registro_exitoso')

    form = UserRegisterForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/registro.html", contexto)

def registro_exitoso(request):
    return render(request, "accounts/registro_exitoso.html")

@login_required
def editar_request(request):
    user = request.user

    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = UserUpdateForm(instance=user)

    contexto = {
        "form": form
    }
    return render(request, "accounts/editar_request.html", contexto)

def editar_avatar_request(request):
    user = request.user
    if request.method == "POST":

        form = AvatarUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            try:
                avatar = user.avatar
                avatar.imagen = data["imagen"]
            except:
                avatar = Avatar(
                    user=user,
                    imagen=data["imagen"]
                )
            avatar.save()

            return redirect("home")

    form = AvatarUpdateForm()
    contexto = {
        "form": form
    }
    return render(request, "accounts/avatar.html", contexto)

def logout_view(request):
    logout(request)
    # Puedes redirigir a donde desees después del cierre de sesión
    return redirect('home')

#------------------------------------------
class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    template_name = 'mensajes/mensaje.html'
    success_url = reverse_lazy('home')


class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajes/mensaje_list.html'
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()
    def handle_no_permission(self):
        return render(self.request, "mensajes/not_found.html")


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")
    template_name = 'mensajes/mensaje_delete.html'
    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario=user_id, id=mensaje_id).exists()

    def handle_no_permission(self):
        return render(self.request, "mensajes/not_found.html")
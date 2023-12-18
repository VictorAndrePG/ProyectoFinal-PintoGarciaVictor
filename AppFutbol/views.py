from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView, DetailView, UpdateView

from AppFutbol.models import Equipo, Jugador, Entrenador
from AppFutbol.forms import EquipoForm, JugadorForm, EntrenadorForm, BusquedaFormJugador, BusquedaFormEntrenador, BusquedaFormEquipo

class EquipoDetalle(LoginRequiredMixin, DetailView):
    model = Equipo
    template_name = "AppFutbol/equipo_detalle.html"


def editar_equipo(request, equipo_id):
    equipo = get_object_or_404(Equipo, pk=equipo_id)

    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES, instance=equipo)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.usuario_creacion = request.user
            equipo.save()
            return redirect('mostrar_equipos')
    else:
        form = EquipoForm(instance=equipo)

    contexto = {'form': form, 'equipo': equipo}
    return render(request, 'AppFutbol/editar_equipo.html', contexto)

class EquipoEliminar(DeleteView):
    model = Equipo
    template_name = "AppFutbol/eliminar_equipo.html"
    success_url = "/futbol/mostrar_equipos"

#-------------------------
class JugadorDetalle(LoginRequiredMixin, DetailView):
    model = Jugador
    template_name = "jugadores/jugador_detalle.html"


def editar_jugador(request, jugador_id):
    jugador = get_object_or_404(Jugador, pk=jugador_id)

    if request.method == 'POST':
        form = JugadorForm(request.POST, instance=jugador)
        if form.is_valid():
            form.save()
            return redirect('mostrar_jugadores')
    else:
        form = JugadorForm(instance=jugador)

    contexto = {'form': form, 'jugador': jugador}
    return render(request, 'jugadores/editar_jugador.html', contexto)

class JugadorEliminar(DeleteView):
    model = Jugador
    template_name = "jugadores/eliminar_jugador.html"
    success_url = "/futbol/mostrar_jugadores"

#-------------------------
class EntrenadorDetalle(LoginRequiredMixin, DetailView):
    model = Entrenador
    template_name = "entrenador/entrenador_detalle.html"


def editar_entrenador(request, entrenador_id):
    entrenador = get_object_or_404(Entrenador, pk=entrenador_id)

    if request.method == 'POST':
        form = EntrenadorForm(request.POST, instance=entrenador)
        if form.is_valid():
            form.save()
            return redirect('mostrar_entrenadores')
    else:
        form = EntrenadorForm(instance=entrenador)

    contexto = {'form': form, 'entrenador': entrenador}
    return render(request, 'entrenador/editar_entrenador.html', contexto)


class EntrenadorEliminar(DeleteView):
    model = Entrenador
    template_name = "entrenador/eliminar_entrenador.html"
    success_url = "/futbol/mostrar_entrenadores"
#-------------------------
def mostrar_equipos(request):
    equipos = Equipo.objects.all()
    contexto = {"equipos": equipos, "form":BusquedaFormEquipo()}
    return render(request, 'equipos/equipos.html', contexto)


def agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            equipo = form.save(commit=False)
            equipo.usuario_creacion = request.user
            equipo.save()
            return redirect('mostrar_equipos')
    else:
        form = EquipoForm()

    contexto = {'form': form}
    return render(request, 'equipos/agregar_equipo.html', contexto)

def busqueda_equipo(request):
    nombre = request.GET.get("nombre", "")
    equipos = Equipo.objects.filter(nombre__icontains=nombre)
    contexto = {
        "equipos": equipos,
        "form": BusquedaFormEquipo(),
    }
    return render(request, "equipos/equipos.html", contexto)


def puntuar_equipo(request, equipo_id):
    if request.method == 'POST':
        puntaje = request.POST.get('puntaje')
        equipo = Equipo.objects.get(pk=equipo_id)
        equipo.puntaje += int(puntaje)
        equipo.save()
        return redirect('mostrar_equipo')
    equipo = Equipo.objects.get(pk=equipo_id)
    return render(request, 'equipos/agregar_equipo.html', {'equipo': equipo})

#-----------------------------
def mostrar_jugadores(request):
    jugadores = Jugador.objects.all()
    contexto = {"jugadores": jugadores, "form":BusquedaFormJugador()}
    return render(request, 'jugadores/jugadores.html', contexto)


def agregar_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST)
        puntaje = request.POST.get('puntaje')

        if form.is_valid():
            jugador = form.save(commit=False)
            jugador.puntaje = puntaje
            jugador.save()
            return redirect('mostrar_jugadores')
    else:
        form = JugadorForm()

    contexto = {'form': form}
    return render(request, 'jugadores/agregar_jugador.html', {'form': form})

def busqueda_jugador(request):
    nombre = request.GET.get("nombre", "")
    jugadores = Jugador.objects.filter(nombre__icontains=nombre)
    contexto = {
        "jugadores": jugadores,
        "form": BusquedaFormJugador(),
    }
    return render(request, "jugadores/jugadores.html", contexto)


def puntuar_jugador(request, jugador_id):
    if request.method == 'POST':
        puntaje = request.POST.get('puntaje')
        jugador = Jugador.objects.get(pk=jugador_id)
        jugador.puntaje += int(puntaje)
        jugador.save()
        return redirect('mostrar_jugador')
    jugador = Jugador.objects.get(pk=jugador_id)
    return render(request, 'jugadores/agregar_jugador.html', {'jugador': jugador})
#-----------------------------
def mostrar_entrenadores(request):
    entrenadores = Entrenador.objects.all()
    contexto = {"entrenadores": entrenadores, "form":BusquedaFormEntrenador()}
    return render(request, 'entrenador/entrenadores.html', contexto)


def agregar_entrenador(request):
    if request.method == 'POST':
        form = EntrenadorForm(request.POST)
        puntaje = request.POST.get('puntaje')

        if form.is_valid():
            entrenador = form.save(commit=False)
            entrenador.puntaje = puntaje
            entrenador.save()
            return redirect('mostrar_entrenadores')
    else:
        form = EntrenadorForm()

    contexto = {'form': form}
    return render(request, 'entrenador/agregar_entrenador.html', contexto)

def busqueda_entrenador(request):
    nombre = request.GET.get("nombre", "")
    entrenadores = Entrenador.objects.filter(nombre__icontains=nombre)
    contexto = {
        "entrenadores": entrenadores,
        "form": BusquedaFormEntrenador(),
    }
    return render(request, "entrenador/entrenadores.html", contexto)


def puntuar_entrenador(request, entrenador_id):
    if request.method == 'POST':
        puntaje = request.POST.get('puntaje')
        entrenador = Entrenador.objects.get(pk=entrenador_id)
        entrenador.puntaje += int(puntaje)
        entrenador.save()
        return redirect('mostrar_entrenador')
    entrenador = Entrenador.objects.get(pk=entrenador_id)
    return render(request, 'entrenador/agregar_entrenador.html', {'entrenador': entrenador})

#---------------------
def seleccionar_categoria(request):
    return render(request, 'seleccionar_categoria.html')

#-------------------------
def home(request):
    return render(request, 'index.html')

#-------------------------
def about_me(request):
    return render(request, 'about.html')
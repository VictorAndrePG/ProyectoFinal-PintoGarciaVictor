from django.urls import path
from AppFutbol.views import mostrar_equipos, agregar_equipo, mostrar_jugadores, mostrar_entrenadores, agregar_jugador, \
    agregar_entrenador, seleccionar_categoria, busqueda_jugador, busqueda_entrenador, busqueda_equipo, EquipoDetalle, \
    EquipoEliminar, editar_equipo, JugadorDetalle, JugadorEliminar, editar_jugador, EntrenadorDetalle, \
    EntrenadorEliminar, editar_entrenador, home, about_me

urlpatterns = [
    path('mostrar_equipos/', mostrar_equipos, name='mostrar_equipos'),
    path('agregar_equipo/', agregar_equipo, name='agregar_equipo'),
    path('mostrar_equipos/<int:pk>', EquipoDetalle.as_view(), name='EquipoDetalle'),
    path('eliminar_equipo/<int:pk>', EquipoEliminar.as_view(), name="EquipoEliminar"),
    path('editar_equipo/<int:equipo_id>/', editar_equipo, name='editar_equipo'),

    path('mostrar_jugadores/', mostrar_jugadores, name='mostrar_jugadores'),
    path('agregar_jugador/', agregar_jugador, name='agregar_jugador'),
    path('mostrar_jugadores/<int:pk>', JugadorDetalle.as_view(), name='JugadorDetalle'),
    path('eliminar_jugador/<int:pk>', JugadorEliminar.as_view(), name="JugadorEliminar"),
    path('editar_jugador/<int:jugador_id>/', editar_jugador, name='editar_jugador'),

    path('mostrar_entrenadores/', mostrar_entrenadores, name='mostrar_entrenadores'),
    path('agregar_entrenador/', agregar_entrenador, name='agregar_entrenador'),
    path('mostrar_entrenadores/<int:pk>', EntrenadorDetalle.as_view(), name='EntrenadorDetalle'),
    path('eliminar_entrenador/<int:pk>', EntrenadorEliminar.as_view(), name="EntrenadorEliminar"),
    path('editar_entrenador/<int:entrenador_id>/', editar_entrenador, name='editar_entrenador'),

    path('seleccionar_categoria/', seleccionar_categoria, name='seleccionar_categoria'),

    path('buscar_entrenadores/', busqueda_entrenador),
    path('buscar_jugadores/', busqueda_jugador),
    path('buscar_equipos/', busqueda_equipo),

    path('', home, name='home'),
    path('about', about_me, name='about_me'),
]
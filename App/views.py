from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


# Create your views here.

def inicio(request):
    return render(request, 'index.html')

#CRUD Cartas

#Read Cartas
def cartas(request):

    miscartas = Cartas.objects.all()   

    return render(request, 'cartas.html', {"miscartas": miscartas})


# Create Cartas
def crearCartas(request):
    if request.method == 'POST':
        miFormulario = CartasFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            inscripcion = Cartas(nombre = dataformulario['nombre'],
                                 tipo = dataformulario['tipo'], 
                                 nivel = dataformulario['nivel'], 
                                 ataque = dataformulario['ataque'], 
                                 defensa = dataformulario['defensa'], 
                                 descripcion = dataformulario['descripcion'],
                                 imagen = dataformulario['imagen']
                                 )
            inscripcion.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'cartas.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = CartasFormulario()
        return render(request, 'crear-cartas.html', {'miFormulario': miFormulario})
    
#Delete Cartas

def eliminarCartas(request, id):
    if request.method == 'POST':

        cartas = Cartas.objects.get(id=id)
        cartas.delete()

        cartas = Cartas.objects.all()
        return render(request, 'eliminarcartas.html', {"cartas":cartas} )

#Update Cartas

def editarCartas(request, id):

    cartas = Cartas.objects.get(id=id)
    
    if request.method == 'POST':
        miFormulario = CartasFormulario(request.POST)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            cartas.nombre = dataformulario['nombre']
            cartas.tipo = dataformulario['tipo']
            cartas.nivel = dataformulario['nivel']
            cartas.ataque = dataformulario['ataque']
            cartas.defensa = dataformulario['defensa']
            cartas.descripcion = dataformulario['descripcion']
            cartas.imagen = dataformulario['imagen']
            cartas.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'cartas.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = CartasFormulario(initial={
            "nombre":cartas.nombre,
            "tipo":cartas.tipo,
            "nivel":cartas.nivel,
            "ataque": cartas.ataque,    
            "defensa":cartas.defensa,
            "descripcion":cartas.descripcion,
            "Imagen": cartas.imagen
        })
        return render(request, 'editar-cartas.html', {'miFormulario': miFormulario})


#CRUD Torneo

#Read Torneo

def torneo(request):

    torneo = Torneo.objects.all()   

    return render(request, 'torneo.html', {"torneo": torneo})


# Create Torneo
@staff_member_required(login_url='/App/')
def crearTorneo(request):
    if request.method == 'POST':
        miFormulario = TorneoFormulario(request.POST, request.FILES)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            inscripcion = Torneo(nombre_torneo = dataformulario['nombre_torneo'],
                                 cantidad_participantes = dataformulario['cantidad_participantes'], 
                                 lugar_del_torneo = dataformulario['lugar_del_torneo'], 
                                 premio = dataformulario['premio'], 
                                 codigo_de_torneo = dataformulario['codigo_de_torneo'], 
                                 imagen = dataformulario['imagen']
                                 )
            inscripcion.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'cartas.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = TorneoFormulario()
        return render(request, 'crear-torneo.html', {'miFormulario': miFormulario})
    
#Delete Torneo
@staff_member_required(login_url='/App/')
def eliminarTorneo(request, id):
    if request.method == 'POST':

        torneo = Torneo.objects.get(id=id)
        torneo.delete()

        torneos = Torneo.objects.all()
        return render(request, 'eliminartorneo.html', {"torneos":torneos} )

#Update Torneo
@staff_member_required(login_url='/App/')
def editarTorneo(request, id):

    torneo = Torneo.objects.get(id=id)
    
    if request.method == 'POST':
        miFormulario = TorneoFormulario(request.POST)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            torneo.nombre_torneo = dataformulario['nombre_torneo']
            torneo.cantidad_participantes = dataformulario['cantidad_participantes']
            torneo.lugar_del_torneo = dataformulario['lugar_del_torneo']
            torneo.premio = dataformulario['premio']
            torneo.codigo_de_torneo = dataformulario['codigo_de_torneo']
            torneo.imagen = dataformulario['imagen']
            torneo.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'torneo.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = TorneoFormulario(initial={
            "nombre":torneo.nombre_torneo,
            "cantidad":torneo.cantidad_participantes,
            "Lugar":torneo.lugar_del_torneo,
            "Premio": torneo.premio,    
            "Codigo":torneo.codigo_de_torneo,
            "Imagen": torneo.imagen
        })
        return render(request, 'editar-torneo.html', {'miFormulario': miFormulario})

class MazoList(ListView):
    
    model = Mazo
    template_name= "mazos.html"
    context_object_name = 'mazos'

class MazoDetail(DetailView):
    
    model = Mazo
    template_name = "mazos_detail.html"
    context_object_name = 'mazodetail'

class MazoCreate(CreateView):
    model = Mazo
    template_name = "mazo_create.html"
    fields = ['nombre','tipo','carta_principal','cantidad_de_cartas', 'descripcion', 'imagen']
    success_url = '/App/'

def MazoUpdate(request,id):
    mazo = Mazo.objects.get(id=id)
    
    if request.method == 'POST':
        miFormulario = MazoFormulario(request.POST)
        if miFormulario.is_valid():
            dataformulario = miFormulario.cleaned_data
            mazo.nombre = dataformulario['nombre']
            mazo.tipo = dataformulario['tipo']
            mazo.nivel = dataformulario['carta_principal']
            mazo.ataque = dataformulario['cantidad_de_cartas']
            mazo.defensa = dataformulario['descripcion']
            mazo.imagen = dataformulario['imagen']
            mazo.save()
            return redirect(reverse('Inicio'))
        else:
            return render(request, 'cartas.html',{"mensaje":"Formulario Invalido"})

    else:
        miFormulario = MazoFormulario(initial={
            "nombre":mazo.nombre,
            "tipo":mazo.tipo,
            "carta_principal":mazo.nivel,
            "cantidad_de_cartas": mazo.ataque,    
            "descripcion":mazo.defensa,
            "Imagen": mazo.imagen
        })
        return render(request, 'editar-mazos.html', {'miFormulario': miFormulario})

class MazoDelete(DeleteView):
    model = Mazo
    template_name = "mazo_delete.html"
    success_url = '/App/'

def contactenos(request):
    return render(request, 'contactenos.html')

def about(request):
    return render(request, 'acerca_de_mi.html')


def loginView(request):
    
    if request.method == 'POST':  
        miFormulario = AuthenticationForm(request, data=request.POST)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            user = data['username']
            psw= data['password']
            
            user_data = authenticate(username= user, password= psw )
            
            if user_data:
                login(request, user_data)
                return redirect(reverse('Inicio'))            
            else:
                return redirect(reverse('login'), {"mensaje": 'Error en los datos'})
        else:
            return redirect(reverse('login'), {"mensaje": 'Formulario invalido'})
    else:
        miFormulario = AuthenticationForm()
        return render(request, 'login.html', {'miFormulario': miFormulario})
    
def register(request):
    
    if request.method == 'POST':
        miFormulario = UserCreationForm(request.POST)
        
        if miFormulario.is_valid():
           data = miFormulario.cleaned_data
           usuario = data['username']
           miFormulario.save()
           return render(request, 'index.html', {'mensaje':f' {usuario} te registrastes '})
           
        else:
            return render(request, 'index.html', {'mensaje': 'Formulario invalido'})
    else:
        miFormulario = UserCreationForm()
        return render(request, 'registro.html', {'miFormulario': miFormulario})

def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == 'POST':  
        miFormulario = UserEditForm(request.POST, instance = request.user)
        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            usuario.email = data['email']
            usuario.first_name= data['first_name']
            usuario.last_name= data['last_name']
            usuario.save()
            
            return redirect(reverse('Inicio'), {'mensaje':'Datos actualizados'})            
        else:
            return redirect(reverse('Inicio'), {"mensaje": 'Formulario invalido'})
    else:
        miFormulario = UserEditForm(instance = request.user)
        return render(request, 'editarPerfil.html', {'miFormulario': miFormulario})
    
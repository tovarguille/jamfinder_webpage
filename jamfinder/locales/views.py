import json
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Local
from .forms import RegisterForm, LoginForm

def index(request):
    return render(request, 'locales/index.html')

@login_required
def admin_view(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        direccion = request.POST['direccion']
        horario = request.POST['horario']
        precio = request.POST['precio']
        servicios = request.POST['servicios']
        contacto = request.POST['contacto']
        Local.objects.create(
            nombre=nombre,
            direccion=direccion,
            horario=horario,
            precio=precio,
            servicios=servicios,
            contacto=contacto
        )
        return redirect('admin_view')
    return render(request, 'locales/admin.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'locales/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_view')
            else:
                form.add_error(None, 'Credenciales inválidas')
    else:
        form = LoginForm()
    return render(request, 'locales/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def locales_api(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Local.objects.create(
            nombre=data['nombre'],
            direccion=data['direccion'],
            horario=data['horario'],
            precio=data['precio'],
            servicios=data['servicios'],
            contacto=data['contacto']
        )
        return JsonResponse({"message": "Local creado exitosamente"}, status=201)
    else:
        locales = Local.objects.all()
        return JsonResponse({"locales": list(locales.values())}, status=200)

@login_required
def local_detail_api(request, id):
    try:
        local = Local.objects.get(pk=id)
    except Local.DoesNotExist:
        return JsonResponse({"error": "Local no encontrado"}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        local.nombre = data['nombre']
        local.direccion = data['direccion']
        local.horario = data['horario']
        local.precio = data['precio']
        local.servicios = data['servicios']
        local.contacto = data['contacto']
        local.save()
        return JsonResponse({"message": "Local actualizado exitosamente"}, status=200)

    elif request.method == 'DELETE':
        local.delete()
        return JsonResponse({"message": "Local eliminado exitosamente"}, status=200)


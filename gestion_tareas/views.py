from django.shortcuts import render, HttpResponse, redirect
from gestion_tareas.models import Tarea
from django.contrib import messages

# Create your views here.
def index(request):

    # Obtenemos tareas
    # tareas = Tarea.objects.all()
    # print('TAREAS', tareas)

    # Obtenemos tareas
    tareas = Tarea.objects.values_list('id', 'title', 'created_at')
    # print('TAREAS', tareas)

    return render(request, 'gestion_tareas/index.html', {
        'title': 'Gestion de Tareas',
        'tareas': tareas
    })

def create(request):
    return render(request, 'gestion_tareas/create.html', {
        'title': 'Crear Tareas',
    })

def save(request):

    # print('POST:', request.POST)
    # exit()

    # Enviamos informacion del formulario
    if request.method == "POST":
        if 'Crear' in request.POST:
            title = request.POST['title']
            description = request.POST['description']
            delivery_at = request.POST['delivery_at']

            tarea = Tarea(
                title = title,
                description = description,
                delivery_at = delivery_at
            )

            tarea.save()

            # Crear mensaje flash (session que solo se muestra 1 vez)
            messages.success(request, 'La tarea se creo correctamente')

            return redirect('index_tareas')
        else:
            messages.warning(request, 'Peticion invalida')
    else:
        messages.warning(request, 'Peticion invalida')

def view(request, id):

    # Obtenemos tarea
    tarea = Tarea.objects.get(id=id)

    return render(request, 'gestion_tareas/view.html', {
        'title': 'Detalle Tarea',
        'tarea': tarea
    })

def delete(request, id):

    # Obtenemos tarea
    tarea = Tarea.objects.get(id=id)

    tarea.delete()

    # Crear mensaje flash (session que solo se muestra 1 vez)
    messages.warning(request, 'La tarea se elimino correctamente')

    return redirect('index_tareas')
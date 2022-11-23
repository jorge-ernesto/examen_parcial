from django.shortcuts import render, HttpResponse, redirect
from gestion_tareas.models import Tarea
from django.contrib import messages
from gestion_tareas.forms import FormTarea

# Create your views here.
def index(request):
    # Validamos autenticacion
    if not 'usuario' in request.session:
        return redirect('login')

    # Obtenemos tareas
    # tareas = Tarea.objects.all()

    # Obtenemos tareas
    tareas = Tarea.objects.values_list('id', 'title', 'created_at')

    return render(request, 'gestion_tareas/index.html', {
        'title': 'Gestion de Tareas',
        'tareas': tareas
    })

def create(request):
    # Validamos autenticacion
    if not 'usuario' in request.session:
        return redirect('login')

    return render(request, 'gestion_tareas/create.html', {
        'title': 'Crear Tareas',
    })

def save(request):
    # Validamos autenticacion
    if not 'usuario' in request.session:
        return redirect('login')

    # print('POST:', request.POST)
    # exit()

    # Recoger datos del formulario
    if request.method == "POST":
        if 'Crear' in request.POST:

            # Recoger datos del formulario
            title = request.POST['title'].strip()
            description = request.POST['description'].strip()
            delivery_at = request.POST['delivery_at']

            # Validacion con Forms Django
            formulario = FormTarea(request.POST)
            if not formulario.is_valid():
                messages.warning(request, formulario.errors)
                return redirect('create_tarea')

            # Validacion
            """
            errores = {}
            if (title == '' or title == None):
                errores['title'] = 'El titulo no es válido'
            if (description == '' or description == None):
                errores['description'] = 'La descripcion no es válida'
            if (delivery_at == '' or delivery_at == None):
                errores['delivery_at'] = 'La fecha de entrega no es válida'

            if (len(errores) > 0):
                for error in errores:
                    messages.warning(request, errores[error])
                return redirect('create_tarea')
            """

            # Obtenemos datos
            tarea = Tarea(
                title = title,
                description = description,
                delivery_at = delivery_at
            )

            # Guardamos
            try:
                tarea.save()
                messages.success(request, 'La tarea se creo correctamente')
                return redirect('index_tareas')
            except Exception as e:
                messages.warning(request, 'ERROR: ' + str(e))
                return redirect('create_tarea')

def view(request, id):
    # Validamos autenticacion
    if not 'usuario' in request.session:
        return redirect('login')

    # Obtenemos tarea
    tarea = Tarea.objects.get(id=id)

    return render(request, 'gestion_tareas/view.html', {
        'title': 'Detalle Tarea',
        'tarea': tarea
    })

def delete(request, id):
    # Validamos autenticacion
    if not 'usuario' in request.session:
        return redirect('login')

    # Obtenemos tarea
    tarea = Tarea.objects.get(id=id)

    tarea.delete()
    messages.warning(request, 'La tarea se elimino correctamente')
    return redirect('index_tareas')
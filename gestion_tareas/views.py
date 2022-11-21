from django.shortcuts import render

# Create your views here.
def list(request):
    return render(request, 'gestion_tareas/list.html', {
        'title': 'Gestion de Tareas'
    })
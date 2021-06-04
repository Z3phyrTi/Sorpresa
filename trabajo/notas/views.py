from django.shortcuts import render
from .models import Nota

# Create your views here.
def vistaPrincipal(request):
    note= Nota.objects.all()
    context = {
        'Notas': note
    }
    return render(request, 'note/listaNotas.html', context)
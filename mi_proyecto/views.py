# mi_proyecto/views.py
from django.http import HttpResponse

def pagina_inicio(request):
    return HttpResponse('Página de inicio')

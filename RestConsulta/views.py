from django.http import JsonResponse

def medicos (request):
    if request.method == 'GET':
        medico ={'id':1, 'nome': 'Adriano' }
        return JsonResponse(medico)
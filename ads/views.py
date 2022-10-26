from django.http import JsonResponse,HttpResponse


# Create your views here.
def root(request):
    return JsonResponse({'status': 'ok'})
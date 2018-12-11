from service.models import Service

def services(request):
    return {
        'categories': Service.objects.all()
    }

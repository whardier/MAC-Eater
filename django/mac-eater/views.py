from django.http import HttpResponse

from locations.models import Location

def version(request):
    import platform
    return HttpResponse(platform.python_version())


def locationrandom(request):
    l = Location.objects.all()[0]
    for i in range(1000):
        l2 = l
        l2.id = None
        l2.save()

    return HttpResponse("OK")

from django.http import HttpResponse

def version(request):
    import platform
    return HttpResponse(platform.python_version())


from django.shortcuts import render


def home(request):
    template_name = 'home.html'
    return render(request, template_name)


def resultado(request):
    template_name = 'resultado.html'
    return render(request, template_name)

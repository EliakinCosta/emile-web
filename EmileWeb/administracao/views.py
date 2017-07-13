from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'administracao/base.html', {})


def wall_messages_list(request):
    return render(request, 'administracao/wall_messages_list.html', {})

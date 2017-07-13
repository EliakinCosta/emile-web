from django.shortcuts import render
import requests


# Create your views here.

def home(request):
    return render(request, 'administracao/base.html', {})


def wall_messages_list(request):
    response = requests.get('http://emile-server.herokuapp.com/wall_messages/{0}'.format(request.user.email))

    if response.status_code == 200:
        _json = response.json()        
        return render(request, 'administracao/wall_messages_list.html', _json)
    return render(request, 'administracao/wall_messages_list.html', {})

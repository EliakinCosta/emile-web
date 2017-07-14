from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from administracao import forms
from django.views import View
from django.core.urlresolvers import reverse_lazy
import json
from  django.http import JsonResponse


@login_required
def home(request):
    return render(request, 'administracao/base.html', {})


@login_required
def wall_messages_list(request):
    response = requests.get('http://emile-server.herokuapp.com/wall_messages/{0}'.format(request.user.email))

    if response.status_code == 200:
        _json = response.json()
        return render(request, 'administracao/wall_messages_list.html', _json)
    return render(request, 'administracao/wall_messages_list.html', {})


def institutions_programs(request, pk):
    response = requests.get('http://emile-server.herokuapp.com/programs')

    if response.status_code == 200:
        _json = response.json()        
        return JsonResponse(dict(_json))
    return JsonResponse({})


class WallMessageCreateView(View):
    template_name = 'administracao/wall_message_create.html'
    success_url = reverse_lazy('administracao:wall_messages_list')
    form_class = forms.MessageForm
    initial = { 'form' : form_class }

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, { 'form' : form})

from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from administracao import forms
from django.views import View
from django.core.urlresolvers import reverse_lazy
import json
from  django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect


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


def destinations_by_user_type(request, pk):
    response = requests.get('http://emile-server.herokuapp.com/destinations_by_user_type/{0}'.format(pk))

    if response.status_code == 200:
        _json = response.json()
        return JsonResponse(dict(_json))
    return JsonResponse({})

def programs_course_sections(request, pk):
    response = requests.get('http://emile-server.herokuapp.com/programs_course_sections/{0}'.format(pk))
    print("result",response.status_code)
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

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Mensagem enviada com sucesso!")
            return redirect('administracao:wall_messages_list')

        return render(request, self.template_name, { 'form' : form})

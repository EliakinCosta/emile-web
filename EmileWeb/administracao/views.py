from django.shortcuts import render
import requests
from django.contrib.auth.decorators import login_required
from administracao import forms
from django.views import View
from django.core.urlresolvers import reverse_lazy
import json
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import redirect
import os
from django.conf import settings


@login_required
def home(request):
    return render(request, 'administracao/base.html', {})


@login_required
def wall_messages_list(request):
    url = '{0}/wall_messages/{1}'.format(settings.BASE_URL,request.user.email)
    return render(request, 'administracao/wall_messages_list.html', response_to_dict(url))


def destinations_by_user_type(request, pk):
    url = '{0}/destinations_by_user_type/{1}'.format(settings.BASE_URL, pk)
    return JsonResponse(response_to_dict(url))


def response_to_dict(url):
    response = requests.get(url)
    if response.status_code == 200:
        _json = response.json()
        return dict(_json)
    return {}



def param_values_service(request):
    if request.method == 'POST':
        url_user = '{0}/{1}/{2}'.format(settings.BASE_URL,'user_details', request.user.email)
        user = response_to_dict(url_user).get('user')

        if user:
            destination_data_dict = request.POST.get('destination_data')
            param_values_service = json.loads(destination_data_dict)['param_values_service']
            url = '{0}{1}'.format(settings.BASE_URL, param_values_service)

            if param_values_service == '<%users%>':
                return JsonResponse({})

            result = response_to_dict(url.replace('$', str(user.get('id'))))
            return JsonResponse(result)
        return JsonResponse({'result': "invalid user email"})
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
            obj = form.save()
            print(form.cleaned_data)

            initial_path = obj.message_file.path
            obj.message_file.name = '/{0}/test.pdf'.format(obj.pk)
            new_path = settings.MEDIA_ROOT + obj.message_file.name

            self.mkdir(new_path)
            os.rename(initial_path, new_path)
            obj.save()

            url_file = '{0}media{1}'.format(request.build_absolute_uri('/'), str(obj.message_file))

            for courser_section in form.cleaned_data['course_section']:
                data = {"post_message":dict(user_type_destination_id=form.cleaned_data['user_type_destination'],
                                            parameter=int(courser_section),
                                            message=str(form.cleaned_data['message']) + ' - ' + str(url_file),
                                            sender=5)}
                headers = {'Content-type': 'application/json'}
                url = '{0}/wall_push_notification'.format(settings.BASE_URL)
                r = requests.post(url, data=json.dumps(data), headers=headers)
                message = dict(r.json())
                print(message)

            messages.add_message(request, messages.SUCCESS, "Mensagem enviada com sucesso!")
            return redirect('administracao:wall_messages_list')

        return render(request, self.template_name, { 'form' : form})

    def mkdir(self, filename):
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.makedirs(os.path.dirname(filename))
            except OSError as exc: # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

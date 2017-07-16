from django import forms
from administracao import models


def get_institutions():
    return [('', '-----'), (1, 'IFBA')]


class MessageForm(forms.ModelForm):
    user_type_destination = forms.ChoiceField(choices=[], label='Tipo de destino', required=True)
    course_section = forms.ChoiceField(choices=[], label='Turma', required=False)
    message = forms.CharField(required=True, label='Mensagem', max_length=250, widget=forms.Textarea)

    class Meta:
        model = models.MessageFile
        fields = ('message_file',)

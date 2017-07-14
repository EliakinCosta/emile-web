from django import forms
from administracao import models


def get_institutions():
    return [('', '-----'), (1, 'IFBA')]


class MessageForm(forms.ModelForm):
    institution = forms.ChoiceField(choices=get_institutions())
    message = forms.CharField(required=True, label='Mensagem', max_length=250, widget=forms.Textarea)


    class Meta:
        model = models.MessageFile
        fields = ('message_file',)

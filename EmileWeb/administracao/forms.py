from django import forms
from administracao import models
from django_select2.forms import Select2MultipleWidget


def get_institutions():
    return [('', '-----'), (1, 'IFBA')]


NUMBER_CHOICES = [
    (1, 'One'),
    (2, 'Two'),
    (3, 'Three'),
    (4, 'Four'),
]


class MessageForm(forms.ModelForm):
    user_type_destination = forms.ChoiceField(choices=[], label='Tipo de destino', required=True)
    course_section = forms.MultipleChoiceField(widget=Select2MultipleWidget(attrs={'data-language': 'pt-BR','placeholder': 'Escolha um Operador'}), choices=[])
    message = forms.CharField(required=True, label='Mensagem', max_length=250, widget=forms.Textarea)

    class Meta:
        model = models.MessageFile
        fields = ('message_file',)

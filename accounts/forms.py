# accounts/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nome",
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome', 'class': 'mt-2 w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm'})
    )
    last_name = forms.CharField(
        label="Sobrenome",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Seu sobrenome', 'class': 'mt-2 w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm'})
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'seuemail@exemplo.com', 'class': 'mt-2 w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm'})
    )
    email2 = forms.EmailField(
        label="Confirmar Email",
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Confirme seu email', 'class': 'mt-2 w-full px-4 py-3 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 text-sm'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # Campos que o UserCreationForm já lida: username, password1, password2.
        # Adicionamos os campos do modelo User que queremos no formulário:
        fields = ('username', 'first_name', 'last_name', 'email')
        # 'email2' não está no modelo User, é apenas para validação no formulário.

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Se você quiser definir uma ordem específica dos campos no formulário:
        # (username já é adicionado pelo UserCreationForm, assim como password1 e password2)
        field_order = ['first_name', 'last_name', 'username', 'email', 'email2', 'password1', 'password2']
        # Recriar self.fields com a ordem desejada, se for diferente da ordem de declaração
        # ou se alguns campos forem herdados e outros definidos localmente.
        # No entanto, a ordem de declaração dos campos na classe geralmente é respeitada.
        # Ajuste os widgets dos campos de senha herdados, se necessário (já está bom com widget_tweaks)

    def clean_email(self):
        """
        Validação para garantir que o email não está em uso.
        """
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(email=email).exists():
            raise ValidationError("Este endereço de email já está registrado.")
        return email

    def clean_email2(self):
        """
        Validação para garantir que os campos de email e confirmação de email coincidem.
        """
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')
        if email and email2 and email != email2:
            raise ValidationError("Os endereços de email não coincidem.")
        return email2 # Retorna email2 para que ele seja incluído em cleaned_data

    def save(self, commit=True):
        """
        Salva o usuário com os campos adicionais.
        """
        user = super().save(commit=False) # Salva username e senha hasheada
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email'] # Atribui o email validado
        if commit:
            user.save()
        return user
# accounts/backends.py
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # O Django AuthenticationForm passa o valor do campo 'username' como o parâmetro 'username' aqui.
        # Nós o trataremos como o email do usuário.
        if username is None:
            # Se por algum motivo 'username' não foi passado, tenta pegar o email de kwargs.
            # Isso é mais para robustez, pois AuthenticationForm sempre passará 'username'.
            email = kwargs.get(UserModel.EMAIL_FIELD)
            if email is None:
                return None # Não pode autenticar sem um email/username
        else:
            email = username # Trata o 'username' do formulário como email

        try:
            # Tenta encontrar um usuário cujo email corresponda (case-insensitive)
            user = UserModel.objects.get(email__iexact=email)
        except UserModel.DoesNotExist:
            # Nenhum usuário encontrado com este email.
            # O Django tentará o próximo backend na lista AUTHENTICATION_BACKENDS (se houver).
            return None
        except UserModel.MultipleObjectsReturned:
            # Isso não deve acontecer se você tiver unique=True para o campo email
            # ou se sua lógica de registro impedir emails duplicados.
            # Se acontecer, pega o primeiro usuário encontrado.
            user = UserModel.objects.filter(email__iexact=email).order_by('id').first()

        # Verifica a senha e se o usuário pode ser autenticado
        if user and user.check_password(password) and self.user_can_authenticate(user):
            return user
        return None

    # O método get_user(user_id) já é herdado de ModelBackend e funciona como esperado.
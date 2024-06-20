from rest_framework.exceptions import AuthenticationFailed, APIException
from accounts.models import User
from companies.models import Enterprise, Employee
from django.contrib.auth.hashers import check_password, make_password

class Authentication:
    def signin(self, email=None, password=None) -> User:
        exception_auth = AuthenticationFailed('Email e/ou senha incorreto(s)!')
        user_exists = User.objects.filter(email=email).exists()

        if not user_exists or not check_password(password):
            raise exception_auth
        
        user = User.objects.filter(email=email).first()

        if not check_password(password, user.password):
            raise exception_auth
        
        return user

    def signup(self, name, email, password, type_account='owner', company_id=False):
        if not name or name == '':
            raise APIException('O nome nao deve ser vazio')
        
        if not email or email == '':
            raise APIException('O email nao deve ser vazio')
        
        if not password or password == '':
            raise APIException('A senha nao deve ser vazia')
        
        if type_account == 'employee' and not company_id:
            raise APIException("O campo id da empresa nao deve ser nulo")
        
        user = User
        if user.objects.filter(email=email).exists():
            raise APIException("Este email ja existe")
        
        password_hashed = make_password(password)

        created_user = user.objects.create(
            name=name,
            email=email,
            password=password_hashed,
            is_owner=0 if type_account == 'employee' else 1
        )

        if type_account=='owner':
            created_enterprise =  Enterprise.objects.create(
                name='Nome',
                user_id=created_user.id,
            )
        
        if type_account=='employee':
            Employee.objects.create(
                enterprise_id = company_id or created_enterprise.id,
                user_id = created_user.id
            )

        return created_user
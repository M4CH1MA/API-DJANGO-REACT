from rest_framework import permissions
from accounts.models import User_Groups, Group_Permissions
from django.contrib.auth.models import Permission

def check_permission(user, method, permission_to) -> bool | None:
    if not user.is_authenticated:
        return False
    
    if user.is_owner:
        return True
    
    required_permission = 'view_' + permission_to

    if method == 'POST':
        required_permission = 'add_' + permission_to

    elif method == 'PUT':
        required_permission = 'change_' + permission_to

    elif method == 'DELETE':
        required_permission = 'delete_' + permission_to
    
    groups = User_Groups.objects.values('group_id').filter(user_id=user.id).all()

    for group in groups:
        permissions = Group_Permissions.objects.values('permssion_id').filter(group_id=group['group_id']).all()

        for permission in permissions:
            if Permission.objects.filter(id=permission['permission_id'], codename=required_permission).exists():
                return True
            
class EnployeePermission(permissions.BasePermission):
    message = 'O funcionario nao tem permissao para gerenciar os funcionarios'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='employee')
    
class GroupsPermission(permissions.BasePermission):
    message = 'O funcionario nao tem permissao para gerenciar os grupos'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='group')
    
class GroupPermissionsPermission(permissions.BasePermission):
    message = 'O funcionario nao tem permissao para gerenciar as permissoes'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='permission')
    
class TaskPermission(permissions.BasePermission):
    message = 'O funcionario nao tem permissao para gerenciar as tarefas dos usuarios'

    def has_permission(self, request, _view):
        return check_permission(request.user, request.method, permission_to='task')
from rest_framework.exceptions import APIException

class NotFoundEmployee(APIException):
    status_code = 404
    default_detail = "Funcionario nao encontrado"
    default_code = "not_found_employee"

class NotFoundGroup(APIException):
    status_code = 404
    default_detail = "Grupo nao foi encontrado"
    default_code = "not_found_group"

class RequiredFields(APIException):
    status_code = 400
    default_detail = "Envie os campos padroes correto"
    default_code = "error_required_field"

class NotFoundTaskStatus(APIException):
    status_code = 404
    default_detail = "O status da tarefa nao foi encontrado"
    default_code = "not_found_task_status"

class NotFoundTask(APIException):
    status_code = 404
    default_detail = 'Tarefa nao encontrado'
    default_code = "not_found_task"
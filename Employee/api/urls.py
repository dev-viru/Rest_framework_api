from django.urls import path
from .views import EmployeeListCreateView, update_salary_and_delete_inactive

urlpatterns = [
    # Previous endpoints for CRUD operations
    path('', EmployeeListCreateView.as_view(), name='employee-list-create'),

    # New endpoint for updating salary and deleting inactive employees
    path('update-salary-delete-inactive/', update_salary_and_delete_inactive, name='update-salary-delete-inactive'),
]

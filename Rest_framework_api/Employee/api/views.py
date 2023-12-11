from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer



from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils import timezone
from datetime import timedelta


@api_view(['POST'])
def update_salary_and_delete_inactive(request):
    if request.method == 'POST':
        today = timezone.now().date()
        employees = Employee.objects.filter(joining_date__lte=today - timedelta(days=365))
        for employee in employees:
            employee.salary += 1000
            employee.save()

        inactive_employees = Employee.objects.filter(status='inactive')
        inactive_employees.delete()

        return Response(
            {"message": "Salaries updated for employees who completed one year and inactive employees deleted"})



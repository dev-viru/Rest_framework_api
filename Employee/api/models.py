from django.db import models

class Employee(models.Model):
    emp_name = models.CharField(max_length=100)
    joining_date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)  # 'active' or 'inactive'

    def __str__(self):
        return self.emp_name


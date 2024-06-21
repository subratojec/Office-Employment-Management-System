from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=150, null=False)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Role(models.Model):
    role = models.CharField(max_length=150, null=False)

    def __str__(self):
        return self.role

class Employee(models.Model):
    first_name = models.CharField(max_length=32, null=False)
    last_name = models.CharField(max_length=32, null=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)  # New field for soft deletion

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

# Optional: Create an ArchivedEmployee model if you need to store additional information
class ArchivedEmployee(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)  # Link to original Employee
    archived_date = models.DateTimeField(auto_now_add=True)  # Auto-record archiving time
    # Additional fields for archived information (optional)

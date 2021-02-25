# import the standard Django Model
# from built-in library
from django.db import models
from django.urls import reverse, reverse_lazy

# Create your models here.
# declare a new model with a name"employee"
class Employee(models.Model):
    # fields of the model
    eid = models.AutoField(primary_key=True,serialize = False,verbose_name ='ID')
    ename = models.CharField(max_length=100)
    eemail = models.EmailField()
    econtact = models.CharField(max_length=15)
    edob = models.DateField(blank=True, null=True)# If no date is selected then Django saves blank field value.

    def get_absolute_url(self):
        return reverse('employee-detail', kwargs={'pk': self.pk})
    #objects = models.Manager()
    class Meta:
        db_table = "employee"
        ordering = ['eid',]#sorts the records ascending using 'eid' field






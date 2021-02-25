from django.urls import reverse_lazy
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Employee

import pyautogui as pu


# Create your views here.
# Only logged in superuser can see this view
class EmployeeCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = Employee
    template_name = "create.html"
    fields=['eid','ename','eemail','econtact','edob']
    login_url = 'login'  #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully creation
    def get_success_url(self):
         #Displaying message of successful creation of new employee
         pu.alert(text='New Employee Created Successfully',title='Create',button='OK')
         return reverse_lazy('employees-list')


# Only logged in superuser can see this view
class EmployeeListView(LoginRequiredMixin,UserPassesTestMixin,ListView):

    model = Employee
    template_name = 'show.html'
    context_object_name = 'employees'
    paginate_by = 5
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser


    def get_queryset(self):  # new

        if self.request.method == "GET":
            query = self.request.GET.get('search')  # your input name is 'search'
            print('Search word:' + str(query))
        if query:
            return Employee.objects.filter(ename__icontains=query)

        else:
            return Employee.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EmployeeListView, self).get_context_data(**kwargs)
        employees = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(employees, self.paginate_by)
        try:
            employees = paginator.page(page)
        except PageNotAnInteger:
            employees = paginator.page(1)
        except EmptyPage:
            employees = paginator.page(paginator.num_pages)
        context['employees'] = employees
        return context



# Only logged in superuser can see this view
class EmployeeDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):

    model = Employee
    template_name = 'detail.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser
   

# Only logged in superuser can see this view
class EmployeeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Employee
    template_name = 'update.html'
    # specify the fields
    fields = ['eid', 'ename', 'eemail', 'econtact', 'edob']
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # updating details
    # url to redirect after successfully updation
    def get_success_url(self):
         # Displaying message of successful updation of  employee
         pu.alert(text='Employee Info Updated Successfully', title='Update', button='OK')
         return reverse_lazy('employees-list')



# Only logged in superuser can see this view
class EmployeeDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Employee
    template_name = 'delete.html'
    login_url = 'login' #if not authenticated redirect to login page

    # only superuser is allowed to see this view.
    def test_func(self):
        return self.request.user.is_superuser

    # url to redirect after successfully deletion
    def get_success_url(self):
        # Displaying message of successful deletion of employee
         pu.alert(text='Employee Deleted Successfully', title='Delete', button='OK')
         return reverse_lazy('employees-list')











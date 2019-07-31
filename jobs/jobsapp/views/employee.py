from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView, CreateView, ListView

from ..forms import EmployeeProfileUpdateForm, CreateEmployeeProfileForm
from ..models import User, EmployeeDetails, Hire, EmployeeProfile
from ..decorators import user_is_employee


class EditProfileView(UpdateView):
    model = User
    form_class = EmployeeProfileUpdateForm
    context_object_name = 'employee'
    template_name = 'jobs/employee/edit-profile.html'
    success_url = reverse_lazy('jobs:employee-profile')

    @method_decorator(login_required(login_url=reverse_lazy('jobs:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("User doesn't exists")
        # context = self.get_context_data(object=self.object)
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = self.request.user
        print(obj)
        if obj is None:
            raise Http404("Job doesn't exists")
        return obj


'''
class HirePerJobView(ListView):
    model = Hire
    template_name = 'jobs/employee/hire.html'
    context_object_name = 'hirer'
    paginate_by = 1

    @method_decorator(login_required(login_url=reverse_lazy('jobs:login')))
    @method_decorator(user_is_employee)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_queryset(self):
        return Hire.objects.filter(employeeDetails_id=self.kwargs['employeeDetails_id']).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employeeDetails'] = EmployeeDetails.objects.get(id=self.kwargs['employeeDetails_id'])
        return context
'''


class EmployeeProfileCreateView(CreateView):
    template_name = 'jobs/employee/employee_profile_details_create.html'
    form_class = CreateEmployeeProfileForm
    extra_context = {
        'title': 'Add Your Profile Details'
    }
    success_url = reverse_lazy('jobs:employee-profile')

    @method_decorator(login_required(login_url=reverse_lazy('jobs:login')))
    def dispatch(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return reverse_lazy('jobs:login')
        if self.request.user.is_authenticated and self.request.user.role != 'employee':
            return reverse_lazy('jobs:login')
        return super().dispatch(self.request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(EmployeeProfileCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


'''
class HirerListView(ListView):
    model = Hire
    template_name = 'jobs/employee/all-hirer.html'
    context_object_name = 'hirer'

    def get_queryset(self):
        # jobs = Job.objects.filter(user_id=self.request.user.id)
        return self.model.objects.filter(employeeDetails__user_id=self.request.user.id)

'''
'''
@login_required(login_url=reverse_lazy('jobs:login'))
def filled(request, employee_id = None):
    job = EmployeeDetails.objects.get(user_id=request.user.id, id=employee_id)
    job.filled = True
    job.save()
    return HttpResponseRedirect(reverse_lazy('jobs:employee-dashboard'))
'''


def view_employeeProfiles(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)


    else:
        user = request.user
    profile = EmployeeProfile.objects.get(user=user)
    args = {'user': user, 'profile': profile}

    return render(request, 'jobs/employee/profile.html', args)


def edit_employeeProfiles(request):
    pass

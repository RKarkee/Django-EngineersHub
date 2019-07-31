from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


from .views import *

app_name = "jobs"

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('search', SearchView.as_view(), name='search'),
    path('employer/dashboard', include([
        path('', DashboardView.as_view(), name='employer-dashboard'),
        path('all-applicants', ApplicantsListView.as_view(), name='employer-all-applicants'),
        path('applicants/<int:job_id>', ApplicantPerJobView.as_view(), name='employer-dashboard-applicants'),
        path('mark-filled/<int:job_id>', filled, name='job-mark-filled'),
    ])),
   # path('employee/dashboard',include([
    #    path('', EmployeeDashboardView.as_view(), name='employee-dashboard'),
    #])),
    path('apply-job/<int:job_id>', ApplyJobView.as_view(), name='apply-job'),
    path('jobs', JobListView.as_view(), name='jobs'),
    path('jobs/<int:id>', JobDetailsView.as_view(), name='jobs-detail'),
    path('employer/jobs/create', JobCreateView.as_view(), name='employer-jobs-create'),
    path('employee/register', RegisterEmployeeView.as_view(), name='employee-register'),
    path('employer/register', RegisterEmployerView.as_view(), name='employer-register'),
    path('employee/profile/update', EditProfileView.as_view(), name='employee-profile-update'),
    #path('employee',EmployeeDetailsListView.as_view(),name='employeeDetails'),
    #path('employeeDetails/<int:id>', EmployeeDetailsDetailsView.as_view(), name='employee-details'),
    #path('employeeProfile/<int:id>', EmployeeProfileDetailsView.as_view(), name='employee-profile-details'),
    #path('employeeDetails/<int:employeeDetails_id>',HireEmployeeView.as_view(), name='hire-employee'),
    # path('employee/employeeDetails/create',EmployeeDetailsCreateView.as_view(), name='employee-employeeDetails-create'),
    path('employee/profile',employee.view_employeeProfiles, name = 'employee-profile'),
    path('employee/profile/<int:pk>', employee.view_employeeProfiles, name='view_profile_with_pk'),
    path('employee/profile/add_details',EmployeeProfileCreateView.as_view(), name='employee-profile-add_details'),
    path('employee/profile/edit',employee.edit_employeeProfiles, name = 'employee-profile-edit'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('login', LoginView.as_view(), name='login'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django import template

from ..models import Applicant, Hire

register = template.Library()


@register.simple_tag(name='is_already_applied')
def is_already_applied(job, user):
    applied = Applicant.objects.filter(job=job, user=user)
    if applied:
        return True
    else:
        return False


@register.simple_tag(name='is_applied_already')
def is_already_applied(employeeDetails, user):
    applied = Hire.objects.filter(employeeDetails=employeeDetails, user=user)
    if applied:
        return True
    else:
        return False

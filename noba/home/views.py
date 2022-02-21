from django.shortcuts import render
from django.template import RequestContext


def page_not_found(request, exception):
    response = render(request, "404.html")
    response.status_code = 404
    return response


def internal_error(request):
    response = render(request,"500.html")
    response.status_code = 500
    return response
from django.http import response
from django.shortcuts import render


def home(request):
    return render(request, 'admin/base_site.html')

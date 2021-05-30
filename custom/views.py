from django.http import response
from django.shortcuts import render
from django.http import JsonResponse


def home(request):
    # return render(request, 'admin/base_site.html')
    return JsonResponse({'data': 'coming'})

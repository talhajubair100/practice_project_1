from django.shortcuts import render
from .models import District
# Create your views here.

def district_list(requets):
    district = District.objects.all()
    context = {'dist': district}
    return render(requets, 'address/district_list.html', context)

def district_details(request, id):
    detail_obj = District.objects.get(id=id)
    context = {'dist_detail': detail_obj}
    return render(request, 'address/district_details.html', context)
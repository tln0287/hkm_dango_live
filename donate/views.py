from django.shortcuts import render
from .models import AddDonation

# Create your views here.

def donate(request):
    data = AddDonation.objects.all()
    context = dict()
    context['data'] = data
    return render(request, 'donation.html', context)

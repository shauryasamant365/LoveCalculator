from django.shortcuts import render, redirect
from .models import *
import random

# Create your views here.
def index(request):
    return render(request, 'dashboard/index.html')


def results(request):
    if request.method == "POST":
        username = request.POST['username'].split(" ")[0].lower()
        partner = request.POST['partner'].split(" ")[0].lower()
        if (len(Calculation.objects.filter(username=username, partner=partner)) == 1):
            calculation = Calculation.objects.get(username=username, partner=partner)
            percentage = calculation.percentage
        elif (len(Calculation.objects.filter(username=partner, partner=username)) == 1):
            calculation = Calculation.objects.get(username=partner, partner=username)
            percentage = calculation.percentage
        elif username == partner:
            percentage = 100
        else:
            percentage = random.randint(20, 99)
            Calculation.objects.create(username=username.lower(), partner=partner.lower(), percentage=percentage)   
        return render(request, 'dashboard/results.html', {'username': username.title(), 'partner': partner.title(), 'percentage': percentage})


def about(request):
    return render(request, 'dashboard/about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        subject = request.POST["subject"]
        message = request.POST["message"]
        Contact.objects.create(name=name, email=email, subject=subject, message=message)
        return redirect("index")
    return render(request, 'dashboard/contact.html')
    
from django.shortcuts import render, redirect
from .models import Participant
from .forms import RegistrationForm
from django.http import FileResponse, Http404
import os

def download_file(request):
    pdf_path = 'static/Invitation Letter - cyber security.pf'  # Specify the path to your PDF file
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="your_pdf_file.pdf"'
            return response
    raise Http404("PDF file does not exist")


def main(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, "main.html", {'form': form})
    # return render(request,"main.html")

def home(request):
    return render(request,"workshop/home.html")

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = RegistrationForm()
    return render(request, 'workshop/register.html', {'form': form})

def registration_success(request):
    return render(request, 'workshop/registration_success.html')

from django.shortcuts import render, HttpResponse
from datetime import datetime
from api.models import Contact
from django.contrib import messages


# Create your views here.
def home(request):
    info = {
        'name': 'leave :)',
    }
    return render(request, 'index.html', info)

def about(request):
    return render(request, 'about.html')

def help(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        date = datetime.today()
        contact_data = Contact(email=email, password=password, date=date)
        contact_data.save()
        messages.success(request, 'Your email has been added !')

    return render(request, 'help.html')




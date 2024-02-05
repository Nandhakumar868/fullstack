from django.shortcuts import render
from .models import Registration_form
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def registration_view(request):
    
    if request.method == 'POST':   
        name = request.POST['firstname']
        email = request.POST['emailid']
        address = request.POST['addresss']
        phonenumber = request.POST['phonenumber']

        new_form = Registration_form(name=name,email=email,address=address,phone_no=phonenumber)
        new_form.save()
        return render(request, 'success.html') 
    else:
        form = Registration_form()
        return render(request, 'index.html', {'form': form})

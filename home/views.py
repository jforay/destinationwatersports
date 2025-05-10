from django.shortcuts import redirect, render

# Create your views here.
from .forms import ContactForm

def home(request):
    return render(request, 'home/home.html')

def saftey(request):
    return render(request, 'home/saftey.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the form data to the database
            return redirect('home')  # Redirect after POST
    else:
        form = ContactForm()
    return render(request,'home/contact.html', {'form':form})


def rates(request):
    return render(request, 'home/rates.html')
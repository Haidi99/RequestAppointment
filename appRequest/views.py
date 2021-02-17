from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .models import Person, Company
from .forms import RequestForm
from django.http import JsonResponse
from django.contrib import messages

def home(request):
    obj = Item.objects.all()
    return render(request, 'appRequest/home.html', {'obj':obj})

def form(request):
    if request.method == 'GET':
        return render(request, 'appRequest/form.html', {'form':RequestForm})
    else:
        try:
            form = RequestForm(request.POST)
            if form.is_valid():
                newrequest = form.save(commit=False)
                newrequest.save()
                messages.success(request, 'Your have booked your appointment successfully!')
            return render(request, 'appRequest/final.html')
        except ValueError:
            return render(request, 'appRequest/home.html', {'form':RequestForm(), 'error':'Bad data passed in. Try again.'})


'''def form(request):
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appRequest/final.html')
    return render(request, 'appRequest/home.html', {'form': form})
'''

    # AJAX
def load_companies(request):
    country_id = request.GET.get('country_id')
    companies = Company.objects.filter(country_id=country_id).all()
    return render(request, 'appRequest/company_dropdown_list_options.html', {'companies': companies})
    # al function de btgeeb al id bta3 al country w b3d keda btshof al companies ally btmatch 
    #m3 al country w tb3tha ll drop down list.

from django.http import request
from django.shortcuts import redirect, render
from .forms import PeopleForm, ActivitiesForm
from .models import People, Activities

# Create your views here.
def register(request):
    form = PeopleForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return redirect('display-activities')
    context = {'page_title': 'Register', 'form':form}
    return render(request, 'register_people.html', context)

def display(request):
    people = People.objects.all()
    activities = Activities.objects.all()
    context = {'people': people, 'activities': activities, 'page_title' : "Activities"}
    return render(request, "display_activities.html",context)

def register_activites(request):
    form = ActivitiesForm(request.POST or None)
    if (form.is_valid() and request.method == 'POST'):
        form.save()
        return redirect('display-activities')
    context = {'page_title': 'Register', 'form':form}
    return render(request, 'register_activities.html', context)
from django.shortcuts import render, redirect
from django.views.generic import ListView
from myclientapp.models import Person

# class PersonListView(ListView):
#     model = Person
#     template_name = 'person.html'
#     context_object_name = 'persons'
def index(request):
    data = Person.objects.all()
    return render(request, 'person.html', {'persons':data})

def add_tenant(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        try:
            person = Person.objects.get_or_create(first_name=fname, last_name=lname)
            return redirect('index')
        except Exception as e:
            print('Error',e)
    return render(request, 'add_person.html',{})



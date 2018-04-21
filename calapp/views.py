from django.shortcuts import render
from .models import Entry

# Create your views here.
def index(request):
    entries = Entry.objects.all()
    return render(request, "calapp/index.html",{'entries':entries})

def details(request):
    entry = Entry.objects.get(id=pk)
    return render(request, "calapp/details.html",{'entry':entry})

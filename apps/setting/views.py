from django.shortcuts import render

    #My imports
from .models import Setting,About,History
# Create your views here.
def index(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting":setting
    }
    return render(request, "setting/index-3.html", context)

def contact(request):
    setting = Setting.objects.latest("id")
    context = {
        "setting":setting
    }
    return render(request, "setting/contact.html", context)

def about(request):
    setting = Setting.objects.latest("id")
    about = About.objects.latest("id")
    history = History.objects.latest("id")
    context = {
        "setting":setting,
        "about":about,
        "history":history,
    }
    return render(request, "setting/about.html", context)
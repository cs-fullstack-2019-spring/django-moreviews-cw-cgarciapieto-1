from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup


# Create your views here.
def index(request):
    return HttpResponse("Test URL")
# function that takes a tring and places it after the word hello
def hello (request, person):
    return HttpResponse("hello" + str(person))

def times2 (request, number):
    return HttpResponse("The product times 2 is:" + str(number *2))

def total (request, number):
    for num in range(0, number+1):
        sum += num
        return HttpResponse("The sum of the number is " + sum)




# function that grabs all the cup objects

def getall(request):
    getallCups = Cup.objects.all()
    slightlynew= Cup.objects.filter(material__gte= "slightly new")
    context = {
        "getAllCups": getallCups,
        "slightlynew": slightlynew,
    }

    return render(request, "cupApp/index.html", context)
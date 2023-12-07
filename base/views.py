from django.shortcuts import render

# Create your views here.

rice = [
    {'id':1, 'name':'rice'}
]

def homepage(request):
    context= {'rice': rice}
    return render(request, 'home.html' ,context)
from django.shortcuts import render

def members(request):
    return render(request, 'myfirst.html')
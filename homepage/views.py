from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'home.html')

def adetera_view(request):
    return render(request,'adetera.html')

def matrix_view(request):
    return render(request,'matrix.html')

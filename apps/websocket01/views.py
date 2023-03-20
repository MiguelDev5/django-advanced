from django.shortcuts import render

# Create your views here.
def index(request):
    print("Se ejecutó index...")
    return render(request, 'index.html', {})
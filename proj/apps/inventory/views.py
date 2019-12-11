from django.shortcuts import render

# Create your views here.

# Create your views here.
def main(request):
    return render(request, 'inventory/index.html')

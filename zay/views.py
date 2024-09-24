from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'zay/index.html')
def about(request):
    return render(request, 'zay/about.html')
def shop(request):
    return render(request, 'zay/shop.html')
def contact(request):
    return render(request, 'zay/contact.html')
from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request,'home/index.html')
def about (request):
    return render(request,'home/about.html')
def contact (request):
    return render(request,'home/contact.html')
def gallery (request):
    return render(request,'home/gallery.html')
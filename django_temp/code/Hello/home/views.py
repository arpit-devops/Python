from django.shortcuts import render, HttpResponse

# Create your views here.

context= {
    "var1": "foo",
    "var2": "bar"
}

def index(request):
    return render(request, "index.html", context)
    #return HttpResponse("this is home page")

def about(request):
    return HttpResponse("this is about page")

def service(request):
    return HttpResponse("this is service page")
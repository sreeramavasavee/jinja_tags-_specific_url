from django.shortcuts import render

# Create your views here.
def jinja2(request):
    d={'name':'keerthi','age':50}
    return render(request,'jinja2.html',context=d)
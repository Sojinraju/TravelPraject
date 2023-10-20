from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()

    return render(request, "index.html",{'result':obj,'res':ob})

    #  name="india",{'obj':name}
# def about(request):
# return render(request,("result.html"))
# def contact(request):
# return HttpResponse("Hello am contact")
# def result(request):
#   x=int(request.GET['num1'])
# y=int(request.GET['num2'])
#  a=x+y
#  s=x-y
#  m=x*y
#  d=x/y
#  return render(request,"result.html",{'add':a,'sub':s,'mul':m,'div':d})

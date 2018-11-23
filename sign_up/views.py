from django.http import HttpResponse
from django.template import loader
from .models import *
from django.utils.datastructures import MultiValueDictKeyError

def adddata(request):
    fn = request.POST['t1']
    ln = request.POST['t2']
    rn = request.POST['t3']
    br = request.POST['c1']
    ph = request.FILES['photo']
    if Student.objects.filter(roll_no=rn):
        return HttpResponse("This roll no is already registered")
    else:
        studentObj = Student.objects.create(
            first_name = fn,
            last_name = ln,
            roll_no = rn,
            image = ph,
            branch = br,
            )
        studentObj.save()
        return HttpResponse("You successfully signed up")


def index(request):
    template = loader.get_template('sign_up/index.html')
    context = {}
    return HttpResponse(template.render(context,request))
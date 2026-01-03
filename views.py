from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    our_dict={'insert_text':'This is a Django app coming from first_app/index.html!'}
    return render(request,'first_app/index.html',context=our_dict)
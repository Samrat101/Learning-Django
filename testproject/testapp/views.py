from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={"insert_content":"THIS IS JUST A TEST APP"}
    return render(request,'testapp/index.html',context=my_dict)

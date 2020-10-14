from django.shortcuts import render
from apptwo.models import user
# Create your views here.

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    user_list=user.objects.order_by('first_name')
    user_dict={'users':user_list}
    return render(request,'apptwo/users.html',context=user_dict)

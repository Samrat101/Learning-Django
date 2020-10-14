from django.shortcuts import render
# from apptwo.models import user
# Create your views here.
from apptwo.forms import NewUserForm

def index(request):
    return render(request,'apptwo/index.html')

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR FORM IS INVALID")

    return render(request,'apptwo/users.html',{'form':form})

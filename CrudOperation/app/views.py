
from django.shortcuts import render
from.forms import StudentRegForm
from.models import StudntRegistration
# Create your views here.
def showform(request):
    if request.method == "POST":
        form = StudentRegForm(request.POST)
        if form.is_valid():
            Name = form.cleaned_data['name']
            Email = form.cleaned_data['email']
            Department = form.cleaned_data['department']
            Mobile = form.cleaned_data['mobno']
            studentdata =StudntRegistration(name=Name,email=Email, department= Department,mobno=Mobile)
            studentdata.save()
            form = StudentRegForm()
    else:
        form = StudentRegForm()

    return render(request,'home.html',{'form':form})



def showprofile(request):
    student_details = StudntRegistration.objects.all()
    return render(request,'stdetails.html',{'stprofile':student_details})
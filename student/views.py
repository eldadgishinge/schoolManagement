from django.shortcuts import render,redirect
from .forms import StudentForm




# Create your views here.

def student_form(request):
    if request.method=="POST":
        form= StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_form')
        else:
            print(form.errors)
    else:
        form= StudentForm()
    return render(request, "index.html", {"form": form})



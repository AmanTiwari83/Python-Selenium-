from django.shortcuts import render
from  django.core.mail import  send_mail


# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST["name"]
        subject=request.POST["subject"]
        semail=request.POST['semail']
        remail=request.POST['remail']
        image=request.POST['image']
        send_mail(
            subject,
            image,
            name,
            'amantiwari22062004@gmail.com',
            [remail],
            fail_silently=False
        )
    return render(request,"./index.html")

def thank(request):
    return render(request,"thank.html")
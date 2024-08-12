from .models import newsletter
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import JobApplication, SpaceImg, EmsImg, AcvImg
from django.conf import settings
from django.core.files.storage import FileSystemStorage


# Create your views here.
def loadindex(request):
    if request.method == "POST" and all(field in request.POST for field in ['username', 'email']):
        name = request.POST['username']
        mail = request.POST['email']
        obj_newsletter = newsletter(username=name, email=mail)
        obj_newsletter.save()
    return render(request, "index.html")


def loadabout(request):
    return render(request, "about.html")

# services start
def loadservice(request):
    return render(request,"service.html")

def pcba(request):
    return render(request,"PCB-Assembly.html")

def smt(request):
    return render(request,"smt.html")

def thole(request):
    return render(request,"WaveSolder(TH)Assembly.html")

def bga(request):
    return render(request,"bga.html")

def turnkey(request):
    return render(request,"TurnkeyAssembly.html")

def boxb(request):
    return render(request,"BoxBuildAssembly.html")

def cem(request):
    return render(request,"ContractElectronicManufacturing.html")

def pcbspacegrade(request):
    return render(request,"aero-space grade product.html")

def pcbaerospacedefence(request):
    return render(request,"pcb-aerospace-defence.html")

def loadinfrastructure(request):
    return render(request,"infrastructure.html")

def projectcompleted(request):
    return render(request,"")


def emvariousindus(request):
    projects = EmsImg.objects.all()
    return render(request, "emvariousindus.html", {'projects': projects})

def spacequalified(request):
    images = SpaceImg.objects.all()
    return render(request, "spacequalified.html", {'images': images})

# services end

# pages start

def achievement(request):
    images = AcvImg.objects.all()
    return render(request, "achievement.html", {'images': images})


def awardscertificate(request):
    return render(request,"award-certificate.html")


def careers(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        position_applied_for = request.POST['options']
        experience = request.POST['experience']
        resume = request.FILES['file']

        # Save the application to the database
        job_application = JobApplication(
            name=name,
            email=email,
            mobile=mobile,
            position_applied_for=position_applied_for,
            experience=experience,
            resume=resume
        )
        job_application.save()

        # Save the resume file
        fs = FileSystemStorage()
        filename = fs.save(resume.name, resume)
        resume_url = fs.url(filename)

        # Send an email with the form details
        email_subject = 'New Job Application'
        email_body = f"""
        Name: {name}
        Email: {email}
        Mobile: {mobile}
        Position Applied For: {position_applied_for}
        Experience: {experience}
        Resume: {resume_url}
        """

        email = EmailMessage(
            email_subject,
            email_body,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_RECEIVER]
        )
        email.attach(resume.name, resume.read(), resume.content_type)
        email.send()
        response_html = """
        <html>
            <head>
                <meta http-equiv="refresh" content="5;url=/careers/" />
            </head>
            <body>
                <p>Thank you for your application. You will be redirected back to the careers page in 5 seconds.</p>
            </body>
        </html>
        """
        return HttpResponse(response_html)

    return render(request, "careers.html")


def testimonial(request):
    return render(request,"testimonial.html")

# pages stop

@csrf_exempt

def loadcontact(request):
    if request.method == 'POST':
        yourname = request.POST.get('yourname')
        gmail = request.POST.get('gmail')
        subject = request.POST.get('subject')
        mobile = request.POST.get('mobile')  # Get mobile number
        message = request.POST.get('message')

        contact = Contact(yourname=yourname, gmail=gmail, subject=subject, mobile=mobile, message=message)
        contact.save()

        # Send email
        send_mail(
            subject,
            f'Name: {yourname}\nEmail: {gmail}\nMobile: {mobile}\n\nMessage:\n{message}',
            'your_email@gmail.com',  # From email
            ['smartparkings11@gmail.com'],  # To email
            fail_silently=False,
        )

        return redirect('/loadcontact')  # Redirect to a success page after saving

    return render(request, "contact.html")

def success(request):
    return render(request, 'success.html')

from django.shortcuts import render, redirect,HttpResponse
from home.models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate

def home(request):

      return render(request, "home/index.html")
def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        msg = request.POST.get('comment')
        con = Contact(name=name, email=email, message=msg, mobile=mobile)
        con.save()
        return redirect('/contact')
    allpost = Contact.objects.all()[::-1]
    post = Post.objects.all()
    data = {'allpost': allpost, 'posts': post}
    return render(request,  "home/contact.html", data)

def loginform(request):
    show = SignupForm()
    showl = LoginForm()
    context = {'showsignup': show , 'showlogin': showl}
    return render(request, "home/loginform.html", context)

def signup(request):

        if request.method == "POST":
            fm = SignupForm(request.POST)
            if fm.is_valid():
                name = fm.cleaned_data['name']
                email = fm.cleaned_data['email']
                username = fm.cleaned_data['mobile']
                passw = fm.cleaned_data['password']
            myuser = User.objects.filter(username=username)

            if myuser.exists():
                messages.error(request, 'Not Signup, Username already taken')
                return redirect('/signup')

            myuser = User.objects.create_user(username, email, passw)
            myuser.first_name = name
            myuser.save()
            messages.success(request, 'Successfully Created Your Account')
            return redirect('/loginform')
        else:
            fm = SignupForm()

        return render(request, 'home/signup.html', {'fm': fm})

def login_page(request):

        fm = LoginForm()
        if request.method == 'POST':
            fm = LoginForm(request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['mobile']
                passw = fm.cleaned_data['password']
            if not User.objects.filter(username=username).exists():
                messages.error(request, 'Invalid Username')
                return redirect('/loginform')

            myuser = authenticate(username=username, password=passw)
            if myuser is None:
                messages.error(request, 'Invalid Password')
                return redirect('/loginform')
            else:
                auth_login(request, myuser)
                messages.success(request, 'Successfully loginform')
                return redirect('/changepassword')

        return render(request, 'home/loginform.html', {'fm': fm})


def logout_page(request):
    auth_logout(request)
    messages.success(request, 'Account logout')
    return redirect('/loginform')


def product(request):
    post = Post.objects.all()
    return render(request, 'home/product.html', {'posts': post})

def jobs(request):
    job = Addjob.objects.all()[::-1]
    return render(request, 'home/jobs.html', {'job':job})


def aboutus(request):
    return render(request, 'home/aboutus.html')

def viewcontact(request):

    allpost = Contact.objects.all()[::-1]
    return render(request, 'aprofile/viewcontact.html', {'allpost':allpost})

def addjob(request):

    if request.method == "POST":
        jobtitle = request.POST.get('jobtitle')
        salary = request.POST.get('salary')
        experience = request.POST.get('experience')
        location = request.POST.get('location')
        con = Addjob(jobtitle=jobtitle, salary=salary, experience=experience, location=location)
        con.save()
        return redirect('/addjob')


    return render(request, 'aprofile/addjob.html')


def addnotification(request):

    if request.method == "POST":
        notification = request.POST.get('notification')

        con = Addnotification(notification=notification)
        con.save()
        return redirect('/addnotification')

    noti = Addnotification.objects.all()
    return render(request, 'aprofile/addnotification.html', {"noti": noti})

def viewemployee(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp
    }

    return render(request, 'aprofile/viewemployee.html', {'emp': emp})


def add(request):


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone,
         )
        emp.save()
        return redirect('viewemployee')
    return render(request, 'aprofile/viewemployee.html', )

def edit(request):
    emp = Employee.objects.all()
    context = {
        'emp': emp,
    }
    return redirect(request, 'aprofile/viewemployee.html', context)
def update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('viewemployee')

    return redirect(request, 'aprofile/viewemployee.html')

def delete(request, id):
        emp = Employee.objects.filter(id=id)
        emp.delete()
        context = {
            'emp': emp,
        }

        return redirect('viewemployee')


def viewcomplain(request):
    comp = Complain.objects.all()
    return render(request, 'aprofile/viewcomplain.html', {'comp':  comp})

def viewfeedback(request):
    feed = Feedback.objects.all()
    return render(request, 'aprofile/viewfeedback.html', {'feed': feed})
@login_required()
def complain(request):



    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        complain = request.POST.get('complain')
        con = Complain(name=name, email=email, complain=complain)
        con.save()
        return redirect('/complain')

    return render(request,  "aprofile/complain.html")
@login_required()
def feedback(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        fdk = Feedback(name=name, email=email, feedback=feedback)
        fdk.save()
        return redirect('/feedback')



    return render(request,  "aprofile/feedback.html")


@login_required()
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            v = form.save()
            update_session_auth_hash(request, v)
            return HttpResponse(' Password Change Successfully !!!')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'form': form,

    }

    return render(request, 'aprofile/changepassword.html', context)



def subscriber(request):

    myuser= User.objects.all()
    return render(request, 'aprofile/subscriber.html', {'myuser':myuser})




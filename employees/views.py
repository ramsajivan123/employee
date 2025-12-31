from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User, auth
from .models import employee,feedback  # you can do all models imoprt by *   
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")

def login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['pass']
        data = authenticate(username=u,password=p)
        try:
            if data.is_staff:
                auth.login(request,data)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d ={'log':error}
    return render(request,"login.html",d)

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def admin_dashboard(request):
    return render(request,"dashboard.html")

@login_required(login_url='login')
def add(request):
    error = ""
    if request.method == "POST":
        n = request.POST['fname']
        e = request.POST['email']
        p = request.POST['phone']
        post = request.POST['post']
        g = request.POST['gender']
        s = request.POST['salary']
        a = request.POST['address']
        state = request.POST['state']
        img=request.FILES['image']
        try:
            employee.objects.create(full_name=n,email=e,phone=p,gender=g,post=post,salary=s,address=a,state=state,image=img)
            error="no"
        except:
            error="yes"
    return render(request,"add_recoards.html",{'error':error})

@login_required(login_url='login')
def view_employee(request):
    info = employee.objects.all()
    d = {'data':info}
    return render(request,"view_recoards.html",d)

@login_required(login_url='login')
def edit_employee(request):
    return render(request,"edit_recoards.html",{'data':employee.objects.all()})

@login_required(login_url='login')
def edit_form(request,id):
    error = ""
    data = employee.objects.get(id=id)
    if request.method == "POST":
        n = request.POST['fname']
        e = request.POST['email']
        ph = request.POST['phone']
        p = request.POST['post']
        g = request.POST['gender']
        sal = request.POST['salary']
        a = request.POST['address']
        s = request.POST['state']
        img = request.FILES['image']

        data.full_name = n
        data.email = e
        data.phone = ph
        data.post = p
        data.gender = g
        data.salary = sal
        data.address = a
        data.state = s
        data.image = img

        try:
            data.save()
            error = "no"
        except:
            error = "yes" 

    d = {'data':data,'error':error}
    return render(request,"edit_action.html",d)

@login_required(login_url='login')
def del_action(request,id):
    data = employee.objects.get(id=id)
    data.delete()
    return redirect('edit_recoards')

def about(request):
    return render(request,"about.html")

def feedback_form(request):
    error=""
    if request.method == "POST":
        n = request.POST['fname']
        e = request.POST['email']
        f = request.POST['feedback']
        try:
            feedback.objects.create(full_name=n,email=e,massage=f)
            error="no"
        except:
            error="yes"
    d ={'error':error}        
    return render(request,"feedback.html",d)

@login_required(login_url='login')
def view_feedback(request):
    data = feedback.objects.all()
    d ={'data':data}
    return render(request,"view_feedback.html",d)

@login_required(login_url='login')
def change_pass(request):
    error = ""

    if request.method == "POST":
        cp = request.POST['cerrent_p']
        np = request.POST['new_p']
        con_p = request.POST['conferm_p']

        logined = request.user
        if logined.check_password(cp):
            if np == con_p:
                error ="no"
                logined.set_password(np)
                logined.save()
            else:
                error ="yes"
        else:
                error ="old"        
    d ={'error':error}
    return render(request,"change_pass.html",d)

def footer(request):
    return render(request,"footer.html")

def photos(request):
    return render(request,"gallery.html")
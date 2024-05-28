from django.shortcuts import render, redirect
from core.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from datetime import date

# Create your views here.


def Registration(request):
    context = {"title": "Signup"}
    if request.method == "POST":
        data = request.POST
        print(data)
        name = data.get("name")
        dob = data.get("dob")
        gender = data.get("gender")
        email = data.get("email")
        password = data.get("password")
        no = data.get("mobile")
        address = data.get("address")
        state = data.get("state")
        education = data.get("education")
        image = request.FILES.get("image")

        user = MyUser.objects.create(
            name=name,
            dob=dob,
            gender=gender,
            email=email,
            no=no,
            address=address,
            state=state,
            education=education,
            image=image,
        )
        user.set_password(password)
        user.save()
        return redirect("login")

    return render(request, "UserRegisteration.html", context=context)


def MyLogin(request):
    context = {"title": "Login"}
    if not request.user.is_authenticated:
        if request.method == "POST":
            data = request.POST
            if request.method == "POST":
                email = request.POST.get("email")
                password = request.POST.get("password")

            if not MyUser.objects.filter(email=email).exists():
                messages.info(request, "Account not exist Please create one!!")
                return redirect("reg")

            user = authenticate(request, email=email, password=password)

            if user is None:
                messages.info(request, "Invalid Password")
                return redirect("login")
            else:
                login(request, user)
                messages.info(request, "Login Sucessfull")
                return redirect("view")

        return render(request, "login.html", context=context)
    else:
        context = {"title": "Home"}
        return render(request, "view.html", context=context)


@login_required(login_url="login")
def addjob(request):
    context = {"title": "Add Job"}
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        skill = data.get("skill")
        duration = data.get("duration")
        salary = data.get("salary")
        deadline = data.get("deadline")
        number = data.get("number")
        vacancy = data.get("vacancy")

        Jobs.objects.create(
            user=request.user,
            title=title,
            skill=skill,
            duration=duration,
            salary=salary,
            deadline=deadline,
            vacancy=vacancy,
        )
    return render(request, "add.html", context=context)


@login_required(login_url="login")
def stream(request):
    if request.method == "POST":
        search = request.POST["search"]
        print(search)
        queryset = Jobs.objects.filter(
            Q(title__icontains=search) | Q(skill__icontains=search)
        )
        contex = {"data": queryset}
        return render(request, "view.html", context=contex)

    queryset = Jobs.objects.all()
    newqueryset = []
    for job in queryset:
        if job.deadline >= date.today():
            newqueryset.append(job)
    contex = {"data": queryset, "title": "Home"}
    return render(request, "view.html", context=contex)


@login_required(login_url="login")
def mylogout(request):
    logout(request)
    return redirect("login")


def profile(request, id):
    if request.method == "POST":
        user = request.user
        resume = request.FILES.get("resume")
        user.resume = resume
        user.save()

    user = MyUser.objects.get(id=id)
    title = user.name + "'s Profile"
    print(title)
    context = {"user": user, "title": title}

    return render(request, "profile.html", context=context)

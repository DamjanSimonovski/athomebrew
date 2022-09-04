from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .models import Courses
from .forms import CourseForm
from .forms import RegisterForm


# Create your views here.

def register_request(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("main:login")
        messages.error(request, "Invalid information.")
    form = RegisterForm
    return render(request=request, template_name="register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("main:home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("main:login_register")


def login_register(request):
    return render(request, "login_register.html")


def home(request):
    queryset = Courses.objects.all()
    context = {"courses": queryset}
    return render(request, "home.html", context=context)


def coursePage(request):
    queryset = Courses.objects.all()
    context = {"courses": queryset, "form": CourseForm}
    return render(request, "courses.html", context=context)


def you_coursePage(request):
    queryset = Courses.objects.all()
    context = {"courses": queryset, "form": CourseForm}
    return render(request, "you_courses.html", context=context)


def userPage(request):
    queryset = RegisterForm.save
    context = {"user": queryset, "form": RegisterForm}
    return render(request, "user.html")


def searchPage(request):
    queryset = Courses.objects.all()
    context = {"courses": queryset, "form": CourseForm}
    return render(request, "search.html", context=context)

def ttPage(request):
    return render(request, "tt.html")

def displayPage(request, id_course):
    course = Courses.objects.get(id=id_course)
    context = {"single": course}
    return render(request, "display.html", context)

def quizPage(request, id_course):
    course = Courses.objects.get(id=id_course)
    context = {"course": course}
    return render(request, "quiz.html", context)

def resultsPage(request):
    return render(request, "results.html")

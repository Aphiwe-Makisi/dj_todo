from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from todos.forms import RegistrationForm, LoginForm, TodoForm
from todos.models import Todo

# Create your views here.
def home(request):
  return render(request, "todos/home.html")

@login_required(login_url="todos:login")
def dashboard(request):

  todos = Todo.objects.filter(user=request.user)

  form = TodoForm()
  context = {"form": form, "todos": todos}
  return render(request, "todos/dashboard.html", context=context)

def register(request):
  if request.method == "POST":
    form = RegistrationForm(request.POST)
    
    if form.is_valid():
      form.save()
      return redirect("todos:login")
    else:
      # invalid form logic
      pass
  else:
    form = RegistrationForm()
  
  context = {"form": form}
  return render(request, "todos/register.html", context=context)


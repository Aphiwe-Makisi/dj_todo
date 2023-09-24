from django.shortcuts import get_object_or_404, redirect, render
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
  context = {"todos": todos}
  return render(request, "todos/dashboard.html", context=context)

@login_required(login_url="todos:login")
def create_todo(request):
  # if method used in form is post
  if request.method == "POST":
    # then create the form
    form = TodoForm(request.POST)

    # if form is valid save and redirect
    if form.is_valid():
      todo = form.save(commit=False)
      todo.user = request.user
      todo.save()
      return redirect("todos:dashboard")
  else:    
    form = TodoForm() # display an empty form

  context = {"form": form}
  return render(request, "todos/create.html", context=context)
  
@login_required(login_url="todos:login")
def update_todo(request, id):
  todo = get_object_or_404(Todo, pk=id)
  
  if request.method == "POST":
    form = TodoForm(request.POST, instance=todo)

    if form.is_valid():
      form.save()
      return redirect("todos:dashboard")

  else:
    form = TodoForm(instance=todo)
  
  context = {"form": form, "id": id}
  return render(request, "todos/update.html", context=context)

@login_required(login_url="todos:login")
def delete_todo(request, id):
  todo = get_object_or_404(Todo, id=id)
  todo.delete()
  return redirect("todos:dashboard")

@login_required(login_url="todos:login")
def profile(request, id):
  return render(request, "todos/profile.html")

@login_required(login_url="todos:login")
def update_profile(request, id):
  return render(request, "todos/update_profile.html")

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


from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from todos.forms import RegistrationForm

# Create your views here.
def home(request):
  return render(request, "todos/home.html")

@login_required
def dashboard(request):
  return render(request, "")

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


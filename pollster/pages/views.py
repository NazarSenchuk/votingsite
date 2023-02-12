from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from polls.models import VotesMember,Choice
from django.contrib.auth.models import User
from .forms import LoginForm
def index(request):
  
  
  
  if request.method == "POST":
    
    username =  request.POST.get('username')
    password = 'Senchuknazar6'
    User.objects.create_user( username =username , password  = password)
      
      
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request,user)
      return redirect('polls:index')
    else:
      print('не вошел ')
  return render(request, 'pages/index.html',)
def change_username(request):
  user = request.user
  print(user)
  if request.method == 'POST':
    new_username  = request.POST.get('username')
    user.username = new_username
    user.save()
  return redirect('index')

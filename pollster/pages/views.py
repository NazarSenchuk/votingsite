from django.shortcuts import render,redirect
from polls.models import MyUser, VotesMember,Choice
def index(request):
  
  if request.method == "POST":
    print(request.POST)
    username = request.POST.get('username')
    user,created = MyUser.objects.get_or_create(username = username)
    print(user)
    choice = Choice.objects.all().first()
    VotesMember.objects.create(choice = choice , user = user)
    return redirect('polls:index')
  return render(request, 'pages/index.html')

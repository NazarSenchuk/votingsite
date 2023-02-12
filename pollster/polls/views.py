from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect , JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from . import forms
from .models import Question, VotesMember,Choice

# Get questions and display them
def index(request):
    form = forms.QuestionForm()
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list, 'form':form}
        
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
  try:
    question = Question.objects.get(pk=question_id)
  except Question.DoesNotExist:
    raise Http404("Question does not exist")
  return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'polls/results.html', { 'question': question })

# Vote for a question choice
def vote(request, question_id):
    # print(request.POST['choice'])
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        VotesMember.objects.create(choice =selected_choice,user = request.user)
        
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
def resultsData(request,obj):
    votens  = []
    items  =  [ ]
    question = Question.objects.get(id = obj)
    votes  = question.choice_set.all()

    for  i in votes:
        items.append(i.choice_text)
        votens.append(i.votes)
    votedata =  [items,votens]
    print(votedata)
    return JsonResponse(votedata ,safe = False  )
def create_question(request):
    
    if request.method == 'POST':
        form = forms.QuestionForm(request.POST)
        if form.is_valid :
            form.save()
    return redirect('polls:index')
     
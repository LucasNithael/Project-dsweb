from django.shortcuts import render, redirect
from .models import Question, Alternative

def index_view(request):
    questions = Question.objects.all().order_by('-id')
    
    return render(
        request,
        'polls/index.html',
        {'questions': questions}
    )


def alternative_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    alternatives = Alternative.objects.filter(question=question).order_by('-vote')
    
    total_vote = 0
    for alternative in alternatives:
        total_vote += alternative.total_vote()


    return render(
        request, 
        'polls/alternative.html',
        {'alternatives': alternatives,
         'question': question,
         'total_vote': total_vote,        
        })


def vote_view(request, alternative_id):
    alternative = Alternative.objects.get(id=alternative_id)
    alternative.vote = alternative.vote + 1
    question_id = alternative.question.id
    alternative.save()
    return redirect('polls:alternative', question_id)

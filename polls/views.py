from django.shortcuts import render
from .models import Question, Alternative

def index_view(request):
    questions = Question.objects.all()
    
    return render(
        request,
        'polls/index.html',
        {'questions': questions}
    )


def alternative_view(request, question_id):
    question = Question.objects.get(pk=question_id)
    alternatives = Alternative.objects.filter(question=question)

    return render(
        request, 
        'polls/alternative.html',
        {'alternatives': alternatives,
         'question': question        
        })
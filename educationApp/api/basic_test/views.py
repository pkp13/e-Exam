from django.shortcuts import render
from api.questions.models import Question
# Create your views here.

def onlineTest(request):
    if request.method == "GET":
        start = True
    else:
        start = False

    testQuestion = Question.objects.all()
    
    start = False
    return render(request, 'test.html', {'question': testQuestion,
                                            'submited': False,
                                            'start': True,
                                        })
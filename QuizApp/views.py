from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from .models import *



# Create your views here.

score = 0

def home(request):
    return render(request, 'index.html')
    



def basic(request):
    global score
    basic = Basic.objects.all()
    if request.method == 'POST':
        answer = request.POST
        print(answer)
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = Basic.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'basic.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(basic), "basic":basic})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "basic.html", {
        "basic": basic
    })
    return render(request, 'basic.html')


def datatypes(request):
    global score
    dtypes = DataTypes.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = DataTypes.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1
        
                else:
                    print(result)
        print(score)
        # return render(request, 'dtypes.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(dtypes), "dtypes":dtypes})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "dtypes.html", {
        "dtypes": dtypes
    })
    return render(request, 'dtypes.html')



def operators(request):
    global score
    operators = Operators.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = Operators.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'operators.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(operators), "operators":operators})
        return HttpResponseRedirect(reverse('result'))
        
    return render(request, "operators.html", {
        "operators": operators
    })
    return render(request, 'operators.html') 


def con_statements(request):
    global score
    conditional = Con_statements.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = Con_statements.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'conditional.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(conditional), "conditional":conditional})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "conditional.html", {
        "conditional": conditional
    })
    return render(request, 'conditional.html') 
    

def loops(request):
    global score
    loops = looping.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = looping.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'loop.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(loops), "loops":loops})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "loop.html", {
        "loops": loops
    })
    return render(request, 'loop.html') 



def function(request):
    global score
    function = functions.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = functions.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'functions.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(function), "function":function})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "functions.html", {
        "function": function
    })
    return render(request, 'functions.html') 




def exceptHandle(request):
    global score
    ExceptHand = ExceptionHandling.objects.all()
    if request.method == 'POST':
        answer = request.POST
        Total_ques = len(answer)-1
        score = 0
        for i in answer:
            if i.isnumeric():
                result = ExceptionHandling.objects.filter(id = i)[0].correct_ans
                if result == answer[i]:
                    score += 1

                else:
                    print(result)
        # return render(request, 'eh.html', {'score':score, 'ques_answered':Total_ques, 'Total_ques':len(ExceptHand), "ExceptHand":ExceptHand})
        return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "eh.html", {
        "ExceptHand": ExceptHand
    })
    return render(request, 'eh.html') 


def Result(request):
    print(score)
    return render(request, 'result.html', {'score':score})

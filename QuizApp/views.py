from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, response
from django.urls import reverse
from .models import *



# Create your views here.


def home(request):
    return render(request, 'index.html')
    



def basic(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "basic.html", {
        "basic": basic
    })
    return render(request, 'basic.html')


def datatypes(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "dtypes.html", {
        "dtypes": dtypes
    })
    return render(request, 'dtypes.html')



def operators(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
        
    return render(request, "operators.html", {
        "operators": operators
    })
    return render(request, 'operators.html') 


def con_statements(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "conditional.html", {
        "conditional": conditional
    })
    return render(request, 'conditional.html') 
    

def loops(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "loop.html", {
        "loops": loops
    })
    return render(request, 'loop.html') 



def function(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "functions.html", {
        "function": function
    })
    return render(request, 'functions.html') 




def exceptHandle(request):
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
        return render(request, 'result.html', {'score':score})
#         return HttpResponseRedirect(reverse('result'))
    
        
    return render(request, "eh.html", {
        "ExceptHand": ExceptHand
    })
    return render(request, 'eh.html') 


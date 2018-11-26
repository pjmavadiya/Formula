from django.shortcuts import render
from django.http import HttpResponse

from models import Formula
# Create your views here.


OPERATOR_CHOICES  = {'ADDITION': '+', 'SUBTRACTION': '-', 'DIVISION': '/', 'MULTIPLICATION': '*'}

values = []
err = False

def test(request):

    data = Formula.objects.all()
    for d in data:
        if d.operator:
            d.operator = OPERATOR_CHOICES[d.operator]
    formula = request.GET['q']
    answer = find_value(request, True)
    return render(request, 'calc.html', {'data': data, 'answer':answer, 'formula':formula})
    #return render(request, 'calc.html')


def find_value(request, inter=False):

    if 'q' in request.GET:
        data = request.GET['q']
        try:
            answer,func_name = calculator(data.split(' '))
        except:
            return HttpResponse("Func defined incorrectly")

        if not answer:
            return HttpResponse("Function not defined")

        global values
        values = []
        if inter:
            return answer
        return HttpResponse(str(answer))


def diaplay_table(request):
    data = Formula.objects.all()
    for d in data:
        if d.operator:
            d.operator = OPERATOR_CHOICES[d.operator]
    return render(request, 'formula.html', {'data': data})


def check_val(val):
    if val.isdigit():
        return val
    for OP in OPERATOR_CHOICES:
        if OPERATOR_CHOICES[OP] == str(val) or OP == str(val):
            return OPERATOR_CHOICES[OP]
    return False

def calculator(data, rec=False):
    value = 0
    global values
    for d in data:
        if not d:
            continue
        is_val = check_val(d)
        #If its degit or operator append to list else perform recursion
        if is_val:
            values.append(is_val)
        else:
            is_exist = Formula.objects.filter(name=d)
            if is_exist:
                calculator([is_exist[0].operandA, is_exist[0].operator, is_exist[0].operandB], True)
            else:
                print d
                global err
                err = True
    if rec:
        return
    if not err:
        print values
        value = eval("".join(values))
    else:
        value,False
    return value,0
            

def calculate(request):
    data = request.GET.get('custom_formula', None)
    if not data:
        return HttpResponse("No data provided")

    try:
        answer,func_name = calculator(data.split(' '))
    except:
        return HttpResponse("Func defined incorrectly")

    if not answer:
        return HttpResponse("Function not defined")

    global values
    values = []
    return HttpResponse(str(answer))



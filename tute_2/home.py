from django.shortcuts import render
import random
def printing(request):
    return render(request, 'index.html')

def change(request):

    text=(request.POST.get('textarea','default'))
    capital=(request.POST.get('capital','off'))
    jumble=(request.POST.get('jumble','off'))
    num1=(request.POST.get('num1'))
    num2=(request.POST.get('num2'))

    changed=""
    jumbled=''
    word={}
    j=text.split(" ")
    (random.shuffle(j))

    if capital=='on':
        for char in text:
            changed=changed+char.upper()
            word = {'capital_text':changed}
    elif jumble=='on':
        for char in j:
            jumbled=(char+" "+jumbled)
            word={'jumble':jumbled}
    elif num1!='':
        sum=f"Sum= {num1+num2}"
        word={'sum':sum}
    else:
        changed=text
        word = {'purpose':changed}
    return render(request, 'capital.html', word)



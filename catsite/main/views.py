from django.shortcuts import render

def index(request):
    return render(request, 'main/homepage.html')

def contact(request):
    return render(request, 'main/basic.html', {'values':['Если остались вопросы - задавайте их по телефону:',
                                                          '8(965)2647790', 'genesis0@yandex.ru']})
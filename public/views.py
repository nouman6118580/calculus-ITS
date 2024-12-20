from django.shortcuts import render


def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def signUp(request):
    return render(request, 'signup.html')

def about(request):
    return render(request, 'about.html')

def quiz(request):
    return render(request, 'quiz.html')

def startQuiz(request):
    return render(request, 'start-quiz.html')   

def calculator(request):
    return render(request, 'calculator.html')   

def dashboard(request):
    return render(request, 'dashboard.html')  

def courses(request):
    return render(request, 'courses.html')  

def courseContent(request):
    return render(request, 'course-content.html') 

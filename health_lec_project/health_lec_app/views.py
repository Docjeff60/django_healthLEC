from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'health_lec_app/index.html')


def dashboard(request):
    return render(request, 'health_lec_app/dashboard.html')


def find_a_doctor_home(request):
    return render(request, 'health_lec_app/find-a-doctor-home.html')


def find_facility(request):
    return render(request, 'health_lec_app/find-facility.html')


def for_professionals(request):
    return render(request, 'health_lec_app/for-professionals.html')


def health_blog(request):
    return render(request, 'health_lec_app/health-blog.html')


def signup(request):
    return render(request, 'health_lec_app/signUp.html')


def telehealth(request):
    return render(request, 'health_lec_app/telehealth.html')

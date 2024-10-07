from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('find_a_doctor_home/', views.find_a_doctor_home, name='find-a-doctor-home'),

    path('find_facility/', views.find_facility, name='find-facility'),

    path('for_professionals/', views.for_professionals, name='for-professionals'),

    path('health_blog/', views.health_blog, name='health-blog'),

    path('signup/', views.signup, name='signUp'),

    path('telehealth/', views.telehealth, name='telehealth'),

]
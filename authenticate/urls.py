from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('delete/<int:pk>', views.delete_user, name='delete'),
    path('exam/', views.do_exam, name='exam'),
    path('submitExam/', views.submit_exam, name='submit_exam'),
    path('addQuestion/', views.add_question,name='addQuestion'),
    path('feedback/', views.feedback_user, name='feedback'),
    path('feedback_layout/', views.feedback_layout, name='feedback_layout'),
    path('detail/<int:id>', views.detail_feedback, name='detail'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
]


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash ,get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages 
from django.core.paginator import Paginator
from .forms import SignUpForm, EditProfileForm,DeleteUser,FeedbackUser,addQuestionform
from .models import Feedback,Quiz
import math

# Create your views here.	from django.shortcuts import render

def listing(page_number):
    next = 0
    previous = 0
    all_users= get_user_model().objects.all()
    p = Paginator(all_users, 5)
    page = p.page(page_number)
    if  p.count % 5 == 0:page_count = int(p.count / 5)
    else : page_count = int(p.count / 5) + 2
    
    if page.number < page_count - 1: next = page.next_page_number()
    if page.number > 1: previous = page.previous_page_number()
    add_number = (page.number - 1) * 5
    
    
    return {"all_users":page.object_list,
            "page_count": range(1,page_count),
            "current_page": page.number,
            "next_page": next,
            "previous_page": previous,
            "add_number":add_number,
            }
def list_feedback(page_number):
    next = 0
    previous = 0
    # all_users= get_user_model().objects.all()
    all_post= Feedback.objects.all().order_by("-time_create").values()
    p = Paginator(all_post, 6)
    page = p.page(page_number)
    if  p.count % 5 == 0:page_count = int(p.count / 5)
    else : page_count = int(p.count / 5) + 2
    
    if page.number < page_count - 1: next = page.next_page_number()
    if page.number > 1: previous = page.previous_page_number()
    add_number = (page.number - 1) * 5
    
    
    return {"feedback":page.object_list,
            "page_count": range(1,page_count),
            "current_page": page.number,
            "next_page": next,
            "previous_page": previous,
            "add_number":add_number,
            }

def home(request): 
    page_number = request.GET.get('page')
    if page_number: context= listing(int(page_number))
    else : context= listing(1)
    return render(request, 'authenticate/home.html', context)

def feedback_layout(request): 
    page_number = request.GET.get('page')
    if page_number: context= list_feedback(int(page_number))
    else : context= list_feedback(1)
    return render(request, 'authenticate/home.html', context)

def login_user (request):
    if request.method == 'POST': #if someone fills out form , Post it 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:# if user exist
            login(request, user)
            messages.success(request,('Đăng nhập thành công'))
            return redirect('home') #routes to 'home' on successful login  
        else:
            messages.success(request,('Tài khoản hoặc mật khẩu không đúng vui lòng thử lại'))
            return redirect('login') #re routes to login page upon unsucessful login
    else:
        return render(request, 'authenticate/login.html', {})

def detail_feedback(request,id):  
    post = Feedback.objects.get(id=id)
    context = {"post":post}
    return render(request, 'authenticate/feedback.html', context)

def logout_user(request):
    logout(request)
    messages.success(request,('Đăng xuất thành công'))
    return redirect('home')

def do_exam(request):
    user = request.GET.get('current_user')
    current_user = get_user_model().objects.get(username=user[:-1])
    questions=Quiz.objects.all()
    context = {'questions':questions,'user':current_user}
    return render(request,'authenticate/exam.html',context)

def submit_exam(request):
    if request.method == 'POST':
            user = request.POST.get('current_user')
            current_user = get_user_model().objects.get(username=user)
            questions=Quiz.objects.all()
            score=0
            wrong=0
            correct=0
            total=0
            for q in questions:
                total+=1
                print(q.ans)
                print(request.POST.get(q.question))
                if q.ans ==  request.POST.get(q.question):
                    score+=10
                    correct+=1
                else:
                    wrong+=1
            percent = "{:.2f}".format(score/(total*10) *100)
            context = {
                'score':score,
                'time': request.POST.get('timer'),
                'correct':correct,
                'wrong':wrong,
                'percent':percent,
                'total':total
            }
            current_user.point = score
            current_user.status = True
            current_user.time = int(request.POST.get('timer'))
            current_user.save(update_fields=["point"])
            current_user.save(update_fields=["status"])
            current_user.save(update_fields=["time"])
            return render(request,'authenticate/result.html',context)

def delete_user(request,pk):
    if request.method == 'POST': 
        form = DeleteUser(request.POST)
        if form.is_valid():
                rem = get_user_model().objects.get(id=pk)
                if rem is not None:
                    rem.delete()
                    messages.info(request, "Người dùng đã được xóa")
                    return redirect("home")
                else:
                    messages.info(request, "Xảy ra lỗi vui lòng thử lại.")
    else:
        form = DeleteUser()
    context = {'form': form}
    return render(request, 'home.html', context)

def feedback_user(request):
    if request.method =='POST':
        form = FeedbackUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Phản hồi đã được gửi'))
            return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            messages.success(request, ('Tạo người dùng thành công'))
            return redirect('home')
    else: 
        form = SignUpForm() 

    context = {'form': form}
    return render(request, 'authenticate/register.html', context)

def add_question(request):    
    if request.user.is_staff:
        form=addQuestionform()
        if(request.method=='POST'):
            form=addQuestionform(request.POST)
            if(form.is_valid()):
                form.save()
                messages.success(request, ('Tạo câu hỏi thành công'))
                return redirect('/addQuestion') 
        else: 
            context={'form':form }
            return render(request,'authenticate/add_question.html',context)
    else: 
        return redirect('home') 

def edit_profile(request):
    if request.method =='POST':
        form = EditProfileForm(request.POST, instance= request.user)
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ('Chỉnh sửa thông tin cá nhân thành công'))
            return redirect('home')
    else: 		#passes in user information 
        form = EditProfileForm(instance= request.user) 

    context = {'form': form}
    return render(request, 'authenticate/edit_profile.html', context)
    #return render(request, 'authenticate/edit_profile.html',{})



def change_password(request):
    if request.method =='POST':
        form = PasswordChangeForm(data=request.POST, user= request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, ('Chỉnh sửa mật khẩu thành công'))
            return redirect('home')
    else: 		#passes in user information 
        form = PasswordChangeForm(user= request.user) 

    context = {'form': form}
    return render(request, 'authenticate/change_password.html', context)
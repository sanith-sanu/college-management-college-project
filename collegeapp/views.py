from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from collegeapp.models import course
from collegeapp.models import student
from collegeapp.models import teacher
import os


def index(request):
    return render(request,'index.html')
def log_in(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'WELCOME {username}')
                return redirect('teacher_home')
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,'index.html')
    else:
        return render(request,'index.html')
    


@login_required(login_url='index') 
def admin_home(request):
    if  request.user.is_staff:
        return render(request,'adminhome.html')
    else:
        return redirect('index')


@login_required(login_url='index')  
def teacher_home(request):
    
        return render(request,'teacherhome.html')
    





 
def teacher_signup(request):
    
        courses=course.objects.all()
        return render(request,'teacher_signup.html',{'cour':courses})


@login_required(login_url='index')  
def add_course(request):

     return render(request,'add_course.html')

@login_required(login_url='index')  
def addc(request):
    
        if request.method=="POST":
            course_name=request.POST['cname']
            course_fee=request.POST['cfee']
            courses=course(course_name=course_name,fee=course_fee)
            courses.save()
            return redirect('admin_home')


@login_required(login_url='index')  
def adds(request):
    
        if request.method=='POST':
            student_name=request.POST['sname']
            student_address=request.POST['saddress']
            age=request.POST['sage']
            jdate=request.POST['jdate']
            sel=request.POST['sel']
            course1=course.objects.get(id=sel)
            students=student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
            students.save()
            return redirect('admin_home')
        
        
@login_required(login_url='index')    
def add_stud(request):
    
        courses=course.objects.all()
        return render(request,'add_stud.html',{'cour':courses})
        
  
def addt(request):
    
        if request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            username = request.POST.get('uname')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')
            address = request.POST.get('address')
            age = request.POST.get('age')
            email = request.POST.get('email')
            cnumber = request.POST.get('number')
            sel = request.POST.get('sel')
            course1 = course.objects.get(id=sel)
            image = request.FILES.get('file')

            if password == cpassword:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username already exists")
                    return redirect('teacher_signup')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=fname, last_name=lname)
                    user.save()
                    user1 = teacher(address=address, age=age, number=cnumber, image=image, user=user, course=course1)
                    user1.save()
                    return render(request,'index.html')
            else:
                messages.info(request, "Password does not match")
                return redirect('teacher_signup')


@login_required(login_url='index')  
def display_teacher(request):
   
        tea=teacher.objects.all()
        return render(request,'show_teachers.html',{'pdt':tea})  


@login_required(login_url='index')         
def delete(request,pk):
   
        user=teacher.objects.get(id=pk)
        if user.image:
            user.image.delete()
        user.delete()
        user.user.delete()
        return redirect('display_teacher')


@login_required(login_url='index')  
def show(request):
   
        stud=student.objects.all()
        return render(request,'show_stud.html',{'stud':stud})


@login_required(login_url='index') 
def update_stud(request,pk):
    
        stud=student.objects.get(id=pk)
        c=course.objects.all()
        return render(request,'update_stud.html',{'stu':stud,'cou':c})


@login_required(login_url='index')  
def edit_stud(request,pk):
    
        stu=student.objects.get(id=pk)
        if request.method=='POST':
            name=request.POST['name']
            address=request.POST['address']
            age=request.POST['age']
            date=request.POST['date']
            cou=request.POST['sel']
            cour=course.objects.get(id=cou)
            stu.student_name=name
            stu.student_address=address
            stu.student_age=age
            stu.joining_date=date
            stu.course=cour
            stu.save()
            return redirect('show')


@login_required(login_url='index')  
def delete_stud(request,pk):
    
        stu=student.objects.get(id=pk)
        stu.delete()
        return redirect('show')


@login_required(login_url='index') 
def display(request):
    
        current_user=request.user.id
        user1=teacher.objects.get(user_id=current_user)
        return render(request,'profile.html',{'teacher':user1})


@login_required(login_url='index')  
def updatetea(request):
    
        current_user = request.user.id
        courses=course.objects.all()
        details = teacher.objects.get(user_id=current_user)
        user1 = teacher.objects.get(user_id=current_user)
        user2 = User.objects.get(id=current_user)

        if request.method == "POST":
            if 'file' in request.FILES:
                
                if user1.image:
                    os.remove(user1.image.path)
                user1.image = request.FILES['file']

            
            user2.first_name = request.POST.get('first_name')
            user2.last_name = request.POST.get('last_name')
            user2.username = request.POST.get('uname')
            user2.email = request.POST.get('email')  
            user2.save()

            user1.age = request.POST.get('age')
            user1.address = request.POST.get('address')
            user1.number = request.POST.get('number')
            sel=request.POST.get('sel')
            user1.course=course.objects.get(id=sel)
            user1.save()

            return redirect('display')
        return render(request, 'edit_teacher.html', {'cour': courses, 'det': details})
    

        
       

       




@login_required(login_url='index') 
def log_out(request):
    
        auth.logout(request)
        return render(request,'index.html')
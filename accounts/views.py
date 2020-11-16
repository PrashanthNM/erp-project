from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .database import create_maths,create_physics,create_english,create_computer,create_chemistry,create_maths_marks,create_physics_marks,create_english_marks,create_computer_marks,create_chemistry_marks,fetch_data

id={'Prashanth':'maths','Praveen':'physics','rakshith':'chemistry','Disha':'english','Monisha':'computer','Akhil':'student','Bhavna':'student','Chetna':'student','Dipti':'student','Greeshma':'student'}

global name
# Create your views here.


def register(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        if User.objects.filter(username=name).exists():
             messages.info(request,'Username Taken')
             return redirect('register')
        else:
            user = User.objects.create_user(username=name, password=password)
            user.save()
        return render(request,"login.html")

    else:
        return render(request,"register.html")

def login(request):
    if request.method=="POST":
        global name
        name=request.POST['name']
        password=request.POST['password']
        user=auth.authenticate(username=name,password=password)

        if user is not None: #if user id and password is same
            auth.login(request,user)

            if id[name]=='student':
                return render(request,'student.html',{'name':name})
            
            else:
                return render(request,'teacher.html',{'name':name,'subject':id[name]})

        else:
            messages.info(request,'invalid credentials')
            return render(request,"login.html")
    else:
        return render(request,'login.html')




def logout(request):
    auth.logout(request)
    return redirect('/')

def teacher(request):
    return render(request,'teacher.html')


def teacher_marks(request):
    if request.method=="POST":
        akhil_c=request.POST['akhil_c']
        akhil_a=request.POST['akhil_a']
        bhavana_c=request.POST['bhavana_c']
        bhavana_a=request.POST['bhavana_a']
        chetna_c=request.POST['chetna_c']
        chetna_a=request.POST['chetna_a']
        dipti_c=request.POST['dipti_c']
        dipti_a=request.POST['dipti_a']
        greeshma_c=request.POST['greeshma_c']
        greeshma_a=request.POST['greeshma_a']
        list_1=[akhil_c,bhavana_c,chetna_c,dipti_c,greeshma_c]
        list_2=[akhil_a,bhavana_a,chetna_a,dipti_a,greeshma_a]
        if id[name]=='maths':
            create_maths_marks(list_1,list_2)
            
        elif id[name]=='physics':
            create_physics_marks(list_1,list_2)


        elif id[name]=='chemistry':
            create_chemistry_marks(list_1,list_2)

        elif id[name]=='english':
            create_english_marks(list_1,list_2)
        
        elif id[name]=='computer':
            create_computer_marks(list_1,list_2)

        return render(request,'teacher.html',{'name':name,'subject':id[name]})
    
    else:

        return render(request,'teacher_marks.html',{'name':name,'subject':id[name]})






def teacher_update_attendence(request):
    #name=request.POST['']

        #name=request.POST['akhil_c']
    #names=['AKHIL','BHAVNA','CHETNA','DIPTI','GREESHMA']
    #usn=['1CR19CS101','1CR19CS102','1CR19CS103','1CR19CS104','1CR19CS105']
    if request.method=="POST":
        akhil_c=request.POST['akhil_c']
        akhil_a=request.POST['akhil_a']
        bhavana_c=request.POST['bhavana_c']
        bhavana_a=request.POST['bhavana_a']
        chetna_c=request.POST['chetna_c']
        chetna_a=request.POST['chetna_a']
        dipti_c=request.POST['dipti_c']
        dipti_a=request.POST['dipti_a']
        greeshma_c=request.POST['greeshma_c']
        greeshma_a=request.POST['greeshma_a']
        list_1=[akhil_c,bhavana_c,chetna_c,dipti_c,greeshma_c]
        list_2=[akhil_a,bhavana_a,chetna_a,dipti_a,greeshma_a]
        if id[name]=='maths':
            create_maths(list_1,list_2)
            
        elif id[name]=='physics':
            create_physics(list_1,list_2)


        elif id[name]=='chemistry':
            create_chemistry(list_1,list_2)

        elif id[name]=='english':
            create_english(list_1,list_2)
        
        elif id[name]=='computer':
            create_computer(list_1,list_2)

        return render(request,'teacher.html',{'name':name,'subject':id[name]})

    else:
        return render(request,'teacher_update_attendence.html',{'name':name,'subject':id[name]})

def students_marks(request):
    student_object=fetch_data()
    return render(request,'students_marks.html',{'student_object':student_object,'name':name})


def students_attendence(request):
    student_object=fetch_data()
    return render(request,'students_attendence.html',{'student_object':student_object,'name':name})
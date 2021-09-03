from django.shortcuts import render
from django.http import HttpResponse, request
from django.urls.conf import re_path
from PATH.models import *
from django.core.mail import send_mail

# Create your views here.

#Home Page
def home(request):
    a=tbl_count.objects.all()
    return render(request, 'home.html',{'a':a})


#contact view
def index(request):
    return render(request, 'index.html')



#Login for customer
def log(request):
    msg=""
    if request.method=='POST':
        username2=request.POST.get('username2')
        password2=request.POST.get('password2')
        if tbl_log.objects.filter(username2=username2,password2=password2):
            data=tbl_Reg.objects.get(username=username2,password=password2)
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,"register.html",{'msg':msg})
            elif data.status=='1':
                return render(request,"index.html",{'msg':msg})
        else:
            msg="Incorrect password or username"
            # return HttpResponse("incorrect password or username!!!")
    return render(request,"login.html",{'msg':msg})


#customer register
def Reg_fun(request):
    msg=""
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        # phone=request.POST.get('phone')
        password=request.POST.get('password')
        rpassword=request.POST.get('rpassword')
        if password==rpassword:
            if tbl_Reg.objects.filter(username=username):
                msg="Username already exist"
                return render(request,"register.html",{'msg':msg})
            else:
                if tbl_Reg.objects.filter(email=email):
                    msg="Email already exist"
                    return render(request,"register.html",{'msg':msg})
                else:
                    data=tbl_Reg.objects.create(username=username,email=email,password=password,status=1)
                    data=tbl_log.objects.create(username2=username,password2=password,status=1)
                    msg="Registration successfully done!!!!"
                    return render(request,"login.html") 
        else:
            msg="Password didn't match"
    return render(request,"register.html",{'msg':msg})


#index page view
def index(request):
    return render(request, 'index.html')


#dealer login view
def stafflog(request):
    
    msg=""
    if request.method=='POST':
        staffusername=request.POST.get('staffusername')
        staffpassword=request.POST.get('staffpassword')

        if staffRegistration.objects.filter(staffname=staffusername,staffpass=staffpassword):
            data=staffRegistration.objects.get(staffname=staffusername,staffpass=staffpassword)
            request.session['userid']=data.id
            if data.status=='staff':
                return render(request,"EmpLogin.html")
        else:
            msg="Incorrect password or username"
    return render(request, 'staffLogin.html',{'msg':msg})


#employee login view
# def employeelogin(request):
#     msg = ""
#     if request.method == "POST":
#         Empusername=request.POST.get('Empusername')
#         Emppassword = request.POST.get('Emppassword')
      
#         if EmpLogin.objects.filter(Empusername=Empusername,Emppassword=Emppassword):
#             data=EmpRegistration.objects.get(Pump=Empusername,Emppass=Emppassword)        
#             request.session['userid']=data.id
#             if data.status=='admin':
#                 return render(request,"staffLogin.html",{'msg':msg})
#             elif data.status=='1':
#                 data1 = tbl_book.objects.filter(pump=Empusername)
#                 print(data1)
#                 return render(request,"details.html",{'data': data1})
#         else:
#             msg="Incorrect username or password"
#     return render(request,"EmpLogin.html",{'msg':msg})




def employeelogin(request):
    msg = ""
    if request.method == "POST":
        Empusername=request.POST.get('Empusername')
        Emppassword = request.POST.get('Emppassword')
        if EmpLogin.objects.filter(Empusername=Empusername,Emppassword=Emppassword):
            data=EmpRegistration.objects.get(Pump=Empusername,Emppass=Emppassword)        
            request.session['userid']=data.id
            if data.status=='admin':
                return render(request,"staffLogin.html",{'msg':msg})
            elif data.status=='1':
                name = Empusername
                data1 = tbl_book.objects.filter(pump=name)
                data2 = tbl_oilbook.objects.filter(oilpump=name)
                return render(request,"details.html",{'data1':data1,'data2':data2})
        else:
            msg="Incorrect username or password"
    return render(request,"EmpLogin.html",{'msg':msg})



#details view
def details(request):
    return render(request, 'details.html')

    

#employee register view
def employeeregister(request):
    msg=""

    if request.method=='POST':
        Empname=request.POST.get('empname')
        Emppass=request.POST.get('emppassword')
        Empphone=request.POST.get('empphone')
        Empmail=request.POST.get('empemail')
        Pump=request.POST.get('pump')
        Empcpass=request.POST.get('empcpassword')

        if Emppass == Empcpass :
            if EmpRegistration.objects.filter(Empname=Empname):
                msg=Empname + "Already Exist"
                return render(request,'EmpRegister.html',{'msg':msg})
            else:
                if EmpRegistration.objects.filter(Empmail=Empmail):
                    msg =Empmail + "Already Exist"
                    return render(request,'EmpRegister.html',{'msg':msg})
                else:
                    if EmpRegistration.objects.filter(Empphone=Empphone):
                        msg = Empphone + "Already Exist"
                        return render(request,'EmpRegister.html',{'msg':msg})
                    else:
                        data = EmpRegistration.objects.create(Empname=Empname,Empmail=Empmail,Empphone=Empphone,Emppass=Emppass,Pump=Pump,status=1)
                        data = EmpLogin.objects.create(Empusername=Pump,Emppassword=Emppass,status=1)
                        msg= "Registration Succesfully Completed"
                        return render(request,'EmpLogin.html')
                        
        else:
            msg = "passowrd Mismatched"
    return render(request,'EmpRegister.html',{'msg':msg})







#booking view
def book(request): 
    categories= PumpDetail.objects.all()  
    msg=""
    if request.method == 'POST':      
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        c_address=request.POST.get('c_address')
        place=request.POST.get('place')
        phone=request.POST.get('phone')
        fuel=request.POST.get('fuel')
        quantity=request.POST.get('quantity')
        pump=request.POST.get('pump')  

        if request.method == 'POST':
            data = request.POST      

            if data['pump'] != 'none':
                pump = PumpDetail.objects.get(id=data['pump'])
            else:
                pump = None

        data=tbl_book.objects.create(fname=fname,lname=lname,address=address,c_address=c_address,place=place,phone=phone,fuel=fuel,quantity=quantity,pump=pump)
        data=PumpDetail.objects.create(Name=pump)
        msg=" successfully done!!!!"
        return render(request,"index.html", {'msg':msg}) 
     
    return render(request,"fuelBooking.html", {'categories': categories})




#contact view
def contact(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name')
        c_email = request.POST.get('c_email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'c_name':c_name,
            'c_email':c_email,
            'subject':subject,
            'message':message,
        }
        # print(data)
        message = '''
        New message :{}


        from: {}
        '''.format(data['message'],data['c_email'])
        send_mail(data['subject'],message,'',['sooryasoorya2848@gmail.com'])
        # return HttpResponse('Thank you for the message we will touch you soon')
        return render(request, 'index.html')
    return render(request, 'contact.html')



def oilchange(request):
    categories= PumpDetail.objects.all()  
    msg=""
    if request.method == 'POST':      
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        oiladdress=request.POST.get('oiladdress')
        oil_c_address=request.POST.get('oil_c_address')
        oilplace=request.POST.get('oilplace')
        oilphone=request.POST.get('oilphone')
        oil=request.POST.get('oil')
        oilquantity=request.POST.get('oilquantity')
        oilpump=request.POST.get('oilpump')  

        if request.method == 'POST':
            data = request.POST      

            if data['oilpump'] != 'none':
                oilpump = PumpDetail.objects.get(id=data['oilpump'])
            else:
                oilpump = None

        data=tbl_oilbook.objects.create(firstname=firstname,lastname=lastname,oiladdress=oiladdress,
        oil_c_address=oil_c_address,oilplace=oilplace,oilphone=oilphone,oil=oil,oilquantity=oilquantity,
        oilpump=oilpump)
        data=PumpDetail.objects.create(Name=oilpump)
        msg=" successfully done!!!!"
        return render(request,"index.html", {'msg':msg}) 
    return render(request, 'oilchangeBooking.html', {'categories': categories})




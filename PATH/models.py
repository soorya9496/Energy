from django.db import models

# Create your models here.

#customer login
class tbl_log(models.Model):
    username2=models.CharField(max_length=50)
    password2=models.CharField(max_length=50)
    status=models.CharField(max_length=10)


#customer register
class tbl_Reg(models.Model):
    username=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    status=models.CharField(max_length=10)


#Dealer login
class staffRegistration(models.Model):
    staffname=models.CharField(max_length=100,null=False,blank=False)
    staffpass=models.CharField(null=False,max_length=20)
    status=models.CharField(max_length=10)


#employee registration
class EmpRegistration(models.Model):
    Empid=models.CharField(max_length=10,default="")
    Empname=models.CharField(max_length=100,null=False,blank=False,default="")
    Empmail=models.EmailField(max_length=50,blank=False, null=False,default="")
    Empphone=models.IntegerField(null=False)
    Pump=models.CharField(max_length=100,null=False,blank=False)
    Emppass=models.CharField(null=False,max_length=20)
    status=models.CharField(max_length=10,default="")


#employee login
class EmpLogin(models.Model):
    Empusername=models.CharField(max_length=100,null=False,blank=False)
    Emppassword=models.CharField(null=False,max_length=20)
    status=models.CharField(max_length=10,default="")


#pumps
class PumpDetail(models.Model):
    Name=models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.Name


#Fuelbooking
class tbl_book(models.Model):
    fname=models.CharField(max_length=50, null=True)
    lname=models.CharField(max_length=50, null=True)
    address=models.CharField(max_length=50, null=True)
    c_address=models.CharField(max_length=50, null=True)
    place=models.CharField(max_length=50, null=True)
    phone=models.IntegerField(null=True)
    fuel=models.CharField(max_length=10, null=True)
    quantity=models.IntegerField( null=True)
    pump=models.CharField(max_length=10, null=True, blank=True)
    status=models.CharField(max_length=10)


#Oil booking
class tbl_oilbook(models.Model):
    firstname=models.CharField(max_length=50, null=True)
    lastname=models.CharField(max_length=50, null=True)
    oiladdress=models.CharField(max_length=50, null=True)
    oil_c_address=models.CharField(max_length=50, null=True)
    oilplace=models.CharField(max_length=50, null=True)
    oilphone=models.IntegerField(null=True)
    oil=models.CharField(max_length=10, null=True)
    oilquantity=models.IntegerField( null=True)
    oilpump=models.CharField(max_length=10, null=True, blank=True)
    status=models.CharField(max_length=10)


#count Section
class tbl_count(models.Model):
    petrol=models.IntegerField(null=True)
    diesel=models.IntegerField(null=True)
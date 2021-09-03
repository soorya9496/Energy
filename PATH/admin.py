from django.contrib import admin
from PATH.models import *

# Register your models here.
class tabl_logAdmin(admin.ModelAdmin):
    list_display = ('username2','password2')
class tbl_RegAdmin(admin.ModelAdmin):
    list_display = ('username','email','password')
class tabl_StaffRegAdmin(admin.ModelAdmin):
    list_display = ('staffname','staffpass')
class tabl_EmpRegAdmin(admin.ModelAdmin):
    list_display = ('Empname','Empmail','Empphone','Pump','Emppass')
class tabl_EmpLoginAdmin(admin.ModelAdmin):
    list_display = ('Empusername','Emppassword')
class tabl_BookAdmin(admin.ModelAdmin):
    list_display = ('fname','lname','address','c_address','place','phone','fuel','quantity','pump')
class tabl_OilBookAdmin(admin.ModelAdmin):
    list_display = ('firstname','lastname','oiladdress','oil_c_address','oilplace','oilphone','oil','oilquantity','oilpump')
class tabl_CountAdmin(admin.ModelAdmin):
    list_display = ('petrol','diesel')




admin.site.register(tbl_log, tabl_logAdmin)
admin.site.register(tbl_Reg, tbl_RegAdmin)
admin.site.register(staffRegistration, tabl_StaffRegAdmin)
admin.site.register(EmpRegistration, tabl_EmpRegAdmin)
admin.site.register(EmpLogin, tabl_EmpLoginAdmin)
admin.site.register(tbl_book, tabl_BookAdmin)
admin.site.register(tbl_oilbook, tabl_OilBookAdmin)
admin.site.register(tbl_count,tabl_CountAdmin)
admin.site.register(PumpDetail)
from django.contrib import admin
from .models import *
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','category','price','image']
class BillAdmin(admin.ModelAdmin):
    list_display = ['name','email','address','city','state','zip','name_on_card','cardno','expmonth','expyear']
class TableAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','guest','date_table','time_table','category','msg']
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'cpassword']
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'mailid', 'service','food','cleanliness','ResponseTime','recommend','rating']
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','city','query']
class CaterAdmin(admin.ModelAdmin):
    list_display = ['cid','name','dcategory','dcapacity','dicategory','dicapacity','tcategory','tcapacity','pcategory','pcapacity','rcategory','rcapacity','decategory','decapacity','drcategory','drcapacity','maincategory','maincapacity']
admin.site.register(item,ItemAdmin)
admin.site.register(Users,UserAdmin)
admin.site.register(storeItems)
admin.site.register(bill,BillAdmin)
admin.site.register(book_tables,TableAdmin)
admin.site.register(Catering_order_table)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Contact,ContactAdmin)
admin.site.register(orders_foods)
admin.site.register(ritems)
admin.site.register(recommendation)
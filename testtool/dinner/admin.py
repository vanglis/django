from django.contrib import admin
from .models import Dinner,TakeOrder
# Register your models here.

class DinnerAdmin(admin.ModelAdmin):
    list_display = ('foods_name','foods_type','price','add_time','update_time')

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser and request.user.username=='www':
            return [f.name for f in self.model._meta.fields]
        return self.readonly_fields

class TakeOrderAdmin(admin.ModelAdmin):
    list_display = ('foods_name', 'foods_type', 'price', 'username', 'add_time', 'update_time')
#admin.site.register([Php,Java])
admin.site.register(Dinner,DinnerAdmin)
admin.site.register(TakeOrder,TakeOrderAdmin)



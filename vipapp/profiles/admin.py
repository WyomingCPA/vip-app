from django.contrib import admin
from .models import Ticket, Order



# Register your models here
class TicketAdmin(admin.ModelAdmin):
    list_display = ('closed', 'title', 'text', 'created', 'user')
    list_filter = ['created', 'closed']
    search_fields = ['title', 'text']

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Order)



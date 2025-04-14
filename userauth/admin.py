# admin.py
from django.contrib import admin
from .models import Profile, Ticket

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_admin')
    search_fields = ('user__username',)

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'title', 'assigned_to', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('title', 'description', 'ticket_number')
    readonly_fields = ('ticket_number',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Ticket, TicketAdmin)

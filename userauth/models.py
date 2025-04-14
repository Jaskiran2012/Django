# userauth/models.py
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)  # Flag for admin or not
    # userauth/models.py

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)
    has_onboarded = models.BooleanField(default=False)  # 👈 NEW FIELD

    def __str__(self):
        return self.user.username


    

class Ticket(models.Model):
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('on_hold', 'On Hold'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tickets')
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tickets', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    
    def save(self, *args, **kwargs):
        # Generate ticket number if not already assigned
        if not self.ticket_number:
            last_ticket = Ticket.objects.order_by('-id').first()
            if last_ticket:
                ticket_id = last_ticket.id + 1
            else:
                ticket_id = 1
            self.ticket_number = f"TK-{ticket_id:04d}"
        super(Ticket, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.ticket_number}: {self.title}"
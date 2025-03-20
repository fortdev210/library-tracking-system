from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone

from celery import shared_task

from .models import Loan

@shared_task
def send_loan_notification(loan_id):
    try:
        loan = Loan.objects.get(id=loan_id)
        member_email = loan.member.user.email
        book_title = loan.book.title
        send_mail(
            subject='Book Loaned Successfully',
            message=f'Hello {loan.member.user.username},\n\nYou have successfully loaned "{book_title}".\nPlease return it by the due date.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[member_email],
            fail_silently=False,
        )
    except Loan.DoesNotExist:
        pass

@shared_task
def check_overdue_loans():
    overdue_loans = Loan.objects.filter(due_date__lt=timezone.now().date(), is_returned=False)
    
    for loan in overdue_loans:
        member_email = loan.member.user.email  
        book_title = loan.book.title
        due_date = loan.due_date.strftime("%Y-%m-%d")
        
        send_mail(
            subject="Overdue Library Book Reminder",
            message=f"Your book '{book_title}' was due on {due_date}. Please return it as soon as possible.",
            from_email="library@domain.com",
            recipient_list=[member_email],
            fail_silently=True,
        )  
    return f"{len(overdue_loans)} reminders sent"
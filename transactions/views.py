from django.shortcuts import render, redirect
from .models import Transaction
from members.models import Member
from books.models import Book
from decimal import Decimal
from django.utils import timezone
import datetime
from django.utils.timezone import timedelta

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def issue_book(request):
    if request.method == 'POST':
        member_id = request.POST.get('member_id')
        book_id = request.POST.get('book_id')
        member = Member.objects.get(id=member_id)
        book = Book.objects.get(id=book_id)

        # Check if the member has an outstanding debt of more than Rs. 500
        if member.outstanding_debt > Decimal('500'):
            return redirect('transaction_list')  # Redirect to transaction list with a message

        # Create a transaction to issue the book
        transaction = Transaction(member=member, book=book)
        transaction.save()

    return redirect('transaction_list')

def return_book(request):
    if request.method == 'POST':
        transaction_id = request.POST.get('transaction_id')
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.return_date = timezone.now()

        # Calculate rent fee if applicable and update outstanding debt
        if transaction.return_date > transaction.issue_date + timedelta(days=7):
            rent_fee = Decimal('10.00')  # Adjust the rent fee as needed
            transaction.rent_fee = rent_fee
            transaction.member.outstanding_debt += rent_fee
            transaction.member.save()

        transaction.save()

    return redirect('transaction_list')

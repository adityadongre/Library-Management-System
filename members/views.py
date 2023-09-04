from django.shortcuts import render, redirect
from .models import Member
from .forms import MemberForm

def member_list(request):
    members = Member.objects.all()
    return render(request, 'members/member_list.html', {'members': members})

def add_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    
    return render(request, 'members/add_member.html', {'form': form})

def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    return render(request, 'members/member_detail.html', {'member': member})

def member_views(request):

    return render(request, 'members/member_views.html')

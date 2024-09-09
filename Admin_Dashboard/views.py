import email
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib import messages
from . models import Department
import pdb;
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from validate_email import validate_email
import threading
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
import datetime
from Employee_Dashboard.models import Tasks

class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send(fail_silently=False)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def DashboardView(request):
    if request.method=="GET":
        emp = User.objects.filter(is_staff=False, is_active=True)
        return render (request, 'Admin_Dashboard/Dashboard_Base.html', {'emp':emp})
    if request.method=='POST':
        employee = request.POST['employee']
        employee=str(employee)
        request.session['employee'] = employee
        maxdate = datetime.datetime.now()
        maxdate = str(maxdate)
        maxdate = maxdate[:10]
        return render (request, 'Admin_Dashboard/Employee_Data.html',{'maxdate':maxdate})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def ViewEmployeesTasksView(request):
    if request.method=="GET":
        return redirect('nDashboard')
    if request.method=='POST':
        employee = request.POST['employee']
        employee=str(employee)
        request.session['employee'] = employee
        maxdate = datetime.datetime.now()
        maxdate = str(maxdate)
        maxdate = maxdate[:10]
        return render (request, 'Admin_Dashboard/Employee_Data.html',{'maxdate':maxdate})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def AdminProfileView(request):
    if request.method=="GET":
        return render (request, 'Admin_Dashboard/Profile.html')
    else:
        return render (request, 'Admin_Dashboard/Profile.html')




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def AddEmployeeView(request):
    obj = Department.objects.filter(owner=request.user)
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        number = request.POST['number'] 
        department = request.POST['department'] 
        date = request.POST['date'] 
        password = request.POST['password'] 
        if not name or not email or not number or not department or not date or not password:
            messages.error(request, 'You must fill all the fields to add an employee!')
            return render (request, 'Admin_Dashboard/AddEmployee.html', {'obj':obj})
        user = User.objects.create_user( first_name= request.user.username, username=name, email=email, id=int(str(number)), last_name=department, date_joined=date )
        user.set_password(password)
        user.is_active = True
        user.save()
        current_site = get_current_site(request)
        email_subject = 'Welcome to our company!'
        email = EmailMessage(
            email_subject,
            'Hi, '+user.username + ', we\'re glad that you\'ve joined our company. Below are your credentials to log in to our website. \n'+
            '\nUsername: '+name+
            '\nEmail: '+email+
            '\nPassword: '+password+
            '\nYour date of joining as registered with us is '+date+
            '\nHere\'s the link to our company\'s website: '+'https://'+current_site.domain,
            'noreply@semycolon.com',
            [email],
        )
        EmailThread(email).start()
        messages.success(request, 'Employee added successfully!')
        return redirect('nadd-employee')
    if request.method=="GET":
        
        return render (request, 'Admin_Dashboard/AddEmployee.html', {'obj':obj})





@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def AddDepartmentView(request):
    
    if request.method =="POST":
        department = request.POST['department']
        if Department.objects.filter(owner = request.user, dept=department).exists():
            messages.error(request, 'The department \''+department+'\' already exists!')
            return redirect('nadd-department')
        Department.objects.create(owner = request.user, dept=department)
        messages.success(request, 'New department added successfully!')
        return redirect('nadd-department')
    else:
        obj = Department.objects.filter(owner = request.user)
        return render (request, 'Admin_Dashboard/AddDepartment.html',{'obj':obj})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def DeleteDepartmentView(request):
    if request.method=="POST":
        dept = request.POST['dept']
        obj = Department.objects.get(owner = request.user, dept=dept)
        obj.delete()
        messages.success(request, 'Department deleted successfully!!')
        return redirect('nadd-department')
    else:
        messages.error(request, 'You tried accessing a prohibited page')
        return redirect('nDashboard')




def ValidateEmployeeUsernameView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        username = data['username']
        if not str(username).isalnum():
            return JsonResponse({'username_error': 'Username should only contain alphanumeric characters!'})
        exists = User.objects.filter(username=username).exists()
        if exists:
            return JsonResponse({'username_error': 'Sorry! This username is in use, choose another one!'})
        return JsonResponse({'username_valid': True})
    else:
        messages.error(request, 'You are accessing a prohibited page!!')
        return redirect('nDashboard')


def ValidateEmployeeEmailView(request):
    if request.method == "POST":
        data = json.loads(request.body)
        email = data['email']
        if not validate_email(email):
            return JsonResponse({'email_error': 'Email is invalid'})
        if User.objects.filter(email=email).exists():
            return JsonResponse({'email_error': 'Sorry, this email is in use, choose another one!'})
        return JsonResponse({'email_valid': True})
    else:
        messages.error(request, 'You tried accessing a prohibited page!!')
        return redirect('nDashboard')











def AdminGetTodayTasksView(request):
    employee = request.session['employee']
    user = User.objects.get(first_name= request.user.username, username=employee)
    today = datetime.date.today()
    today = str(today)
    Ttasks = Tasks.objects.filter(owner=user, StartDate=today)
    Tfinalrep = {}
    def Tget_type(Ttasks):
        return Ttasks.Type
    Ttask_list = list(set(map(Tget_type, Ttasks)))
    def Tget_type_time(Type):
        Ttime=0
        Tfiltered_by_type = Ttasks.filter(Type=Type)
        for item in Tfiltered_by_type:
            Ttime += item.TimeTaken
        return Ttime

    for x in Ttasks:
        for y in Ttask_list:
            Tfinalrep[y] = Tget_type_time(y)
    return JsonResponse({'Ttype_time_data': Tfinalrep}, safe=False)


def AdminGetYestTasksView(request):
    employee = request.session['employee']
    user = User.objects.get(first_name= request.user.username, username=employee)
    yesterday = (datetime.date.today() - datetime.timedelta(1)).strftime('%Y-%m-%d')    
    Ytasks = Tasks.objects.filter(owner=user, StartDate=yesterday)
    Yfinalrep = {}
    def Yget_type(Ytasks):
        return Ytasks.Type
    Ytask_list = list(set(map(Yget_type, Ytasks)))
    def Yget_type_time(YType):
        Ytime=0
        Yfiltered_by_type = Ytasks.filter(Type=YType)
        for item in Yfiltered_by_type:
            Ytime += item.TimeTaken
        return Ytime

    for x in Ytasks:
        for y in Ytask_list:
            Yfinalrep[y] = Yget_type_time(y)
    return JsonResponse({'Ytype_time_data': Yfinalrep}, safe=False)






def AdminGetWeeklyTasksView(request):
    employee = request.session['employee']
    user = User.objects.get(first_name= request.user.username, username=employee)
    today = datetime.datetime.now()
    monday = str(today - datetime.timedelta(today.weekday()))[:10]
    tuesday = str(today - datetime.timedelta(today.weekday()-1))[:10]
    wednesday = str(today - datetime.timedelta(today.weekday()-2))[:10]
    thursday = str(today - datetime.timedelta(today.weekday()-3))[:10]
    friday = str(today - datetime.timedelta(today.weekday()-4))[:10]
    saturday = str(today - datetime.timedelta(today.weekday()-5))[:10]
    sunday = str(today + datetime.timedelta(7-today.weekday()-1))[:10]
    Wtasks = Tasks.objects.filter(owner=user)
    Wfinalrep = {}
    def Wget_type(Wtasks):
        return Wtasks.Type
    Wtask_list = list(set(map(Wget_type, Wtasks)))
    monbreakc=0
    monworkc=0
    monmeetc=0
    monbreak = Tasks.objects.filter(owner=user, StartDate=monday,Type='Break')
    monwork = Tasks.objects.filter(owner=user, StartDate=monday,Type='Work')
    monmeet = Tasks.objects.filter(owner=user, StartDate=monday,Type='Meeting')
    for i in monbreak:
        monbreakc = monbreakc+i.TimeTaken
    for i in monwork:
        monworkc = monworkc+i.TimeTaken
    for i in monmeet:
        monmeetc=monmeetc+i.TimeTaken
    tuebreakc=0
    tueworkc=0
    tuemeetc=0
    tuebreak = Tasks.objects.filter(owner=user, StartDate=tuesday,Type='Break')
    tuework = Tasks.objects.filter(owner=user, StartDate=tuesday,Type='Work')
    tuemeet = Tasks.objects.filter(owner=user, StartDate=tuesday,Type='Meeting')
    for i in tuebreak:
        tuebreakc = tuebreakc+i.TimeTaken
    for i in tuework:
        tueworkc = tueworkc+i.TimeTaken
    for i in tuemeet:
        tuemeetc=tuemeetc+i.TimeTaken
    wedbreakc=0
    wedworkc=0
    wedmeetc=0
    wedbreak = Tasks.objects.filter(owner=user, StartDate=wednesday,Type='Break')
    wedwork = Tasks.objects.filter(owner=user, StartDate=wednesday,Type='Work')
    wedmeet = Tasks.objects.filter(owner=user, StartDate=wednesday,Type='Meeting')
    for i in wedbreak:
        wedbreakc = wedbreakc+i.TimeTaken
    for i in wedwork:
        wedworkc = wedworkc+i.TimeTaken
    for i in wedmeet:
        wedmeetc=wedmeetc+i.TimeTaken
    thubreakc=0
    thuworkc=0
    thumeetc=0
    thubreak = Tasks.objects.filter(owner=user, StartDate=thursday,Type='Break')
    thuwork = Tasks.objects.filter(owner=user, StartDate=thursday,Type='Work')
    thumeet = Tasks.objects.filter(owner=user, StartDate=thursday,Type='Meeting')
    for i in thubreak:
        thubreakc = thubreakc+i.TimeTaken
    for i in thuwork:
        thuworkc = thuworkc+i.TimeTaken
    for i in thumeet:
        thumeetc=thumeetc+i.TimeTaken
    fribreakc=0
    friworkc=0
    frimeetc=0
    fribreak = Tasks.objects.filter(owner=user, StartDate=friday,Type='Break')
    friwork = Tasks.objects.filter(owner=user, StartDate=friday,Type='Work')
    frimeet = Tasks.objects.filter(owner=user, StartDate=friday,Type='Meeting')
    for i in fribreak:
        fribreakc = fribreakc+i.TimeTaken
    for i in friwork:
        friworkc = friworkc+i.TimeTaken
    for i in frimeet:
        frimeetc=frimeetc+i.TimeTaken
    satbreakc=0
    satworkc=0
    satmeetc=0
    satbreak = Tasks.objects.filter(owner=user, StartDate=saturday,Type='Break')
    satwork = Tasks.objects.filter(owner=user, StartDate=saturday,Type='Work')
    satmeet = Tasks.objects.filter(owner=user, StartDate=saturday,Type='Meeting')
    for i in satbreak:
        satbreakc = satbreakc+i.TimeTaken
    for i in satwork:
        satworkc = satworkc+i.TimeTaken
    for i in satmeet:
        satmeetc=satmeetc+i.TimeTaken
    sunbreakc=0
    sunworkc=0
    sunmeetc=0
    sunbreak = Tasks.objects.filter(owner=user, StartDate=sunday,Type='Break')
    sunwork = Tasks.objects.filter(owner=user, StartDate=sunday,Type='Work')
    sunmeet = Tasks.objects.filter(owner=user, StartDate=sunday,Type='Meeting')
    for i in sunbreak:
        sunbreakc = sunbreakc+i.TimeTaken
    for i in sunwork:
        sunworkc = sunworkc+i.TimeTaken
    for i in sunmeet:
        sunmeetc=sunmeetc+i.TimeTaken
    MONDAY = {'monbreakc':monbreakc,'monworkc': monworkc,'monmeetc':monmeetc}
    TUESDAY = {'tuebreakc': tuebreakc,'tueworkc':tueworkc,'tuemeetc':tuemeetc}
    WEDNESDAY = {'wedbreakc':wedbreakc,'wedworkc':wedworkc,'wedmeetc':wedmeetc}
    THURSDAY = {'thubreakc':thubreakc,'thuworkc':thuworkc,'thumeetc':thumeetc}
    FRIDAY = {'fribreakc':fribreakc,'friworkc':friworkc,'frimeetc':frimeetc}
    SATURDAY = {'satbreakc':satbreakc,'satworkc':satworkc,'satmeetc':satmeetc}
    SUNDAY = {'sunbreakc':sunbreakc,'sunworkc':sunworkc,'sunmeetc':sunmeetc}
    return JsonResponse({'MONDAY': MONDAY, 'TUESDAY':TUESDAY,'WEDNESDAY':WEDNESDAY,'THURSDAY':THURSDAY,'FRIDAY':FRIDAY,'SATURDAY':SATURDAY,'SUNDAY':SUNDAY}, safe=False)



def AdminDateFilterView(request):
    date = request.session['date']
    employee = request.session['employee']
    user = User.objects.get(first_name= request.user.username, username=employee)
    Ftasks = Tasks.objects.filter(owner=user, StartDate=date)
    Ffinalrep = {}
    def Fget_type(Ftasks):
        return Ftasks.Type
    Ftask_list = list(set(map(Fget_type, Ftasks)))
    def Fget_type_time(FType):
        Ftime=0
        Ffiltered_by_type = Ftasks.filter(Type=FType)
        for item in Ffiltered_by_type:
            Ftime += item.TimeTaken
        return Ftime

    for x in Ftasks:
        for y in Ftask_list:
            Ffinalrep[y] = Fget_type_time(y)
    return JsonResponse({'Ftype_time_data': Ffinalrep}, safe=False)
    


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def CallAdminDateFilterView(request):
    date = request.POST['date']
    request.session['date'] = date
    employee = request.session['employee']
    return render (request, 'Admin_Dashboard/Employee_Filter.html',{'employee':employee,'maxdate':date})
        


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def DeactivateView(request):
    emp = User.objects.filter(first_name= request.user.username, is_staff=False, is_active=True)
    if request.method=="GET":
        return render (request, 'Admin_Dashboard/Deactivate.html',{'emp':emp})
    else:
        employee= request.POST['employee']
        user = User.objects.get(first_name= request.user.username, username=employee)
        user.delete()
        messages.success(request, employee+' has been deactivated successfully')
        return render (request, 'Admin_Dashboard/Deactivate.html',{'emp':emp})




@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='/authentication/login')
def SearchEmployeeView(request):
    if request.method == 'POST':
        search_str = json.loads(request.body).get('searchText')
        users = User.objects.filter(username__istartswith=search_str) |  User.objects.filter(
            username__icontains=search_str) | User.objects.filter(last_name__istartswith=search_str) |  User.objects.filter(
            last_name__icontains=search_str) | User.objects.filter(email__istartswith=search_str) |  User.objects.filter(
            email__icontains=search_str)
        data = users.values()
        return JsonResponse(list(data), safe=False)

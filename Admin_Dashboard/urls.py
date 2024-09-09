from django.views.decorators.csrf import csrf_exempt
from django.urls import path
from . import views
urlpatterns = [
    path('Dashboard', views.DashboardView, name='nDashboard'),
    path('add-employee', views.AddEmployeeView, name='nadd-employee'),
    path('add-department', views.AddDepartmentView, name='nadd-department'),
    path('delete-department', views.DeleteDepartmentView, name='ndelete-department'),
    path('validate-employee-username', csrf_exempt(views.ValidateEmployeeUsernameView), name='nvalidate-employee-username'),
    path('validate-employee-email', csrf_exempt(views.ValidateEmployeeEmailView), name='nvalidate-employee-email'),
    path('Admin-Profile', views.AdminProfileView, name='nAdminProfile' ),
    path('view_employee_tasks', views.ViewEmployeesTasksView, name='view_employee_tasks'),
    path('Aget_today_tasks', views.AdminGetTodayTasksView, name='Aget_today_tasks'),
    path('Aget_yest_tasks', views.AdminGetYestTasksView, name='Aget_yest_tasks'),
    path('Aget_weekly_tasks', views.AdminGetWeeklyTasksView, name='Aget_weekly_tasks'),
    path('Adate-filter', views.AdminDateFilterView, name='Adate-filter'),
    path('call-Adate-filter', views.CallAdminDateFilterView, name='call-Adate-filter'),
    path('deactivate_employee', views.DeactivateView, name='deactivate_employee'),
    path('search_employee', csrf_exempt(views.SearchEmployeeView), name='search_employee'),
    
    
]

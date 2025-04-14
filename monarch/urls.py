from django.contrib import admin
from django.urls import path
from magic import views
from django.conf import settings
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.map_view, name='map_view'),
    path('get_tahsils/<int:district_id>/', views.get_tahsils, name='get_tahsils'),
    path('get_villages/<int:tahsil_id>/', views.get_villages, name='get_villages'),
    path('get_project/<int:village_id>/', views.get_project, name='get_project'),
    path('get_project_by_id/<int:project_id>/', views.get_project_by_id, name='get_project_by_id'),

     path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('base/', views.base, name='base'),

]
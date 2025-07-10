from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='report'),
    path('', views.home, name='home'),
    path('report/', views.report, name='report_get'),
    path('records/', views.Records, name='records'),
    path('delete/<id>/', views.delete_record, name='delete'),
    path('edit/<id>/', views.edit_record, name='edit'),
    path('pdfreport/<id>/', views.report_pdf, name='pdfreport'),
    path('about/', views.about, name='about'),

]

from django.urls import path
from . import views

urlpatterns = [
    # path('madhav_technicals/', views.madhav_technicals, name='madhav_technicals'),
    # path('madhav_technicals/Gallery.html/',views.Gallary,name='Gallary'),
    # path('madhav_technicals/Service.html/',views.Service,name='Services'),
    # path('madhav_technicals/Contact.html/',views.Contactt,name='Contactt'),
    # path('madhav_technicals/Contact_List.html/',views.Contact_Listt,name='Contact_Listt'),

    path('madhav_technicals', views.madhav_technicals, name='madhav_technicals'),
    path('Gallery',views.Gallary,name='Gallary'),
    path('Service',views.Service,name='Service'),
    path('Contactt',views.Contactt,name='Contactt'),
    path('Contact_Listt',views.Contact_Listt,name='Contact_Listt'),
    path('delete/<int:record_id>/', views.delete_record, name='delete_record'),
    path('About',views.About,name='About'),
    
    path('send_email/', views.send_email, name='send_email'),
]

  

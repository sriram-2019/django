from django.urls import path
from django.urls import include
from dcollege import urls
from dcollege import views
urlpatterns = [
    path('',views.index,name="index"),
    path('sucess/',views.student_signs,name="new"),
    path('staffsuccess/',views.staff,name="new"),
    path('my_view/',views.index2,name="my_view"),
    path('Button.html/',views.index3,name='Button.html'),
    path('upload/',views.photo1,name='upload'),
    path('d/',views.gets,name='d'),
    path('Button.html/ll.html/', views.display_data, name='Button/ll'),
    path('getfile/', views.get_file, name='getfile'),
    path('all_files/', views.all_file, name='all_files'),
]

from django.urls import path
from.import views
urlpatterns = [

    path('',views.showform),
    path('showprofile/',views.showprofile),
    path('edit/<int:id>/',views.edit),
    path('delete<int:id>',views.delete)
    
]
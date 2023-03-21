from django.urls import path 
from .views import home, conversation 
 
urlpatterns = [ 
    path('', home, name='home'), 
    path('conversation/<int:user_id>/', conversation, name='conversation'), 
] 
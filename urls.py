from django.urls import path
from accounting.views import Get_db_results,Send_Email

urlpatterns = [
    path('getdbresults/', Get_db_results, name='Items'),
    path('sendemail/',Send_Email,name='Email-sender')
]

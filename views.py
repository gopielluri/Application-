from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import smtplib

@csrf_exempt
def Get_db_results(request):
    if request.method == 'GET':
        try:
            query = request.GET.get('query')
            print(query)
            results = []
            with connection.cursor() as cursor:
                cursor.execute(query)
                while True:
                    items = cursor.fetchall()
                    columns = [col[0] for col in cursor.description]
                    items_as_dicts = [
                        {column_name: row[i] for i, column_name in enumerate(columns)}
                        for row in items
                    ]
                    results.append(items_as_dicts)
                    if not cursor.nextset():
                        break
            return JsonResponse(results, safe=False)
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            query = data.get('query')
            print(query)
            with connection.cursor() as cursor:
                cursor.execute(query)
                if(cursor.description):
                    columns = [col[0] for col in cursor.description]
                    items = cursor.fetchall()
                    results = [
                        {column_name: row[i] for i, column_name in enumerate(columns)}
                        for row in items
                    ]
                else:
                    results=[]
            print(results)
            return JsonResponse({'success': True, 'message': 'Data updated successfully','results':results})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def Send_Email(request):
    senderEmail="shankarseshamsetti@gmail.com"
    mail="ushak547@gmail.com"
    recieverEmail="aashritha636@gmail.com"
    subject="Test Mail"
    message="Test Message1 from python"
    text=f"Subject: {subject}\n\n{message}"
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login(senderEmail,"Iasgowrishankar@55")
    server.sendmail(mail,recieverEmail,text)
    print("Email sent successfully")
    return JsonResponse({})
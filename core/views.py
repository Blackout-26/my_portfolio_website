import json
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

# Create your views here.

# 1. Serve your React Portfolio
def home(request):
    return render(request, 'index.html')

# 2. Handle the Contact Form
@csrf_exempt
def contact_api(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            
            # Extract data
            name = data.get('name', 'Anonymous')
            email = data.get('email', 'No email provided')
            message = data.get('message', 'No message')

            # Send Email
            send_mail(
                subject=f"Portfolio Contact from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER], # Sends to yourself
                fail_silently=False,
            )

            return JsonResponse({'success': True})
        except Exception as e:
            print(e)
            return JsonResponse({'success': False}, status=500)
            
    return JsonResponse({'error': 'Invalid method'}, status=405)
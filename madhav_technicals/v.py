# from django.conf import settings 
# from django.core.mail import send_mail
# from django.http import HttpResponse
# # from .models import YourModel  # Import your model for the contact information
# from madhav_technicals.models import Contact
# from django.template.loader import render_to_string


# def send_email(request):
#     # Assuming you have a model named 'YourModel' for storing contact information
#     custs = YourModel.objects.all()

#     subject = 'Contact Information'
#     from_email = {} # Sender's email address
#     recipient_list = ['rachitsaini009005@gmail.com']  # Receiver's email address

#     # Render your email content using a Django template
#     email_content = render_to_string('Contact_List.html', {'custs': custs})
    
#     # Use send_mail to send the email
#     send_mail(subject, '', from_email, recipient_list, html_message=email_content)

#     return HttpResponse('Email sent successfully.')




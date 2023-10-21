from django.shortcuts import render
from django.template import loader
from madhav_technicals.models import Contact



# Create your views here.

from django.http import HttpResponse

def madhav_technicals(request):
    # return render(request,'index.html')
 template = loader.get_template('index.html')
 return HttpResponse(template.render())
 
def Gallary(request):
 template = loader.get_template('Gallary.html')
 return HttpResponse(template.render())

def Service(request):
 template= loader.get_template('Service.html')
 return HttpResponse(template.render())

# def Contact_Listt(request):
#   return render(request,'Contact_List.html')

def Contactt(request):
 if request.method == "POST":
    print(request.method,'yes')
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    Email_Id = request.POST['Email_Id']
    subject = request.POST['subject']
    Message = request.POST['Message']

    # if firstname and lastname and Email_Id and subject and Message:
    contact = Contact(firstname=firstname,lastname=lastname,Email_Id=Email_Id,subject=subject,Message=Message)
    print('done')
    contact.save()
    return HttpResponse("Employee added Successfully")
    # CUST_data = Contact(firstname=firstname,lastname=lastname,Email_Id = Email_Id,subject=subject,Message = Message)
    
    # CUST_data.save()


    #  return render(request,'Contact_List.html',{'firstname':firstname,'lastname':lastname,' Email_Id': Email_Id,'subject':subject,'Message':Message})
    # else:
    #   print("not done")
    #   return HttpResponse("Enter all the details")

 elif request.method =="GET":
    
    print(request.method,'no')
    return render(request,'Contact.html')
    
 else:
   return HttpResponse("An Exception is occured")

    # return render(request,'Contact.html')
    # return HttpResponse("Request Added Successfully")
 
 
from django.shortcuts import render
from madhav_technicals.models import Contact  # Assuming your model is named 'Contact'

def Contact_Listt(request):
    custs = Contact.objects.all()
    return render(request, 'Contact_List.html', {'custs': custs})

# views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from madhav_technicals.models import Contact 

def delete_record(request, record_id):
    contact = get_object_or_404(Contact, id=record_id)
    contact.delete()

    # Generate the URL for 'Contact_Listt'
    url = reverse('Contact_Listt')
    
    return redirect(url)  # Redirect to the generated URL

def About(request):
 template = loader.get_template('About.html')
 return HttpResponse(template.render())


from django.conf import settings 
from django.core.mail import send_mail
from django.http import HttpResponse
# from .models import YourModel  # Import your model for the contact information
from madhav_technicals.models import Contact
from django.template.loader import render_to_string


def send_email(request):
    # Assuming you have a model named 'YourModel' for storing contact information
    custs = YourModel.objects.all()

    subject = 'Contact Information'
    from_email = 'rachitsaini0905@gmail.com'  # Sender's email address
    recipient_list = ['rachitsaini009005@gmail.com']  # Receiver's email address

    # Render your email content using a Django template
    email_content = render_to_string('Contact_List.html', {'custs': custs})
    
    # Use send_mail to send the email
    send_mail(subject, '', from_email, recipient_list, html_message=email_content)

    return HttpResponse('Email sent successfully.')




from django.shortcuts import render, redirect
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .forms import ContactForm

# Create your views here.
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            content = form.cleaned_data['content']
            
            html = render_to_string('emails/contactform.html',{
                'name':name,
                'email': email,
                'content': content,
                'phone' : phone
                
            })
            
            print('the form was valid')
            send_mail('문의사항이 도착했습니다.','This is the message','yyw0209@hanmail.net',['cs3@familyexp.com'],html_message=html)
            
            return redirect('index')
    else:
        form = ContactForm()
                
    return render(request, 'index.html',{
        'form':form
    })

def privacy(request):
    return render(request, 'privacy.html')
   
# def send_email(request):
#     if request.method == "POST":
#         subject = request.POST.get('name')
#         message = request.POST.get('message')
#         from_email='yyw0209@hanmail.net'
#         to = ["cs3@familyexp.com"]
#         email = EmailMessage(
#             subject, # subject
#             message, # message
#             from_email=from_email, #from email
#             to=to, #To email
#         )
#         email.send()
#         return redirect('privacy')
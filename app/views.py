
from django.shortcuts import render
# my import
from django.template import loader
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.http import HttpResponseRedirect
# home

def index(request):
 return render(request, 'index.html')

# function to send data to email
def send_mail(request):
 name = request.POST.get('name')
 email = request.POST.get('email')
 courses = request.POST.get('courses')
 template = loader.get_template('contact_form.txt')
 context = {
  'name': name,
  'email': email,
  'courses': courses,
 }
 message = template.render(context)
 email = EmailMultiAlternatives(
  "Mastery Courses",message,
  "congratulation"+"- A gift to you",
  ['mastery3303@gmail.com', email]
 )
 #convert the html and css inside [contact_form] to html template
 email.content_subtype = 'html'
 email.send()
 messages.success(request, 'we sent a link to you email!')
 return HttpResponseRedirect('/')
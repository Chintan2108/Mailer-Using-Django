from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm


def email(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['chintanmaniyar@gmail.com', 'htalreja16@gmail.com', 'harsh@kickstartsolutions.in'], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Mail could not be sent!')
            return redirect('success')
    return render(request, "email.html", {'form': form})


def success(request):
    return HttpResponse('Response Submitted! Thank you for your feedback.')

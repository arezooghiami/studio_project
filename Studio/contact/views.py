from django.shortcuts import render,redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def contact(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.success(request, 'پیام شما با موفقیت فرستاده شد')
            return redirect('home:photo_list')
    else:
        contact_form =ContactForm()

    return render(request,'contact/contact.html',{'contact_form':contact_form})
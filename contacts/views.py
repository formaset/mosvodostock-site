from django.shortcuts import render

def contacts_view(request):
    from .models import ContactsPage
    contacts = ContactsPage.objects.live().first()
    return render(request, 'contacts/contacts.html', {'contacts': contacts})
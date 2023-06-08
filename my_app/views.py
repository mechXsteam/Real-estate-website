from django.shortcuts import render

from contacts.models import Contact
from listings.choices import price_choices, bedroom_choices, state_choices
from listings.models import Listing
from realtors.models import Realtor


# Create your views here.

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {'listings': listings,
               'state_choices': state_choices,
               'bedroom_choices': bedroom_choices,
               'price_choices': price_choices,
               'title': 'BRS Real Estate'
               }
    return render(request, 'index.html', context)


def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    # Get MVP
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
        'title': 'BT Real Estate | About'
    }
    return render(request, 'about.html', context)


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)

    context = {
        'contacts': user_contacts,
        'title': 'BRS Real Estate | Dashboard'
    }
    return render(request, 'dashboard.html', context)

from django.shortcuts import render, redirect

from .models import community_event_manager, Contributor
from .forms import RegistrationForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    community_event_manager = community_event_manager.objects.all()
    return render(request, 'community_event_manager/index.html', {
        #'show_community_event_manager': False,
        # 'show_community_event_manager': True,
        'community_event_manager': community_event_manager
    })
#   return HttpResponse('Hello django!')

def community_event_managers_details(request, community_event_managers_slug):
    # print(community_event_managers_slug)
    try:
      selected_community_event_manager = community_event_manager.objects.get(slug=community_event_managers_slug)
      if request.method == 'GET':
        # selected_community_event_manager = community_event_manager.objects.get(slug=community_event_managers_slug)
        registration_form = RegistrationForm()
        # return render(request, 'community_event_manager/community_event_managers-details.html', {
        # 'community_event_manager_found': True,
        # 'community_event_manager': selected_community_event_manager,
        # 'form': registration_form
        #  'form': registration_form
        # 'community_event_manager_title': selected_community_event_manager['title'],
        # Using dot notation in this method
        # 'community_event_manager_title': selected_community_event_manager.title,
        # 'community_event_manager_description': selected_community_event_manager['description']
        # 'community_event_manager_description': selected_community_event_manager.description
    #    })
      else:
        registration_form = RegistrationForm(request.POST)
        if registration_form.is_valid():
         # contributor = registration_form.save()
           user_email = registration_form.cleaned_data['email_address']
           user_phone = registration_form.cleaned_data['phone_number']
           contributor,_ = Contributor.objects.get_or_create(email_address=user_email, phone_number=user_phone)
           selected_community_event_manager.contributor.add(contributor)
           return redirect('registration_complete', community_event_managers_slug=community_event_managers_slug)


      return render(request, 'community_event_manager/community_event_managers-details.html', {
            'community_event_manager_found': True,
            'community_event_manager': selected_community_event_manager,
            'form': registration_form
        })

    except Exception as exc:
        print(exc)
        return render(request, 'community_event_manager/community_event_managers-details.html', {
            'community_event_manager_found': False
        })

def registration_complete(request, community_event_managers_slug):
  community_event_manager = community_event_manager.objects.get(slug=community_event_managers_slug)
  return render(request, 'community_event_manager/registration-complete.html', {
        'supervisor_email': community_event_manager.supervisor_email
    })
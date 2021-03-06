""" Platzigram middleare catalog. """

# Django

from django.shortcuts import redirect 
from django.urls import reverse

class ProfileCompletionMiddleare:
    """Profile completion middleware.

    Ensure every user is interacting with the platform 
    have their picture and biograpy
    """

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')] and not request.path.startswith('/admin/'):
                        return redirect('users:update_profile')

        # Code to be executed for each request/response after
        # the view is called.
        response = self.get_response(request)
        return response
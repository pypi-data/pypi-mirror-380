# django_hx/decorators.py

from functools import wraps

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


def hx_login_required():
    """
    An extension of Django's @login_required decorator for HTMX requests.

    Applies the standard @login_required behavior (using settings.LOGIN_URL). For HTMX requests (detected via 'HX-Request' header),
    adds an 'HX-Refresh: true' header to the redirect response to trigger a full page refresh to the login page.
    """

    def decorator(view_func):
        # Apply the standard login_required decorator (uses settings.LOGIN_URL by default)
        standard_wrapped = login_required()(view_func)

        @wraps(standard_wrapped)
        def final_wrapped(request, *args, **kwargs):
            response = standard_wrapped(request, *args, **kwargs)
            # If it's a redirect (unauthenticated) and an HTMX request, add the refresh header
            if isinstance(response, HttpResponseRedirect) and request.headers.get(
                "HX-Request"
            ):
                response["HX-Refresh"] = "true"
            return response

        return final_wrapped

    return decorator

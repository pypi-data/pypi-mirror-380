# django_hx/utils.py

from django.shortcuts import render


def hx_render(request, template_name, context=None):
    """
    An enhanced render function for HTMX requests.

    If the request is an HTMX call (HX-Request header present):
    - Renders the specified partial/fragment from the template (e.g., "myapp/mypage.html#content").

    If the request is a standard (non-HTMX) call:
    - Renders the full template, stripping any fragment identifier (#partial) if present.

    Args:
        request: The Django request object.
        template_name: The template name, optionally with a fragment (e.g., "myapp/mypage.html#content").
        context: The context dictionary for the template (default: None).

    Returns:
        HttpResponse: The rendered response.
    """
    context = context or {}

    is_htmx = request.headers.get('HX-Reques')
    full_template_name = template_name.split('#')[0]  # Strip fragment for full render

    if is_htmx:
        # Render the partial using django-template-partials syntax
        response = render(request, template_name, context)
    else:
        # Render the full template
        response = render(request, full_template_name, context)

    return response

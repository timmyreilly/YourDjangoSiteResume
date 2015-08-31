"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Microsoft Code Challege',
            'year':datetime.now().year,
        })
    )
    
def additional_resources(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/additional_resources.html',
        context_instance = RequestContext(request,
        {
            'title':'Additional resources',
            'year':datetime.now().year,
        })
    )


# -*- coding: utf-8 -*-
import sys

from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

from .models import Document
from .forms import DocumentForm
    
def list(request):
    try:
        # Handle file upload
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                newdoc = Document(docfile=request.FILES['docfile'], origin=request.FILES['docfile'])
                newdoc.save()
                
                return HttpResponseRedirect(reverse('list'))
        else:
            form = DocumentForm()  # A empty, unbound form

        # Load documents for the list page
        documents = Document.objects.all()
        print(documents)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        # raise

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

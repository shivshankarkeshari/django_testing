# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Products

# Create your views here.


@login_required
def pdt_dtls(request, pk):
    product = get_object_or_404(Products, pk=pk)
    return render(request, 'pdt_dtl.html', {'product': product})
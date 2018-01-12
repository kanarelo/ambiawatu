from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import render_to_response, redirect, render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json

def index(request):
    return render_to_response("index.html", {
        
    })
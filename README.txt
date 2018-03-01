from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.utils.timezone import now
from rest_framework import serializers
from django.conf.urls import url
from .views import *
from django.conf.urls import url, include
from django.contrib import admin




superuser:
    password: iuytrewq
    name: root
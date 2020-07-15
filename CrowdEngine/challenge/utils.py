from django.shortcuts import render, redirect
from .models import *


class ObjectDetailMixin:
    model = None
    template = None



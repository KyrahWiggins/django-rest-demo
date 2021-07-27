# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Lead
from .serializers import LeadSerializer
from rest_framework import generics


class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

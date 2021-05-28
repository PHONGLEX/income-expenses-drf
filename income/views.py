from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .serializers import IncomeSerializer
from .models import Income
from .permissions import IsOwner


class IncomeList(ListCreateAPIView):
    serializer_class = IncomeSerializer
    queryset = Income.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


class IncomeDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = IncomeSerializer
    lookup_field = "id"
    queryset = Income.objects.all()
    permissions = (permissions.IsAuthenticated, IsOwner)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)


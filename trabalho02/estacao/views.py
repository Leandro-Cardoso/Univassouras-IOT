from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from datetime import datetime

from .models import Data

class DataListView(ListView):
    model = Data
    template_name = 'estacao/data_list.html'
    context_object_name = 'estacao'

    def get_queryset(self):
        start_date_str = self.request.GET.get('start_date')
        end_date_str = self.request.GET.get('end_date')
        queryset = super().get_queryset().order_by('-created_at')

        if start_date_str:
            try:
                start_date_naive = datetime.strptime(start_date_str, '%Y-%m-%d')
                start_date = timezone.make_aware(start_date_naive)
                queryset = queryset.filter(created_at__gte=start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date_naive = datetime.strptime(end_date_str, '%Y-%m-%d')
                end_date = timezone.make_aware(end_date_naive)
                one_day_later = end_date + timezone.timedelta(days=1)
                queryset = queryset.filter(created_at__lt=one_day_later)
            except ValueError:
                pass
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['start_date'] = self.request.GET.get('start_date', '')
        context['end_date'] = self.request.GET.get('end_date', '')
        return context

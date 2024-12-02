from django.views.generic import ListView

from django.shortcuts import render

from apps.reports.models import Report


class ReportListView(ListView):
    model = Report
    template_name = 'pages/reports.html'

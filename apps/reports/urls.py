from django.urls import path

from apps.reports.views import ReportListView

app_name = 'reports'
urlpatterns = [
    path('', ReportListView.as_view(), name='report_list'),
]

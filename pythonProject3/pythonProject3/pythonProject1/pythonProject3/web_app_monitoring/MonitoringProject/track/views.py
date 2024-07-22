from django.shortcuts import render
from .models import UrlRequest, WebAppStatusLog


def status_list(request):
    status_logs = WebAppStatusLog.objects.all()
    return render(request, 'monitoring/status_list.html', {'status_logs': status_logs})

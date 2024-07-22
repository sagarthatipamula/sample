from django.db import models

class UrlRequest(models.Model):
    env_choices = (
        ("PROD", "PROD"),
        ("DEV", "DEV"),
    )
    name = models.CharField(max_length=200, default='')
    email = models.CharField(max_length=200, default='')
    app_name = models.CharField(max_length=200, default='')
    url = models.CharField(max_length=200, default='')
    environment = models.CharField(max_length=200, choices=env_choices, default='')

    def __str__(self):
        return self.app_name

class WebAppStatusLog(models.Model):
    url_request = models.ForeignKey(UrlRequest, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    last_checked = models.DateTimeField()

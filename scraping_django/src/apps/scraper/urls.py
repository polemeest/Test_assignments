"""
URL configuration for main roots:
    "": shows main API gate for monitoring scraped data.
    "request": makes scraping requests with given keywords.
"""

from django.urls import path


urlpatterns = [
    path("", name="show_data"),
    path("request", name="make_request"),
]

from django.urls import path
from .views import company_comparison, company_list

urlpatterns = [
    path("", company_list, name="company-list"),
    path("comparison/", company_comparison, name="company-comparison"),
]

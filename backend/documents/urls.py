from django.urls import path
from .views import parsed_documents, upload_document

urlpatterns = [
    path("upload/", upload_document, name="document-upload"),
    path("parsed/", parsed_documents, name="document-parsed"),
]

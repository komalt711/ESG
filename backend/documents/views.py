from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["POST"])
def upload_document(request):
    return Response(
        {
            "message": "Document upload endpoint ready",
            "next_step": "Connect file parser / OCR pipeline",
        }
    )


@api_view(["GET"])
def parsed_documents(request):
    return Response(
        [
            {"title": "Apex Sustainability Report 2025", "status": "parsed"},
            {"title": "Nordic Governance Policy", "status": "queued"},
        ]
    )

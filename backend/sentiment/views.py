from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def news_feed(request):
    return Response(
        [
            {"label": "positive", "headline": "Renewable investment in German industrials up 18%"},
            {"label": "neutral", "headline": "Updated CSRD disclosure templates released"},
            {"label": "negative", "headline": "Governance controversy flagged for Apex Energy"},
        ]
    )

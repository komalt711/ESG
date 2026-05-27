from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def dashboard_summary(request):
    return Response(
        {
            "portfolio_esg_score": 84.2,
            "regulatory_readiness": 91,
            "high_risk_companies": 11,
            "ai_recommendations_today": 26,
        }
    )


@api_view(["GET"])
def score_trend(request):
    return Response(
        {
            "labels": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
            "values": [71, 73, 74, 78, 81, 84],
        }
    )

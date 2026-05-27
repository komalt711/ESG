from rest_framework.decorators import api_view
from rest_framework.response import Response
from esg_core.mongo import get_mongo_db


@api_view(["GET"])
def company_list(request):
    try:
        db = get_mongo_db()
        documents = list(
            db.companies.find({}, {"_id": 0, "ticker": 1, "name": 1, "score": 1, "risk_level": 1}).limit(20)
        )
        if documents:
            return Response(documents)
    except Exception:
        pass

    return Response(
        [
            {"ticker": "DBGS", "name": "DB Green Steel", "score": 87, "risk_level": "low"},
            {"ticker": "APXE", "name": "Apex Energy", "score": 69, "risk_level": "high"},
        ]
    )


@api_view(["GET"])
def company_comparison(request):
    return Response(
        {
            "labels": [
                "DB Green Steel",
                "Nordic Infra",
                "Urban Logistics",
                "Apex Energy",
                "Riviera Retail",
            ],
            "current_scores": [87, 81, 76, 69, 73],
            "target_scores": [90, 85, 80, 78, 79],
        }
    )

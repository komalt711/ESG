from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def recommendations(request):
    return Response(
        [
            {
                "priority": "high",
                "title": "Increase transition finance exposure",
                "impact": "Reduce carbon intensity by 14%",
            },
            {
                "priority": "medium",
                "title": "Governance review for board diversity",
                "impact": "Improve governance score by 7 points",
            },
        ]
    )

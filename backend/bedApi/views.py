from django.http import JsonResponse
from rest_framework.decorators import api_view


# Get beds
@api_view(['GET'])
def beds(request):
    return JsonResponse(
        {
            "beds": [
                "1",
                "2",
                "3",
                "4",
            ]
        }
    )


# Get bed details
@api_view(['GET'])
def bed_detail(request, bed_id):
    return JsonResponse({"id": bed_id, "name": "Westerberg", "type": "strawberry", "longitude": 52.0, "latitude": 8.05})

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
            ]
        }
    )


# Get bed details
@api_view(['GET'])
def bed_detail(request, bed_id):
    beds = [
        {
            "id":1,
            "name":"Westerberg",
            "culture":"strawberry",
            "longitude":52.28264,
            "latitude":8.0278
        },
        {
            "id":2,
            "name":"Wüste",
            "culture":"tomatoe",
            "longitude":52.26564,
            "latitude":8.0298
        },
        {
            "id":3,
            "name":"Hellern",
            "culture":"lettuce",
            "longitude":52.25564,
            "latitude":7.99
        }
        ]
    return JsonResponse(beds[bed_id])

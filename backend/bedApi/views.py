from django.http import JsonResponse
from django.shortcuts import render

# getter
def beds(request):
    if request.method == 'GET':
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

## ToDo change IMPORT
import string
import sys

import grpc
from django.http import JsonResponse
from google.protobuf import empty_pb2
from google.protobuf.json_format import MessageToDict
from rest_framework.decorators import api_view
from django.core import serializers
from bedApi.models import Bed, Geolocation, Geometrie

from .serializers import BedSerializer

# there is definitly a better way to add an import path
sys.path.append(r'../backend/bedApi/build/grpc/')
import meta_operations_service_pb2_grpc as metaOperations
import project_query_pb2 as projectQuerry

# from build.grpc import meta_operations_service_pb2_grpc as metaOperations
# from build.grpc import project_query_pb2 as projectQuerry
## ToDo change IMPORT

SERVER_URL = "seerep.naturerobots.de:5000"
channel = grpc.insecure_channel(SERVER_URL)
stub = metaOperations.MetaOperationsStub(channel)

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
        {"id": 1, "name": "Westerberg", "culture": "strawberry", "latitude": 52.28264, "longitude": 8.0278},
        {"id": 2, "name": "Wüste", "culture": "tomatoe", "latitude": 52.26564, "longitude": 8.0298},
        {"id": 3, "name": "Hellern", "culture": "lettuce", "latitude": 52.25564, "longitude": 7.99},
    ]
    return JsonResponse(beds[bed_id])


"""@api_view(['GET'])
def beds_grpc(request):
    response = stub.GetProjects(empty_pb2.Empty())
    project_list = MessageToDict(response).get("projects")
    bed_list = []
    for bed in project_list:
        serializer = BedSerializer(data=bed)
        if serializer.is_valid():
            bed_list.append(bed)

    return JsonResponse({"projects": bed_list})"""

# Get grpc beds
@api_view(['GET'])
def beds_grpc(request):
    response = stub.GetProjects(empty_pb2.Empty())    
    
    #save
    """projects = MessageToDict(response)['projects']
    for bed_info in projects:
        bed_info_obj = BedInfo(**bed_info)
        if(bed_info_obj):
            print("save:", bed_info_obj)"""


    #get from db
    data = []
    fields = ('uuid', 'name')
    beds = Bed.objects.all()
    if beds:
        serializer = BedSerializer(beds, many=True, fields= fields)
        if serializer.data:
            data = serializer.data
    return JsonResponse({"beds": data})


# Get grpc bed details
@api_view(['GET'])
def bed_detail_grpc(request, bed_id):
    querry = projectQuerry.ProjectQuery()
    querry.projectuuid = bed_id
    response = stub.GetProjectDetails(querry)
    
    #save
    bed_detail = MessageToDict(response)
    saveBeds(bed_detail)

    #get from db
    data = {}
    bed = Bed.objects.get(uuid=bed_id)
    if bed:
        serializer = BedSerializer(bed, many=False)
        if serializer.data:
            data = serializer.data
    return JsonResponse({"bed": data})


def saveBeds(bed_detail):

    if "info" in bed_detail:
        bed_info = bed_detail['info']
        if "geolocation" in bed_detail:
            bed_geolocation = Geolocation(**bed_detail['geolocation'])
            if bed_geolocation:
                bed_geolocation.save()
                bed = Bed(uuid=bed_info['uuid'],name=bed_info['name'],geolocation=bed_geolocation)
                if bed:
                    bed.save()
                    if "geometries" in bed_detail:
                        bed_geometries = bed_detail['geometries']
                        for bed_geometrie in bed_geometries:
                            bed_geometrie = Geometrie(bed=bed,**bed_geometrie)
                            if bed_geometrie:
                                bed_geometrie.save()
        else:
            bed = Bed(uuid=bed_info['uuid'],name=bed_info['name'])
            if bed:
                bed.save()
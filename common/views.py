from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class IndexView(APIView):
    def get(self, request):
        return render(request, "common/index.html", {"name": "Mosh"})


@api_view(["GET"])
def hello_world(request):
    return Response({"message": "API is running"})

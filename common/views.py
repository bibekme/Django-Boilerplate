from rest_framework.response import Response
from rest_framework.views import APIView


class HelloWorldView(APIView):
    def get(self, request):
        return Response(
            {"detail": "Hello rest of the world from the world of Django. "}
        )

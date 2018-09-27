from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import AirlineSerializer


class AirlineView(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def post(self, request, format=None):
        serializer = AirlineSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)

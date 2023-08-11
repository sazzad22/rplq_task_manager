from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Assignments
from .serializers import AssignmentSerializer

# Create your views here.
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def assignments(request, pk=None):
    if request.method == 'GET':
        if pk is None:
            assignments = Assignments.objects.all()
            serializer = AssignmentSerializer(assignments, many=True)
            return Response(serializer.data)
        else:
            try:
                assignment = Assignments.objects.get(pk=pk)
                serializer = AssignmentSerializer(assignment)
                return Response(serializer.data)
            except Assignments.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

    elif request.method == 'POST':
        serializer = AssignmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        try:
            assignment = Assignments.objects.get(pk=pk)
        except Assignments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = AssignmentSerializer(assignment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        try:
            assignment = Assignments.objects.get(pk=pk)
        except Assignments.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        assignment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
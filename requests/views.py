from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from requests.models import Request
from requests.serializers import RequestSerializer
from django.core.mail import send_mail
from django.conf import settings
import ipdb
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class RequestViews(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Request.objects.all()
    serializer_class = RequestSerializer(many=True)

    def perform_create(self, serializer):
        # ipdb.set_trace()
        return serializer.save(
            product=self.request.data.get("product"),
            user=self.request.user,
        )

    # def create(self, request, *args, **kwargs):
    #     return Response(status=status.HTTP_201_CREATED)

# class RequestDetailViews(RetrieveUpdateDestroyAPIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]

#     queryset = Request.objects.all()
#     serializer_class = RequestSerializer

#     def perform_update(self, serializer):
#         send_mail(
#             subject="",
#             message="",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[""],
#             fail_silently=False,
#         )

#         return super().perform_update(serializer)

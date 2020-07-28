import string, random
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions, status

from users.models import CustomUser
from users.serializers import EmailSerializer, CustomUserSerializers


class EmailValidView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        length = 10
        letters = string.ascii_letters
        confirmation_code = ''.join(random.choice(letters) for i in range(length))
        email = request.data.get('email')
        if (email is not None) and (
                CustomUser.objects.filter(email=email).count() != 1):
            CustomUser.objects.create(email=email,
                                      confirmation_code=confirmation_code, username=email)
            send_mail(
                'Тема письма',
                f'Ваш код подтверждения {confirmation_code}.',
                'api_yamdb@mail.com',  # Это поле "От кого"
                [f'{email}'],  # Это поле "Кому" (можно указать список адресов)
                fail_silently=False,  # Сообщать об ошибках
            )
            serializer = EmailSerializer(CustomUser.objects.get(email=email))
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class JwtGetView(APIView):
    permission_classes = [AllowAny]

    def post(self):
        email = self.request.data.get('email')
        confirmation_code = self.request.data.get('confirmation_code')

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        try:
            usr = CustomUser.objects.get(email=email, confirmation_code=confirmation_code)
        except ObjectDoesNotExist:
            return Response('Пары email - код подтверждения не существует', status=status.HTTP_400_BAD_REQUEST)

        if usr:
            payload = jwt_payload_handler(usr)
            token = jwt_encode_handler(payload)
            user_details = {}
            user_details['token'] = token
            return Response(user_details, status=status.HTTP_200_OK)


class PatchUserView(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializers
    permission_classes = (permissions.IsAdminUser,)
    lookup_field = "username"

    def update(self, *args, **kwargs):
        try:
            usr = CustomUser.objects.get(username=self.kwargs.get('username'))
        except ObjectDoesNotExist:
            return Response(f'Пользователя не существует', status=status.HTTP_400_BAD_REQUEST)

        serializer = CustomUserSerializers(usr, data=self.request.data, partial = True)
        if self.request.user.username == usr.username:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(f'Пользователя не существует', status=status.HTTP_400_BAD_REQUEST)







from django.core.mail import send_mail
import string, random
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework_jwt.settings import api_settings
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from users.models import CustomUser
from users.serializers import EmailSerializer

# @api_view(('POST',))
# def email_valid(request, **kwargs):
#     length = 10
#     letters = string.ascii_letters
#     confirmation_code = ''.join(random.choice(letters) for i in range(length))
#     email = request.data.get('email')
#     if (email is not None) and (
#             CustomUser.objects.filter(email=email).count() != 1):
#         CustomUser.objects.create(email=email,
#                                   confirmation_code=confirmation_code, username=email)
#         send_mail(
#             'Тема письма',
#             f'Ваш код подтверждения {confirmation_code}.',
#             'api_yamdb@mail.com',  # Это поле "От кого"
#             [f'{email}'],  # Это поле "Кому" (можно указать список адресов)
#             fail_silently=False,  # Сообщать об ошибках
#         )
#         serializer = EmailSerializer(CustomUser.objects.get(email=email))
#         return Response(serializer.data)
#     return Response(status=status.HTTP_400_BAD_REQUEST)

class EmailvalidView(APIView):
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


@api_view(('POST',))
def jwt_get(request, **kwargs):
    email = request.data.get('email')
    confirmation_code = request.data.get('confirmation_code')

    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    usr = CustomUser.objects.filter(email=email, confirmation_code=confirmation_code)

    if usr.count() == 1:
        payload = jwt_payload_handler(usr)
        token = jwt_encode_handler(payload)
        usr.token = token
        serializer = CustomUserSerializer(usr)
        return (serializer.data)




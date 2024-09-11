from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import Subscription
from .serializers import SubscriptionSerializer
import json
from django.http import JsonResponse
from accounts.serializers import ProUserSerializer
from accounts.models import ProUser
from datetime import datetime, timedelta
from rest_framework import status

class SubscriptionListView(APIView):
    def get(self, request):
        subscriptions = [
            {
                "title": "Monthly Subscription",
                "price": 100000,
                "subscription_type": 1
            },
            {
                "title": "Quarterly Subscription",
                "price": 270000,
                "subscription_type": 3
            },
            {
                "title": "Semi-Annual Subscription",
                "price": 500000,
                "subscription_type": 6
            }
        ]
        return Response(subscriptions)

class SubscriptionRquest(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            phone_number = data['phone_number']
            subscription_type = data['subscription_type']
            
            if subscription_type == 1:
                price = 100000
                title = 'Monthly Subscription'
            elif subscription_type == 3:
                price = 270000
                title = 'Quarterly Subscription'
            elif subscription_type == 6:
                price = 500000
                title = 'Semi-Annual Subscription'
            else:
                return Response({'error': 'Invalid subscription type'}, status=400)

            request_dict = {
                "title": title,
                "price": price,
                "subscription_type": subscription_type,
                "phone_number": phone_number
            }

            return JsonResponse(request_dict, status=201)

        except json.JSONDecodeError:
            return Response({'error': 'Invalid JSON'}, status=400)
        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=400)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
# ورودی: {"phone_number": "09123456789", "subscription_type": 1}
#خروجی: {"title": "Monthly Subscription", "price": 100000, "subscription_type": 1, "phone_number": "09123456789"}

class CreateProUser(CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('is_paid') == True:
            try:
                subscription_data = {
                    "title": data['title'],
                    "price": data['price'],
                    "subscription_type": data['subscription_type']
                }
                subscription_serializer = SubscriptionSerializer(data=subscription_data)
                if subscription_serializer.is_valid():
                    subscription = subscription_serializer.save()

                    start_date = datetime.now()
                    end_date = start_date + timedelta(days=data['subscription_type'] * 30)

                    pro_user_data = {
                        "user_name": data['user_name'],
                        "subscription": subscription.id,
                        "is_pro": True,
                        "end": end_date
                    }
                    pro_user_serializer = ProUserSerializer(data=pro_user_data)
                    if pro_user_serializer.is_valid():
                        pro_user_serializer.save()
                        return Response(pro_user_serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(pro_user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(subscription_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except KeyError as e:
                return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Payment required'}, status=status.HTTP_400_BAD_REQUEST)
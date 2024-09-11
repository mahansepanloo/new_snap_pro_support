from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import Subscription, SubscriptionRestaurant
from .serializers import SubscriptionSerializer, ProRestaurantsubSerializer
from django.http import JsonResponse
from accounts.serializers import ProUserSerializer, ProRestaurantSerializer
from accounts.models import ProUser
from datetime import datetime, timedelta
from rest_framework import status

class SubscriptionListView(APIView):
    def get(self, request):
        subscriptions = [
            {"title": "Monthly Subscription", "price": 100000, "subscription_type": 1},
            {"title": "Quarterly Subscription", "price": 270000, "subscription_type": 3},
            {"title": "Semi-Annual Subscription", "price": 500000, "subscription_type": 6},
        ]
        return Response(subscriptions)

class SubscriptionRequest(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            phone_number = data['phone_number']
            subscription_type = data['subscription_type']

            subscription_map = {
                1: ("Monthly Subscription", 100000),
                3: ("Quarterly Subscription", 270000),
                6: ("Semi-Annual Subscription", 500000)
            }
            
            if subscription_type not in subscription_map:
                return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)

            title, price = subscription_map[subscription_type]
            request_dict = {
                "title": title,
                "price": price,
                "subscription_type": subscription_type,
                "phone_number": phone_number
            }

            return JsonResponse(request_dict, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class CreateProUser(CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('is_paid'):
            try:
                subscription_serializer = SubscriptionSerializer(data=data)
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

class SubscriptionListViewRestu(APIView):
    def get(self, request):
        subscriptions = [
            {"title": "Annual Subscription", "price": 13000000, "subscription_type": 12},
            {"title": "Quarterly Subscription", "price": 5000000, "subscription_type": 3},
            {"title": "Semi-Annual Subscription", "price": 9000000, "subscription_type": 6},
        ]
        return Response(subscriptions)

class SubscriptionRequestRestaurant(APIView):
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            name_restaurant = data['name_restaurant']
            subscription_type = data['subscription_type']

            subscription_map = {
                12: ("Annual Subscription", 13000000),
                3: ("Quarterly Subscription", 5000000),
                6: ("Semi-Annual Subscription", 9000000)
            }
            
            if subscription_type not in subscription_map:
                return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)

            title, price = subscription_map[subscription_type]
            request_dict = {
                "title": title,
                "price": price,
                "subscription_type": subscription_type,
                "restaurant": name_restaurant  
            }

            return JsonResponse(request_dict, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CreateProRestaurant(CreateAPIView):
    serializer_class = ProRestaurantSerializer
    queryset = SubscriptionRestaurant.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if data.get('is_paid'):
            try:
                subscription_data = {
                    "title": data.get('title'),
                    "price": data.get('price'),
                    "subscription_type": data.get('subscription_type')
                }
                subscription_serializer = ProRestaurantsubSerializer(data=subscription_data)
                
                if subscription_serializer.is_valid():
                    subscription = subscription_serializer.save()

                    start_date = datetime.now()
                    end_date = start_date + timedelta(days=data['subscription_type'] * 30)

                    pro_restaurant_data = {
                        "name": data.get('restaurant_name'),
                        "subscription": subscription.id,
                        "is_pro": True,
                        "start": start_date,
                        "end": end_date
                    }
                    pro_restaurant_serializer = ProRestaurantSerializer(data=pro_restaurant_data)
                    
                    if pro_restaurant_serializer.is_valid():
                        pro_restaurant_serializer.save()
                        return Response(pro_restaurant_serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response(pro_restaurant_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response(subscription_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            except KeyError as e:
                return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Payment required'}, status=status.HTTP_400_BAD_REQUEST)
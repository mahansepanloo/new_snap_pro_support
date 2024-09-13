from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from .models import Subscription, SubscriptionRestaurant
from .serializers import SubscriptionSerializer, ProRestaurantsubSerializer
from django.http import JsonResponse
from accounts.serializers import ProUserSerializer, ProRestaurantSerializer
from accounts.models import ProUser, ProRestaurant
from datetime import datetime, timedelta
from rest_framework import status
import requests    
from django.utils import timezone
from snap_pro_project.settings import env

class SubscriptionListView(APIView):
    def get(self, request):
        subscriptions = [
            {"title": "Monthly Subscription", "price": 100000, "subscription_type": 1},
            {"title": "Quarterly Subscription", "price": 270000, "subscription_type": 3},
            {"title": "Semi-Annual Subscription", "price": 500000, "subscription_type": 6},
        ]
        return Response(subscriptions)

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
            phone_number = data.get('phone_number')
            subscription_type = data.get('subscription_type')

            if not phone_number:
                return Response({'error': 'Phone number is required'}, status=status.HTTP_400_BAD_REQUEST)

            subscription_map = {
                1: ("Monthly Subscription", 100000),
                3: ("Quarterly Subscription", 270000),
                6: ("Semi-Annual Subscription", 500000)
            }
            
            if subscription_type not in subscription_map:
                return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)

            _, price = subscription_map[subscription_type]
            
            if not ProUser.objects.filter(phone_number=phone_number).exists():
                ProUser.objects.create(
                    phone_number=phone_number,
                    is_pro=False,
                    subscription_type=subscription_type,
                )

            request_dict = {
                "price": price,
                "phone_number": phone_number
            }

            response = requests.post("https://45.139.10.8:8004/getfactor",headers= env('key')
                                     ,data=request_dict)

          
            return JsonResponse(request_dict, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.RequestException as e:
            return Response({'error': 'External request failed', 'details': str(e)}, status=status.HTTP_502_BAD_GATEWAY)
        except Exception as e:
            return Response({'error': 'Internal server error', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdateProUser(APIView):
    serializer_class = ProUserSerializer
    query_set = ProUser.objects.all()
    def post(self, request, *args, **kwargs):
        data = request.data
        if request.headers.get('api_keys') ==  env('key'):
            if data.get('is_paid')==True:
                try:
                    current_user = ProUser.objects.get(phone_number=data['name'])
                    subscription_type = current_user.subscription_type
                    current_user.is_pro = True
                    current_user.start = timezone.now()
                    current_user.end = current_user.start + timedelta(days=subscription_type * 30)


                    if subscription_type == 1:
                        sub_id = 1
                    elif subscription_type == 3:
                        sub_id = 2
                    elif subscription_type == 6:
                        sub_id = 3
                    else:
                        return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)
                    Subscription_cur = Subscription.objects.get(id=sub_id)
                    current_user.subscription = Subscription_cur
                    current_user.save()

                    pro_user_data = {
                        "phone_number": data['name'],
                        "is_pro": True,
                        "end": current_user.end,
                        "start": current_user.start,

                    }

                    # response = requests.post("YOUR_URL_HERE", data=pro_user_data)

                    return Response({'message': 'User upgraded to Pro successfully'}, status=status.HTTP_200_OK)

                except ProUser.DoesNotExist:
                    return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

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
            restaurant_name = data['restaurant_name']
            subscription_type = data['subscription_type']

            subscription_map = {
                12: ("Annual Subscription", 13000000),
                3: ("Quarterly Subscription", 5000000),
                6: ("Semi-Annual Subscription", 9000000)
            }
            
            if subscription_type not in subscription_map:
                return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)

            _ , price = subscription_map[subscription_type]

            if not ProRestaurant.objects.filter(restaurant_name = restaurant_name).exists():
                ProRestaurant.objects.create(
                    restaurant_name = restaurant_name ,
                    is_pro=False,
                    subscription_type = subscription_type,
                )

            request_dict = {
                "price": price,
                "restaurant": restaurant_name 
            }
            response = requests.post("https://45.139.10.8:8004/getfactor",headers= env('key')
                                     ,data=request_dict)
            return JsonResponse(request_dict, status=status.HTTP_201_CREATED)

        except KeyError as e:
            return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class UpdateProRestaurant(APIView):
    serializer_class = ProRestaurantSerializer
    queryset = ProRestaurant.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data
        if request.headers.get('api_keys') == env('key'):
            if data.get('is_paid')==True:         
                try:
                    current_restaurant = ProRestaurant.objects.get(restaurant_name=data['name'])
                    current_restaurant.is_pro = True
                    current_restaurant.start = datetime.now()
                    subscription_type = current_restaurant.subscription_type
                    current_restaurant.end = datetime.now() + timedelta(days=subscription_type * 30)
                    if subscription_type == 3:
                        sub_id = 1
                    elif subscription_type == 6:
                        sub_id = 2
                    elif subscription_type == 12:
                        sub_id = 3
                    else:
                        return Response({'error': 'Invalid subscription type'}, status=status.HTTP_400_BAD_REQUEST)
                    Subscription_cur = SubscriptionRestaurant.objects.get(id=sub_id)
                    current_restaurant.subscription = Subscription_cur
                    current_restaurant.save()

                    pro_restaurant_data = {
                        "restaurant_name": current_restaurant.restaurant_name,
                        "start": current_restaurant.start,
                        "end": current_restaurant.end
                    }

                    # response = requests.post("YOUR_URL_HERE", data=pro_restaurant_data)

                    return Response({'message': 'Restaurant upgraded to Pro successfully'}, status=status.HTTP_200_OK)
                
                except ProRestaurant.DoesNotExist:
                    return Response({'error': 'Restaurant not found'}, status=status.HTTP_404_NOT_FOUND)
                
                except KeyError as e:
                    return Response({'error': f'Missing field: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
                
                except requests.exceptions.RequestException as e:
                    return Response({'error': f'Error in external request: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)
                
                except Exception as e:
                    return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
            else:
                return Response({'error': 'Payment required'}, status=status.HTTP_400_BAD_REQUEST)
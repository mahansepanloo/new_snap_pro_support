from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from .models import Subscription, SubscriptionRestaurant
from .serializers import SubscriptionSerializer, ProRestaurantsubSerializer
from django.http import JsonResponse
from accounts.serializers import ProUserSerializer, ProRestaurantSerializer
from accounts.models import ProUser, ProRestaurant
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
            user_sub =Subscription.objects.create(
                title=title,
                price=price,
                subscription_type=subscription_type
            )
            ProUser.objects.create(
                phone_number=phone_number,
                subscription=user_sub.id ,
                is_pro=False,
                end=datetime.now() + timedelta(days=subscription_type * 30)
            )
            request_dict = {
                "price": price,
                "phone_number": phone_number
            }
            request.post("******", json =  request_dict)
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
                current_user = ProUser.objects.get(phone_number=data['phone_number'])
                current_user.is_pro = True
                current_user.save()  

                start_date = datetime.now()
                end_date = start_date + timedelta(days=data['subscription_type'] * 30)
                
                pro_user_data = {
                    "phone_number": data['phone_number'],
                    "is_pro": True,
                    "end": end_date
                }


                # response = requests.post("YOUR_URL_HERE", json=pro_user_data)
                
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
            current_sub = SubscriptionRestaurant.objects.create(
                title=title,
                price=price,
                subscription_type=subscription_type
            )
            ProRestaurantSerializer.objects.create(
                subscription=current_sub.id,
                restaurant=name_restaurant,
            )
            request_dict = {
                "price": price,
                "restaurant": name_restaurant  
            }
            request.post("******", json =  request_dict)

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
                current_restaurant = ProRestaurant.objects.get(restaurant=data['name'])
                current_restaurant.is_pro = True
                current_restaurant.start = datetime.now()
                current_restaurant.end = datetime.now() + timedelta(days=data['subscription_type'] * 30)
                current_restaurant.save()

                pro_restaurant_data = {
                    "name": data.get('name'),
                    "start": current_restaurant.start.isoformat(),
                    "end": current_restaurant.end.isoformat()
                }

                # Ensure you have an appropriate URL
                response = requests.post("YOUR_URL_HERE", json=pro_restaurant_data)
                response.raise_for_status()  # Check if the request was successful
                
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
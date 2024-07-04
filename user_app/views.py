from django.shortcuts import render
from .models import Friend
from django.contrib.auth.models import User
from .serializers import UserSerializer, FriendSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST', ])
def usersData(request):
    ResponseData = None
    try:
        if request.method == 'GET':
            userData = User.objects.filter(is_active=True)
            serializer = UserSerializer(userData, many=True)
            ResponseData = {'status':status.HTTP_200_OK, 'data':serializer.data}

        elif request.method == 'POST':
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                user.set_password(request.data['password'])
                user.save()
                ResponseData = {'status':status.HTTP_201_CREATED, 'data':serializer.data}
            else:
                ResponseData = {'status':status.HTTP_400_BAD_REQUEST, 'data':serializer.errors}
        return Response(ResponseData)
    except Exception as e:
        ResponseData = {'status':status.HTTP_500_INTERNAL_SERVER_ERROR, 'data':str(e)}
    return Response(ResponseData)



@api_view(['PUT','DELETE'])
def updateUser(request, id):
    ResponseData = None
    try:
        if request.method == 'PUT':
            try:
                userData = User.objects.get(id=id)
                serializer = UserSerializer(userData, data=request.data)
                if serializer.is_valid():
                    user = serializer.save()
                    if not request.data.get('password'):
                        pass
                    else:
                        user.set_password(request.data['password'])
                        user.save()
                    ResponseData = {'status':status.HTTP_200_OK, 'data':serializer.data}
                else:
                    ResponseData = {'status':status.HTTP_400_BAD_REQUEST, 'data':serializer.errors}
            except User.DoesNotExist:
                ResponseData = {'status': status.HTTP_404_NOT_FOUND, 'message': 'User not found'}

        elif request.method == 'DELETE':
            try:
                userData = User.objects.get(id=id)
                userData.is_active = False
                userData.save()
                ResponseData = {'status':status.HTTP_200_OK, 'data':"Deleted Successfully"}
            except User.DoesNotExist:
                ResponseData = {'status': status.HTTP_404_NOT_FOUND, 'message': 'User not found'}
        return Response(ResponseData)
    except Exception as e:
        ResponseData = {'status':status.HTTP_500_INTERNAL_SERVER_ERROR, 'data':str(e)}
    return Response(ResponseData)




# Friend    

@api_view(['GET','POST'])
def FrndData(request):
    try:
        ResponseData = None
        if request.method == 'GET':
            getData = Friend.objects.all().order_by('-id')
            serializer = FriendSerializer(getData, many=True)
            ResponseData = {'status': 200, 'data': serializer.data}
        elif request.method == 'POST':
            try:
                user_id = request.data.get('user')
                friend_id = request.data.get('friend')
                if not user_id or not friend_id:
                    return Response({'status': 400, 'data': 'User ID and Friend ID are required'})
                user = User.objects.get(id=user_id)
                friendData, created = Friend.objects.get_or_create(user=user)
                friendData.friend.add(friend_id)
                ResponseData = {'status': 200, 'data': 'Friend User added successfully'}
            except User.DoesNotExist:
                ResponseData = {'status': 404, 'data': 'User not found'}
            except Friend.DoesNotExist:
                ResponseData = {'status': 404, 'data': 'Friend not found'}
            except Exception as e:
                ResponseData = {'status': 500, 'data': str(e)}
    except Exception as e:
        ResponseData = {'status': 500, 'data': str(e)}
    return Response(ResponseData)
    


@api_view(['PUT'])
def removefrnd(request,f_id):
    try:
        responseData = None
        frnd_id = request.data['frnd_id']
        frnd_data = Friend.objects.get(user_id=f_id)
        frnd_to_remove = User.objects.get(id=frnd_id)
        frnd_data.friend.remove(frnd_to_remove)
        print("frnd_data",frnd_data,"frnd_to_remove",frnd_to_remove, "count=",frnd_data.friend.count())
        if frnd_data.friend.count() == 0:
            frnd_data.delete()
            print("executed1")
        responseData = {'status':200,'data':'Friend Id removed successfully'}
    except User.DoesNotExist:
        ResponseData = {'status': 404, 'data': 'User not found'}
    except Friend.DoesNotExist:
        ResponseData = {'status': 404, 'data': 'Friend not found'}
    except Exception as e:
        responseData = {'status':500,'data':str(e)}
    return Response(responseData)
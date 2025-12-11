from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Music Recommendation API is running!"})

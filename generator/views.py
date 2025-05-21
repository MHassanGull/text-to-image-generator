from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import json
from datetime import datetime
from django.conf import settings
from .stable_diffusion_utils import generate_image
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

@csrf_exempt
def generate_image_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # <-- FIX IS HERE
            prompt = data.get("prompt")

            if not prompt:
                return JsonResponse({"error": "Prompt is required"}, status=400)

            filename = f"{datetime.now().timestamp()}.png"
            output_path = os.path.join(settings.MEDIA_ROOT, filename)
            generate_image(prompt, output_path)

            image_url = request.build_absolute_uri(settings.MEDIA_URL + filename)
            return JsonResponse({"image_url": image_url})

        except Exception as e:
            print("Error:", str(e))
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid method"}, status=405)

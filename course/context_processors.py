from .models import *


def courses_pro(request):
    return {
        'coursesDrop': Course.objects.filter(is_active=True)
    }

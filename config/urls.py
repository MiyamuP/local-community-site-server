from django.contrib import admin
from django.urls import include , path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/',include('memorymap.urls')),#api/がパスにあるとmemorymapのapiに飛ぶ
    # path('', include('front.urls'))
    path('', include('frontend.urls'))
    #例）http://localhost:8000/api/events
    #path('events',EventListAPIView.as_view()),#10件
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

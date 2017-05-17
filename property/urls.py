from django.conf.urls import url
from .views import post_sell_view
urlpatterns = [
    url(r'^postad_sell/', post_sell_view,name='sell_page'),
    
]

from django.conf.urls import url, include

from hello.views import HomePageView, SecondPageView

urlpatterns = [

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^second/', SecondPageView.as_view(), name='second'),
    

]

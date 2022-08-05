from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from accounts.views import signup
from portfolio_app.views import index
from django.urls import include, path

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path('signup/', signup, name="signup"),
    # path('login', login_user, name='login'),
    # path('logoiut', logout_user, name='logout'),
    # path('cart, cart, name='cart'),
    # path('checkout', checkout, name='checkout'),
]

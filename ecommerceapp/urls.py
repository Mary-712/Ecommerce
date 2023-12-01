from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name='home'),
    path('loginn',views.loginn,name='loginn'),
    path('login1',views.login1,name='login1'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('userhome',views.userhome,name='userhome'),
    path('logoutt',views.logoutt,name='logoutt'),
    path('signup',views.signup,name='signup'),
    path('signupaction',views.signupaction,name='signupaction'),
    path('add_category',views.add_category,name='add_category'),
    path('add_product',views.add_product,name='add_product'),
    path('show_product',views.show_product,name='show_product'),
    path('show_user',views.show_user,name='show_user'),
    path('category',views.category,name='category'),
    path('addprod',views.addprod,name='addprod'),
    path('cart',views.cart,name='cart'),
    path('fil/<int:pk>',views.fil,name='fil'),
    path('addtocart/<int:pk>',views.addtocart,name='addtocart'),
    path('deletepage/<int:pk>',views.deletepage,name="deletepage"),
    path('deletepage1/<int:pk>',views.deletepage1,name="deletepage1"),
    path('deletepage12/<int:pk>',views.deletepage2,name="deletepage2"),
    
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
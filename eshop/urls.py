from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import *
urlpatterns = [
    path('', views.home,name='Home'),
    path('login/',views.login_page,name='Login'),
    path('logout/',views.logout_page,name='Logout'),
    path('register/',views.register,name='Register'),
    path('search',views.search,name='search'),   
    
    path('changePassword/',auth_views.PasswordChangeView.as_view(template_name='main/changePassword.html',form_class=ChangePasswordForm,success_url='/passwordChangedone'),name='passwordChange'),
    path('passwordChangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='main/passwordChangedone.html'),name='passwordChangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='main/password_reset.html',form_class=ResetPasswordForm,),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='main/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html',form_class=MysetPasswordForm,),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'),name='password_reset_complete'),

    path('collections/',views.collections,name='Collections'),
    path('collections/<str:name>',views.productView,name='Products'),
    path('collections/<str:cname>/<str:pname>',views.product_details,name='Product_details'),

    path('addcart',views.addCart,name='addCart'),
    path('cart',views.viewCart,name='Cart'),
    path('pluscart',views.plusCart,name='plusCart'),
    path('minusCart',views.minusCart,name='minusCart'),
    path('removeCart/<int:pid>',views.removeCart,name='removeCart'),

    path('addWishlist/<int:pid>',views.addWishlist,name='addWishlist'),
    path('wishlist',views.view_wishlist,name='wishlist'),
    path('addCount',views.addCount,name='addCount'),
    path('minusCount',views.minusCount,name='minusCount'),
    path('removewishlist/<int:pid>',views.remove_wishlist,name='remove_wishlist'),

    path('buyproduct/<int:pid>',views.buyProduct,name='buyproduct'),
    path('addQty',views.addQty,name='addQty'),
    path('minQty',views.minQty,name='minQty'),
    path('removeProduct/<int:product_id>',views.removeProduct,name='removeProduct'),
    
    path('profile/',views.viewProfile,name='profile'),
    path('address/',views.address,name='address'),
    path('newAddress',views.newAddress,name='newAddress'),
    path('updateAddress/<int:id>',views.updateAddress,name='updateAddress'),
    path('deleteAddress/<int:delete_id>',views.deleteAddress,name='deleteAddress'),
    path('shippingAddress/<str:product>',views.shippingAddress,name='shippingAddress'),

    path('checkout/<str:item>',views.checkOut,name='checkout'),
    path('payment/<int:custid>/<str:product_item>',views.payment,name='payment'),

    path('orderinfo',views.orderInfo,name='orderinfo'),
    path('orders',views.orders,name='orders'),
    path('viewOrders/<int:orderid>',views.viewOrders,name='viewOrders'),
    path('cancelOrder/<int:orderid>',views.cancelOrder,name='cancelOrder'),
    path('returnOrder/<int:orderid>',views.returnOrder,name='returnOrder'),
]
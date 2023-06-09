from django.urls import path,include
from.import views
from .views import EmailAttachementView


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('base', views.base, name='base'),
    path('logout', views.logout, name='logout'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile/<pk>', views.edit_profile, name='edit_profile'),
    path('itemview',views.itemview,name='itemview'),
    path('additem',views.additem,name='additem'),
    path('add',views.add,name='add'),
    path('add_account',views.add_account,name='add_account'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('edititem/<int:id>',views.edititem,name='edititem'),
    path('edit_db/<int:id>',views.edit_db,name='edit_db'),
    path('Action/<int:id>',views.Action,name='Action'),
    path('cleer/<int:id>',views.cleer,name='cleer'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('sales',views.add_sales,name='add_sales'),
    # ==================second portion====================================
    path('invoiceview',views.invoiceview,name='invoiceview'),
    path('itemdata',views.itemdata,name='itemdata'),
    path('add_prod',views.add_prod,name='add_prod'),
    path('detailedview/<int:id>',views.detailedview,name='detailedview'),
    path('edited_prod/<int:id>',views.edited_prod,name='edited_prod'),
    path('dele/<int:pk>',views.dele,name='dele'),
    path('payment_term',views.payment_term,name='payment_term'),
    path('add_cx',views.add_cx,name="add_cx"),
    path('emailattachment', EmailAttachementView.as_view(), name='emailattachment'),
    path('customerdata', views.customerdata, name='customerdata'),
path('allestimates',views.allestimates,name='allestimates'),
path('newestimate',views.newestimate,name='newestimate'),
path('add_customer_for_invoice',views.add_customer_for_invoice,name='add_customer_for_invoice'),
path('payment_term_for_invoice',views.payment_term_for_invoice,name='payment_term_for_invoice')

    
]
"""fake_product_detection URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fake_product import views

urlpatterns = [
    path('',views.main_index,name='main_index'),
    path('login',views.login,name='login'),
    path('logincode',views.logincode,name='logincode'),
    path('logout',views.logout,name='logout'),
    path('reg_form',views.reg_form,name='reg_form'),
    path('registration',views.registration,name='registration'),
    path('reg',views.reg,name='reg'),
    path('likepost',views.reg,name='likepost'),

    path('admin_home',views.admin_home,name='admin_home'),

    path('managecategory',views.managecategory,name='managecategory'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addedcategory',views.addedcategory,name='addedcategory'),
    path('deletecategory/<int:id>',views.deletecategory,name='deletecategory'),

    path('manageproduct',views.manageproduct,name='manageproduct'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('addedproduct',views.addedproduct,name='addedproduct'),
    path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct'),
    path('editproduct/<int:id>', views.editproduct, name='editproduct'),
    path('updateproduct', views.updateproduct, name='updateproduct'),
    path('searchproduct', views.searchproduct, name='searchproduct'),

    path('verify_manufacturer',views.verify_manufacturer,name='verify_manufacturer'),
    path('accept_manufacturer/<int:id>', views.accept_manufacturer, name='accept_manufacturer'),
    path('reject_manufacturer/<int:id>', views.reject_manufacturer, name='reject_manufacturer'),
    path('searchman', views.searchman, name='searchman'),


    path('view_stockinfo',views.view_stockinfo,name='view_stockinfo'),
    path('searchproduct_a',views.searchproduct_a,name='searchproduct_a'),

    path('verify_distributor',views.verify_distributor,name='verify_distributor'),
    path('accept_distributor/<int:id>', views.accept_distributor, name='accept_distributor'),
    path('reject_distributor/<int:id>', views.reject_distributor, name='reject_distributor'),
    path('searchdist', views.searchdist, name='searchdist'),

    path('verify_shop',views.verify_shop,name='verify_shop'),
    path('accept_shop/<int:id>', views.accept_shop, name='accept_shop'),
    path('reject_shop/<int:id>', views.reject_shop, name='reject_shop'),
    path('searchshop', views.searchshop, name='searchshop'),


    path('manufacturer',views.manufacturer,name='manufacturer'),

    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('viewstock/<int:id>/<str:name>',views.viewstock,name='viewstock'),
    path('searchproducts',views.searchproducts,name='searchproducts'),
    path('updatequantity/<int:id>',views.updatequantity,name='updatequantity'),
    path('updatedstock',views.updatedstock,name='updatedstock'),
    path('search_stock',views.search_stock,name='search_stock'),

    path('view_update_dist_req',views.view_update_dist_req,name='view_update_dist_req'),
    path('view_req_details/<int:id>',views.view_req_details,name='view_req_details'),
    path('accept_distreq/<int:id>', views.accept_distreq, name='accept_distreq'),
    path('reject_distreq/<int:id>', views.reject_distreq, name='reject_distreq'),
    path('search_req', views.search_req, name='search_req'),

    path('distributor',views.distributor,name='distributor'),

    path('view_manufacturer',views.view_manufacturer,name='view_manufacturer'),
    path('searchman1',views.searchman1,name='searchman1'),
    path('view_product/<int:id>',views.view_product,name='view_product'),
    path('searchproduct_d',views.searchproduct_d,name='searchproduct_d'),

    path('send_req/<int:id>/<str:p>/<int:s>',views.send_req,name='send_req'),
    path('stock', views.stock, name='stock'),

    path('view_reqstatus',views.view_reqstatus,name='view_reqstatus'),
    path('add_request',views.add_request,name='add_request'),
    path('finish_order',views.finish_order,name='finish_order'),
    path('view_reqstatus_details/<int:id>',views.view_reqstatus_details,name='view_reqstatus_details'),
    path('search_req_status',views.search_req_status,name='search_req_status'),

    path('view_reqst_shop',views.view_reqst_shop,name='view_reqst_shop'),
    path('view_req_details_s/<int:id>',views.view_req_details_s,name='view_req_details_s'),
    path('search_req_s',views.search_req_s,name='search_req_s'),
    path('accept_shopreq/<int:id>', views.accept_shopreq, name='accept_shopreq'),
    path('reject_shopreq/<int:id>', views.reject_shopreq, name='reject_shopreq'),


    path('shop',views.shop,name='shop'),
    path('view_distributor',views.view_distributor,name='view_distributor'),
    path('searchdist1',views.searchdist1,name='searchdist1'),


    path('view_product_s/<int:id>',views.view_product_s,name='view_product_s'),
    path('searchproduct_s',views.searchproduct_s,name='searchproduct_s'),

    path('send_request/<int:id>/<str:p>/<int:s>',views.send_request,name='send_request'),
    path('stock1',views.stock1,name='stock1'),

    path('add_request_s',views.add_request_s,name='add_request_s'),
    path('finish_order_s',views.finish_order_s,name='finish_order_s'),


    path('view_request_status',views.view_request_status,name='view_request_status'),
    path('view_reqstatus_details_s/<int:id>',views.view_reqstatus_details_s,name='view_reqstatus_details_s'),
    path('search_req_status_s',views.search_req_status_s,name='search_req_status_s'),

    path('view_order',views.view_order,name='view_order'),
    path('viewmore/<int:id>',views.viewmore,name='viewmore'),
    path('managebill',views.managebill,name='managebill'),
    path('addbill',views.addbill,name='addbill'),
    path('viewbill',views.viewbill,name='viewbill'),
    path('view_billsearch',views.view_billsearch,name='view_billsearch'),
    path('viewmore_bill/<int:id>',views.viewmore_bill,name='viewmore_bill'),




    path('ordrprdct',views.ordrprdct,name='ordrprdct'),
    path('srchordr_products',views.srchordr_products,name='srchordr_products'),
    path('ordrdtls/<int:id>',views.ordrdtls,name='ordrdtls'),
    path('addbill/<int:id>',views.addbill,name='addbill'),
    path('addbillcode',views.addbillcode,name='addbillcode'),
    path('ordrprdctcode',views.ordrprdctcode,name='ordrprdctcode'),

    path('view_returninfo',views.view_returninfo,name='view_returninfo'),
    path('acceptreturninfo/<int:id>',views.acceptreturninfo,name='acceptreturninfo'),
    path('rejectreturninfo/<int:id>',views.rejectreturninfo,name='rejectreturninfo'),
    path('search_retuninfo',views.search_retuninfo,name='search_retuninfo'),

    path('and_logincode',views.and_logincode,name='and_logincode'),
    path('and_registration',views.and_registration,name='and_registration'),


    path('and_vshop',views.and_vshop,name='and_vshop'),
    path('and_vshop_search',views.and_vshop_search,name='and_vshop_search'),
    path('and_vproduct',views.and_vproduct,name='and_vproduct'),
    path('and_category',views.and_category,name='and_category'),
    path('and_vproduct_search',views.and_vproduct_search,name='and_vproduct_search'),
    path('and_vproduct_details',views.and_vproduct_details,name='and_vproduct_details'),
    path('and_vone_productdet',views.and_vone_productdet,name='and_vone_productdet'),

    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('user_view_cart',views.user_view_cart,name='user_view_cart'),
    path('payment',views.payment,name='payment'),
    path('deleteviewproduct/<int:id>/<int:qid>', views.deleteviewproduct, name="deleteviewproduct"),

    path('cancel_s_order',views.cancel_s_order,name='cancel_s_order'),
    path('ordrprdctcodeand',views.ordrprdctcodeand,name='ordrprdctcodeand'),
    path('view_ordersearch',views.view_ordersearch,name='view_ordersearch'),


    path('and_vpurchase_history', views.and_vpurchase_history, name="and_vpurchase_history"),
    path('and_vreturn_info', views.and_vreturn_info, name="and_vreturn_info"),
    path('and_return_product', views.and_return_product, name="and_return_product"),

    path('andviewproducts', views.andviewproducts, name="andviewproducts"),







]

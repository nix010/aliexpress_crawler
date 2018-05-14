from django.urls import path
# from kw_search import views
from shopify_sites import views

urlpatterns = [
    path('', views.shopifypage_view, name='home'),
    
    path('sfpage/', views.shopifypage_view, name='sfpage'),
    path('sfpage/delete/<int:shopifypage_id>/', views.delete_shopifypage_view, name='delete_sfpage'),
    path('sfpage/update/<int:shopifypage_id>/', views.update_shopifypage_view, name='update_sfpage'),
    path('sfpage/products', views.shopify_product_view, name='sfpage_products'),
    path('sfpage/products/ajax', views.shopify_product_ajax_view, name='sfpage_products_ajax'),
    path('sfpage/<int:site_id>/changegroup/', views.site_change_group, name='site_change_group'),
    path('sfpage/select/', views.sites_select, name='site_select_ajax'),
    path('sfpage/ajax/', views.shopifypage_ajax_view, name='sfpage_ajax'),


    path('sitegroup/', views.sitegroup_view, name='sitegroup'),
    path('sitegroup/select/', views.sitegroup_select, name='sitegroup_select_ajax'),
    path('sitegroup/delete/<int:sitegroup_id>/', views.delete_sitegroup_view, name='delete_sitegroup'),
    
    path('login/', views.login_view, name='login'),

]
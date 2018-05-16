from django.urls import path
# from kw_search import views
from products_crawler import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('cookies/', views.cookies_view, name='cookie_list'),
    path('cookies/<int:cookie_id>/delete', views.CookieView.delete, name='cookie_delete'),
    
    
    path('category/', views.category_view, name='category_list'),
    path('category/<int:category_id>/crawlnow/', views.CategoryView.crawl_trigger, name='category_crawl'),
    path('category/<int:category_id>/delete/', views.CategoryView.delete, name='category_delete'),
    
    path('product/', views.product_view, name='product_list'),
    # path('product/', views.product_view, name='products_ajax'),

]
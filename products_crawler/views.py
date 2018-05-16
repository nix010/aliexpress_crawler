from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from products_crawler.models import *
from products_crawler.tasks import crawl_category
from products_crawler.utils import parse_cookie_str, get_aliexpress_category_name, _paginator


def home(request):
    return render(request,'base.html')



class CategoryView(TemplateView):
    
    template_name = 'category/list.html'

    def get(self, request, *args, **kwargs):
        context = {
            'categories': Category.objects.order_by('-created_at')
        }
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
    
        category_url = request.POST.get('category_url')
        if category_url:
            try:
                category_url = category_url.split('?')[0]
                category_name = get_aliexpress_category_name(category_url)
            
                obj = Category.objects.create(
                    name=category_name,
                    url =category_url,
                )
                print(obj)
        
            except:
                pass
        return redirect(category_view)

    @staticmethod
    def delete(request, *args, **kwargs):
    
        category_id = kwargs.get('category_id')
        Category.objects.get(id=category_id).delete()
        return redirect(category_view)
    
    @staticmethod
    def crawl_trigger(request, *args, **kwargs):
        
        category_id = kwargs.get('category_id')
        crawl_category.delay(category_id)
        return redirect(category_view)

category_view = CategoryView.as_view()


class ProductView(TemplateView):
    
    template_name = 'product/list.html'
    
    def ajax(self, context,page):
        page = int(page)
        return JsonResponse({
            'html'      :render_to_string('product/list_item.html',context=context),
            'page_end'  :context['products'].paginator.num_pages <= page
        })
    
    def get(self, request, *args, **kwargs):
        
        page = int(request.GET.get('page',1))
        products = Product.objects.annotate(lucky = Count('buyer', filter = Q(buyer__buyer_lucky=True)) )\
            .filter(lucky__gte =1)
        
        if request.GET.get('by_cate'):
            products = products.filter(category__id=request.GET.get('by_cate'))
        
        products = products.order_by('-updated_at')
        
        products = _paginator(products, 10,page)
        context = {
            'products': products
        }

        if request.GET.get('is_ajax'):
            return self.ajax(context,page)

        return self.render_to_response(context=context)
    
    
product_view = ProductView.as_view()


class CookieView(TemplateView):
    
    template_name = 'cookie/list.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'cookies': AliexpressCookie.objects.order_by('-created_at')
        }
        return self.render_to_response(context=context)

    def post(self, request, *args, **kwargs):
        
        cookie_text = request.POST.get('cookie')
        print(cookie_text)
        if cookie_text:
            try:
                cookie = parse_cookie_str(cookie_text)
                print(cookie)

                obj = AliexpressCookie.objects.create(cookies=cookie)
                print(obj)

            except:
                pass
        return redirect(cookies_view)
    
    @staticmethod
    def delete(request,*args, **kwargs):
        cookie_id = kwargs.get('cookie_id')
        if cookie_id:
            AliexpressCookie.objects.filter(id=cookie_id).delete()
        return redirect(cookies_view)

cookies_view = CookieView.as_view()
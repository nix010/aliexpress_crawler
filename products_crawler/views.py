from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Max
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template.loader import render_to_string
from django.views.generic import TemplateView
from products_crawler.models import *
from products_crawler.tasks import crawl_category, crawl_keyword_category
from products_crawler.utils import parse_cookie_str, get_aliexpress_category_name, _paginator


def home(request):
    return render(request,'base.html')

class LoginView(TemplateView):
    
    template_name = 'login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().get(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Logged in')
            return redirect(request.GET.get('next', '/'))
        return redirect(login_view)

login_view = LoginView.as_view()

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
                keyword = None
                if 'SearchText=' in category_url:
                    params = parse_qs(urlparse(category_url).query)
                    keyword = params.get('SearchText', [None])[0]
                    category_name = 'Keyword: %s' % keyword
                else:
                    category_url = category_url.split('?')[0]
                    category_name = get_aliexpress_category_name(category_url)
                
                obj = Category.objects.update_or_create(
                    name    =category_name,
                    url     =category_url,
                    keyword =keyword,
                    defaults=dict(
                        name=category_name,
                        url     =category_url,
                        keyword =keyword,
                    )
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
        if request.GET.get('cate_type') == 'keyword':
            crawl_keyword_category.delay(category_id)
        else:
            crawl_category.delay(category_id)
        return redirect(category_view)

category_view = login_required(CategoryView.as_view())


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
        products = Product.objects \
            .annotate(lucky = Count('buyer', filter = Q(buyer__buyer_lucky=True)) ) \
            .filter(lucky__gte =1).annotate(lucky_time=Max('buyer__buyer_time', filter = Q(buyer__buyer_lucky=True)))
        
        
        
        if request.GET.get('by_cate'):
            products = products.filter(category__id=request.GET.get('by_cate'))
        
        
        if request.GET.get('order_by'):
            products = products.order_by('-'+request.GET.get('order_by'))
        else:
            products = products.order_by('-updated_at')
        
        products = _paginator(products, 10,page)
        context = {
            'products': products
        }
        
        if request.GET.get('is_ajax'):
            return self.ajax(context,page)
        
        return self.render_to_response(context=context)


product_view = login_required(ProductView.as_view())


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

cookies_view = login_required(CookieView.as_view())
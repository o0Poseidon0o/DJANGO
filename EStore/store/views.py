from django.shortcuts import render
from store.models import Category, SubCategory, Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from store.forms import *
from cart.cart import Cart


# Create your views here.
def index(request):
    # Giỏ hàng
    cart = Cart(request)

    # Đọc danh sách sản phẩm
    # Thiết bị gia đình
    subcategory_tbgd = SubCategory.objects.filter(category=1).values_list('id')
    list_subcategoryid_tbgd = []
    for item in subcategory_tbgd:
        list_subcategoryid_tbgd.append(item[0])
    list_product_tbgd = Product.objects.filter(subcategory__in=list_subcategoryid_tbgd).order_by('-public_day')[:20]

    # Đồ dùng nhà bếp
    subcategory_ddnb = SubCategory.objects.filter(category=2).values_list('id')
    list_subcategoryid_ddnb = []
    for item in subcategory_ddnb:
        list_subcategoryid_ddnb.append(item[0])
    list_product_ddnb = Product.objects.filter(subcategory__in=list_subcategoryid_ddnb).order_by('-public_day')[:20]

    return render(request, 'store/index.html', {
        'list_product_ddnb': list_product_ddnb,
        'list_product_tbgd': list_product_tbgd,
        'cart': cart,
    })


def contact(request):
    form = FormContact()
    result = ''
    if request.POST.get('btnSendMessage'):
        form = FormContact(request.POST, Contact)
        if form.is_valid():
            request.POST._mutable = True
            post = form.save(commit=False)
            post.name = form.cleaned_data['name']
            post.phone_number = form.cleaned_data['phone_number']
            post.email = form.cleaned_data['email']
            post.subject = form.cleaned_data['subject']
            post.message = form.cleaned_data['message']
            post.save()
            result = '''
            <div class="alert alert-success" role="alert">
                Gửi thông tin thành công
            </div>
            '''
        else:
            result = '''
            <div class="alert alert-danger" role="alert">
                Gửi thông tin thất bại.
            </div>'''


    return render(request, 'store/contact.html', {
        'form': form,
        'result': result,
    })


def subcategory(request, pk):
    # Danh sách danh mục
    subcategories = SubCategory.objects.order_by('name')

    # Đọc danh sách sản phẩm theo danh mục (subcategory)
    if pk == 0:
        # Đọc tất cả
        products = Product.objects.order_by('-public_day')

        # Hiển thị tên danh mục (subcategory)
        subcategory_name = 'Tất cả sản phẩm (' + str(products.count()) + ')'
    else:
        # Đọc theo danh mục
        products = Product.objects.filter(subcategory=pk).order_by('-public_day')

        # Hiển thị tên danh mục (subcategory)
        subcategory = SubCategory.objects.get(id=pk)
        subcategory_name = str(subcategory) + ' (' + str(products.count()) + ')'

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    
    try:
        products_pager = paginator.page(page)
    except PageNotAnInteger:
        products_pager = paginator.page(1)
    except EmptyPage:
        products_pager = paginator.page(paginator.num_pages)

    return render(request, 'store/product-list.html', {
        'subcategories': subcategories,
        'products': products_pager,
        'product_slide': products_pager[:10],
        'subcategory_name': subcategory_name,
    })


def search(request):
    # Danh sách danh mục
    subcategories = SubCategory.objects.order_by('name')

    products = []
    title = ''
    if request.GET.get('product_name'):
        # Gán biến
        tu_khoa = request.GET.get('product_name').strip()
        products = Product.objects.filter(name__contains=tu_khoa).order_by('-public_day')

        # Hiển thị tiêu đề tìm kiếm
        title = 'Tìm thấy ' + str(products.count()) + ' sản phẩm với từ khóa "' + tu_khoa + '"'

    # Phân trang
    page = request.GET.get('page', 1)
    paginator = Paginator(products, 15)
    
    try:
        products_pager = paginator.page(page)
    except PageNotAnInteger:
        products_pager = paginator.page(1)
    except EmptyPage:
        products_pager = paginator.page(paginator.num_pages)

    return render(request, 'store/product-list.html', {
        'subcategories': subcategories,
        'products': products_pager,
        'subcategory_name': title,
        'product_slide': products_pager,
    })


def product_detail(request, pk):

    return render(request, 'store/product-detail.html')

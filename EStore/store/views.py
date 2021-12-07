from django.shortcuts import render
from store.my_module import check_session
from store.models import Category, SubCategory, Product


# Create your views here.
def index(request):
    session_status = check_session(request, 's_khachhang')
    session_info = request.session.get('s_khachhang') if session_status == True else {}

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
        'session_status': session_status,
        'session_info': session_info,
        'list_product_ddnb': list_product_ddnb,
        'list_product_tbgd': list_product_tbgd,
    })


def contact(request):
    return render(request, 'store/contact.html')


def subcategory(request, pk):
    session_status = check_session(request, 's_khachhang')
    session_info = request.session.get('s_khachhang') if session_status == True else {}

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

    return render(request, 'store/product-list.html', {
        'session_status': session_status,
        'session_info': session_info,
        'subcategories': subcategories,
        'products': products,
        'product_slide': products[:10],
        'subcategory_name': subcategory_name,
    })
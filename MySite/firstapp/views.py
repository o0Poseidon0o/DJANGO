from django.shortcuts import render, HttpResponse
from datetime import datetime
from firstapp.models import Category, Website, Content


# Create your views here.
def register(request):
    return render(request,'firstapp/register.html')


def read_websites(request):
    websites = Website.objects.order_by('name')
    # print(websites)
    return render(request, 'firstapp/websites.html', {
        'websites': websites,
    })

def read_contents(request):
    contents = Content.objects.order_by('name')
    print(contents)
    return render(request, 'firstapp/contents.html', {
        'contents': contents,
    })

def contents_by_web(request, pk):
    contents = Content.objects.filter(website=pk)
    print(contents)
    return render(request, 'firstapp/contents.html', {
        'contents': contents,
    })

def index(request):
    return HttpResponse('Trang chủ')

def contact(request):
    return HttpResponse('Liên hệ')

def products(request):
    return HttpResponse('Danh sách sản phẩm')

def product(request, id_product):
    ket_qua = 'Bạn đang xem sản phẩm %i' %id_product
    return HttpResponse(ket_qua)

def tinh_tong(request, a, b):
    ket_qua = 'Tổng = %i + %i = %i' % (a, b, a + b)
    return HttpResponse(ket_qua)

def read_year(request, year):
    kq = 'This year is %s' % year
    return HttpResponse(kq)

def index_3(request):
    tong = 15 + 6
    cau_chao = 'Chào mừng bạn đến với Lập trình Python'

    dtb = 8.5

    ds_san_pham = ['Sản phẩm 1', 'Sản phẩm 2', 'Sản phẩm 3', 'Sản phẩm 4', 'Sản phẩm 5']

    hoc_sinh = {
        'Ma_so': 'HS01',
        'Ho_ten': 'Học sinh 1',
        'Dia_chi': 'TPHCM',
        'Ngay_sinh': '11/11/2000',
        'Email': 'hs1@gmail.com'
    }

    ds_hoc_sinh = [
        {
            'Ma_so': 'HS01',
            'Ho_ten': 'Học sinh 1',
            'Dia_chi': 'TPHCM',
            'Ngay_sinh': '11/11/2000',
            'Email': 'hs1@gmail.com'
        },
        {
            'Ma_so': 'HS02',
            'Ho_ten': 'Học sinh 2',
            'Dia_chi': 'TPHCM',
            'Ngay_sinh': '11/11/2000',
            'Email': 'hs2@gmail.com'
        },
        {
            'Ma_so': 'HS03',
            'Ho_ten': 'Học sinh 3',
            'Dia_chi': 'TPHCM',
            'Ngay_sinh': '11/11/2000',
            'Email': 'hs3@gmail.com'
        },
        {
            'Ma_so': 'HS04',
            'Ho_ten': 'Học sinh 4',
            'Dia_chi': 'TPHCM',
            'Ngay_sinh': '11/11/2000',
            'Email': 'hs4@gmail.com'
        }
    ]

    ngay_hien_hanh = datetime.now()

    # print(hoc_sinh.items())
    # print(hoc_sinh['Ma_so'])

    # for hoc_sinh in ds_hoc_sinh:
    #     print(ds_hoc_sinh.index(hoc_sinh) + 1)

    # stt = 0
    # for hoc_sinh in ds_hoc_sinh:
    #     stt += 1
    #     print(stt)

    return render(request, 'firstapp/index.html', {
        'Tong': tong,
        'Cau_chao': cau_chao,
        'DTB': dtb,
        'DS_San_pham': ds_san_pham,
        'Hoc_sinh': hoc_sinh,
        'DS_hoc_sinh': ds_hoc_sinh,
        'Ngay_hien_hanh': ngay_hien_hanh,
    })


def index_2(request):
    return HttpResponse('''
    <!DOCTYPE html>
<html>

<head>
    <title>Page Title</title>

    <style>
        /* p {
            background-color: #FFFF66;
        } */

        /* .doan_van {
            background-color: #FFFF66;
        }

        #bang_cua_toi {
            background-color: #FF9999;
        } */
    </style>

    <link rel="stylesheet" href="css/style.css">
</head>

<body>

    <h1>This is heading 1</h1>
    <h2>This is heading 2</h2>
    <h3>This is heading 3</h3>
    <h4>This is heading 4</h4>
    <h5>This is heading 5</h5>
    <h6>This is heading 6</h6>

    <p class="doan_van" style="color: red; font-family: Arial, Helvetica, sans-serif; font-size: 20px;">Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the
        embed code for the video you want to add. You can also type a keyword to search online for the video that best
        fits your document. To make your document look professionally produced, Word provides header, footer, cover
        page, and text box designs that complement each other.</p>

    <p class="doan_van" style="font-size: 25px;"><b>Video</b> provides a <i>powerful way to help you prove your point</i>. When you click Online Video, you can paste in the
        <u>embed code</u> for the video you want to add. You can also type a keyword to search online for the video that best
        fits your document. To make your document look professionally produced, Word provides header, footer, cover
        page, and text box designs that complement each other.</p>

    <div style="text-decoration: underline;">Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the
        embed code for the video you want to add. You can also type a keyword to search online for the video that best
        fits your document. To make your document look professionally produced, Word provides header, footer, cover
        page, and text box designs that complement each other.</div>

    <div style="text-decoration: overline;">Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the
        embed code for the video you want to add. You can also type a keyword to search online for the video that best
        fits your document. To make your document look professionally produced, Word provides header, footer, cover
        page, and text box designs that complement each other.</div>

    <hr style="border: 5px; border-color: red; border-style: dotted;">

    <div style="text-decoration: line-through;">Video provides a powerful way to help you prove your point. When you click Online Video, you can paste in the
        embed code for the video you want to add. You can also type a keyword to search online for the video that best
        fits your document. <br>To make your document look professionally produced, Word provides header, footer, cover
        page, and text box designs that complement each other.</div>

    <br>

    <hr style="border: 5px red dotted;">

    <p style="font-size: 25px;">H<sub>2</sub>0, H<sub>2</sub>S0<sub>4</sub></p>

    <p style="font-size: 25px;">10<sup>5</sup>, 102<sup>8</sup></p>

    <p>
        <pre>
            *
        *       *
    *               *
*                       *
        </pre>
    </p>

    <table border="1px" id="bang_cua_toi">
        <tr>
            <th>Month</th>
            <th>Savings</th>
        </tr>
        <tr>
            <td>January</td>
            <td>$100</td>
        </tr>
    </table>

    <br>

    <a href="https://www.w3schools.com" target="_blank">Visit W3Schools.com!</a>

    <br>

    <ul>
        <li>Coffee</li>
        <li>Tea</li>
        <li>Milk</li>
    </ul>

    <ol>
        <li>Coffee</li>
        <li>Tea</li>
        <li>Milk</li>
    </ol>

    <br><br>

    <img src="images/xe.jpeg" alt="Xe o to">

    <br>


</body>

</html>
    ''')


def demo_static(request):

    return render(request, 'firstapp/demo_static.html')
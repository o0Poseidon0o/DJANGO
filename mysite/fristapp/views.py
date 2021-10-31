from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse ('Chao ca lop')
def products(request):
    return HttpResponse ('danh sach san pham')
def product(request,id_product):
    ketqua= 'ban dang xem san pham %i' %id_product
    return HttpResponse(ketqua)
def index_3(request):
    dtb=5
    sanpham=['sanpham1','sanpham2','sanpham3']
    cot=['STT','Ma hoc sinh','ten hoc sinh','Ngay sinh','noi sinh','Dia chi']
    dong=['1','2','3','4','5']
    ten=[
        {
             'a':'1',
             'b':'1',
             'c':'1',
             'd':'1',
             'e':'1',
        },
        {
             'a':'2',
             'b':'2',
             'c':'2',
             'd':'2',
             'e':'2',
        },
        {
             'a':'3',
             'b':'3',
             'c':'3',
             'd':'3',
             'e':'3',
        },
        {
             'a':'4',
             'b':'4',
             'c':'4',
             'd':'4',
             'e':'4',
        },
        {
             'a':'5',
             'b':'5',
             'c':'5',
             'd':'5',
             'e':'5',
        }
    ]
    test={ 'a':'1',
             'b':'1',
             'c':'1',
             'd':'1',
             'e':'1',}
   
    return render(request,'fristapp/index.html',{
        'DTB':dtb,
        'sanpham':sanpham,
        'COT':cot,
        'dong':dong,
        'test':test,     
        'ten':ten,
    })
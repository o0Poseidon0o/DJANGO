from django.shortcuts import redirect, render
from customer import forms
from customer import models
from store.my_module import *


# Create your views here.
def login(request):
    session_status = check_session(request, 's_khachhang')
    if session_status:
        return redirect('store:index')

    # Đăng ký
    result_register = ''
    form = forms.FormDangKy()
    if request.POST.get('btnDangKy'):
        form = forms.FormDangKy(request.POST, models.Customer)
        if form.is_valid():
            if form.cleaned_data['mat_khau'] == form.cleaned_data['xac_nhan_mat_khau']:
                request.POST._mutable = True
                post = form.save(commit=False)
                post.ho = form.cleaned_data['ho']
                post.ten = form.cleaned_data['ten']
                post.email = form.cleaned_data['email']
                post.mat_khau = form.cleaned_data['mat_khau']
                post.dien_thoai = form.cleaned_data['dien_thoai']
                post.dia_chi = form.cleaned_data['dia_chi']
                post.save()
                result_register = '''
                <div class="alert alert-success" role="alert">
                    Đăng ký thành viên thành công!
                </div>
                '''
            else:
                result_register = '''
                <div class="alert alert-warning" role="alert">
                    Mật khẩu và Xác nhận mật khẩu không khớp!
                </div>
                '''
        else:
            result_register = '''
                <div class="alert alert-danger" role="alert">
                    Đăng ký thành viên không thành công. Vui lòng kiểm tra lại thông tin nhập!
                </div>
                '''

    # Đăng nhập
    result_login = ''
    if request.POST.get('btnDangNhap'):
        # Gán biến
        email = request.POST.get('email')
        mat_khau = request.POST.get('mat_khau')

        # Đọc dữ liệu
        khach_hang = models.Customer.objects.filter(email=email, mat_khau=mat_khau)

        if khach_hang.count() > 0:
            request.session['s_khachhang'] = khach_hang.values()[0]
            return redirect('store:index')
        else:
            result_login = '''
            <div class="alert alert-danger" role="alert">
                Đăng nhập thất bại
            </div>
            '''

    return render(request, 'store/login.html', {
        'form': form,
        'result_register': result_register,
        'result_login': result_login,
    })


def logout(request):
    if request.session.get('s_khachhang'):
        del request.session['s_khachhang']
    return redirect('customer:login')

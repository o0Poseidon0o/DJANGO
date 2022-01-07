from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from customer import forms
from customer import models
from store.my_module import *
from django.contrib.auth.hashers import Argon2PasswordHasher, PBKDF2PasswordHasher
from customer.forms import FormUser, FormUserProfileInfo


# Create your views here.
def users(request):
    form_user = FormUser()
    form_profile = FormUserProfileInfo()
    result_register = ''

    if request.POST.get('btnDangKy'):
        form_user = FormUser(request.POST)
        form_profile = FormUserProfileInfo(request.POST, request.FILES)

        if form_user.is_valid() and form_profile.is_valid():
            if form_user.cleaned_data['password'] == form_user.cleaned_data['confirm_password']:
                # GHI VÀO CSDL
                # User
                user = form_user.save()
                user.set_password(user.password)
                user.save()

                # Profile
                profile = form_profile.save(commit=False)
                profile.user = user
                profile.save()

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

    if request.POST.get('btnDangNhap'):
        # Gán biến
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('customer:users')
    print(request.user)

    return render(request, 'store/user.html', {
        'form_user': form_user,
        'form_profile': form_profile,
        'result_register': result_register,
    })


def logout_user(request):
    logout(request)
    return redirect('customer:users')


def login_customer(request):
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
                # hasher = Argon2PasswordHasher()  # salt: 8 bytes
                hasher = PBKDF2PasswordHasher() # salt: 1 byte
                request.POST._mutable = True
                post = form.save(commit=False)
                post.ho = form.cleaned_data['ho']
                post.ten = form.cleaned_data['ten']
                post.email = form.cleaned_data['email']
                post.mat_khau = hasher.encode(form.cleaned_data['mat_khau'], '1')
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
        hasher = Argon2PasswordHasher()
        encoded = hasher.encode(mat_khau, '12345678')

        # Đọc dữ liệu
        khach_hang = models.Customer.objects.filter(email=email, mat_khau=encoded)

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


def logout_customer(request):
    if request.session.get('s_khachhang'):
        del request.session['s_khachhang']
    return redirect('customer:login')

from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .decorators import *
from .forms import *
from .tokens import *
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage


def signup_redirect(request):
    messages.error(request, "Wystąpił błąd, może już masz założone konto o takich danych!")
    return redirect("homepage")


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Dziękujemy za potwierdzenie emaila, teraz możesz się zalogować.')
        return redirect('login')
    else:
        messages.error(request, 'Aktywacyjny link jest nie ważny!')
    return redirect('index')


def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('authorization/activateAccount.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Drogi <b>{user}</b>, proszę sprawdź swoją skrzynkę pocztową <b>{to_email}</b> i kliknij \
            otzymany link aktywacyjny, żeby zatwierdzić rejestrację <b>Uwaga:</b> Sprawdź też katalog spam.')
    else:
        messages.error(request, f'Problem z wysłaniem maila potwierdzającego na adres email {to_email}. Sprawdź czy podałeś prawidłowego emaila.')


@user_not_authenticated
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # login(request, user)
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('/')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()
    return render(request, "authorization/register.html", {"form": form})


@login_required
def customLogout(request):
    logout(request)
    messages.info(request, "Udało się wylogować!")
    return redirect("index")


@user_not_authenticated
def customLogin(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user)
                messages.success(request, f"Witaj <b>{user.username}</b>! Udało ci się prawidłowo zalogować")
                if 'next' in request.POST:
                    return redirect(request.POST['next'])
                return redirect("index")
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    form = UserLoginForm()
    return render(request=request, template_name="authorization/login.html", context={"form": form})

def profile(request, username):
    return redirect("index")
    # if request.method == "POST":
    #     user = request.user
    #     form = UserUpdateForm(request.POST, request.FILES, instance=user)
    #     if form.is_valid():
    #         user_form = form.save()
    #         messages.success(request, f'{user_form.username}, Your profile has been updated!')
    #         return redirect("profile", user_form.username)
    #
    #     for error in list(form.errors.values()):
    #         messages.error(request, error)
    #
    # user = get_user_model().objects.filter(username=username).first()
    # if user:
    #     form = UserUpdateForm(instance=user)
    #     form.fields['description'].widget.attrs = {'rows': 1}
    #     return render(
    #         request=request,
    #         template_name="users/profile.html",
    #         context={"form": form}
    #     )
    #
    # return redirect("index")
#
#
# @login_required
# def password_change(request):
#     user = request.user
#     if request.method == 'POST':
#         form = SetPasswordForm(user, request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your password has been changed")
#             return redirect('login')
#         else:
#             for error in list(form.errors.values()):
#                 messages.error(request, error)
#
#     form = SetPasswordForm(user)
#     return render(request, 'password_reset_confirm.html', {'form': form})
#
#
# @user_not_authenticated
# def password_reset_request(request):
#     if request.method == 'POST':
#         form = PasswordResetForm(request.POST)
#         if form.is_valid():
#             user_email = form.cleaned_data['email']
#             associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
#             if associated_user:
#                 subject = "Password Reset request"
#                 message = render_to_string("template_reset_password.html", {
#                     'user': associated_user,
#                     'domain': get_current_site(request).domain,
#                     'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
#                     'token': account_activation_token.make_token(associated_user),
#                     "protocol": 'https' if request.is_secure() else 'http'
#                 })
#                 email = EmailMessage(subject, message, to=[associated_user.email])
#                 if email.send():
#                     messages.success(request,
#                                      """
#                                      <h2>Password reset sent</h2><hr>
#                                      <p>
#                                          We've emailed you instructions for setting your password, if an account exists with the email you entered.
#                                          You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address
#                                          you registered with, and check your spam folder.
#                                      </p>
#                                      """
#                                      )
#                 else:
#                     messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")
#
#             return redirect('homepage')
#
#         for key, error in list(form.errors.items()):
#             if key == 'captcha' and error[0] == 'This field is required.':
#                 messages.error(request, "You must pass the reCAPTCHA test")
#                 continue
#
#     form = PasswordResetForm()
#     return render(
#         request=request,
#         template_name="password_reset.html",
#         context={"form": form}
#     )
#
#
# def passwordResetConfirm(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.objects.get(pk=uid)
#     except:
#         user = None
#
#     if user is not None and account_activation_token.check_token(user, token):
#         if request.method == 'POST':
#             form = SetPasswordForm(user, request.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
#                 return redirect('homepage')
#             else:
#                 for error in list(form.errors.values()):
#                     messages.error(request, error)
#
#         form = SetPasswordForm(user)
#         return render(request, 'password_reset_confirm.html', {'form': form})
#     else:
#         messages.error(request, "Link is expired")
#
#     messages.error(request, 'Something went wrong, redirecting back to Homepage')
#     return redirect("homepage")

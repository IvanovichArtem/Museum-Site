from typing import Any
from django.shortcuts import render, HttpResponseRedirect
from user.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth
from django.urls import reverse, reverse_lazy
from catalog.models import Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from user.models import User


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("catalog:home"))
        else:
            print("form is not valid")
    else:
        form = UserLoginForm()

    context = {"form": form}
    return render(request, "user/login.html", context)


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "user/registration.html"
    success_url = reverse_lazy("user:login")


# def registration(request):
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Вы успешно зарегестрировались.")
#             return HttpResponseRedirect(reverse("user:login"))
#         else:
#             print("form is not valid")
#     else:
#         form = UserRegistrationForm()

#     context = {"form": form}
#     return render(request, "user/registration.html", context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("catalog:home"))


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = "user/profile.html"

    def get_success_url(self) -> str:
        return reverse_lazy("user:profile", args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Личный кабинет"
        context["baskets"] = Basket.objects.filter(user=self.request.user)
        return context


# @login_required
# def profile(request):
#     if request.method == "POST":
#         form = UserProfileForm(
#             instance=request.user, data=request.POST, files=request.FILES
#         )
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("user:profile"))
#         else:
#             print("Form is not valid", form.errors)
#     else:
#         form = UserProfileForm(instance=request.user)

#     context = {
#         "title": "Профиль",
#         "form": form,
#         "baskets": Basket.objects.filter(user=request.user),
#     }
#     return render(request, "user/profile.html", context)

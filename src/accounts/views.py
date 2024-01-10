from django.contrib.auth import get_user_model, login
from django.http import HttpResponse
from django.shortcuts import render  # NOQA: F401
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView, RedirectView

from accounts.forms import UserRegistrationForm
from accounts.services.emails import send_registration_email
from accounts.utils.token_generator import TokenGenerator


class UserRegistration(CreateView):
    template_name = "registration/create_user.html"
    form_class = UserRegistrationForm
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()

        send_registration_email(request=self.request, user_instance=self.object)

        return super().form_valid(form)


class ActivateUserView(RedirectView):
    url = reverse_lazy("index")

    def get(self, request, uuid64, token, *args, **kwargs):
        try:
            pk = force_str(urlsafe_base64_decode(uuid64))
            current_user = get_user_model().objects.get(pk=pk)
        except (get_user_model().DoesNotExist, TypeError, ValueError):
            return HttpResponse("Wrong data!!!")

        if current_user and TokenGenerator().check_token(current_user, token):
            current_user.is_active = True
            current_user.save()

            login(
                request,
                current_user,
                backend="django.contrib.auth.backends.ModelBackend",
            )

            return super().get(request, *args, **kwargs)
        return HttpResponse("Wrong data!!!")

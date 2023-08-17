from django.shortcuts import redirect
from django.contrib import messages

class RedirectToHome:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user home', request.user.pk)

        return super().dispatch(request, *args, **kwargs)


class SuccessMessageMixin:
    """
    Add a success message on successful form submission.
    """
    success_message = ''

    def form_valid(self, form):
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            messages.success(self.request, success_message)
        return response

    def get_success_message(self, cleaned_data):
        return self.success_message % cleaned_data
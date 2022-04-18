from django.shortcuts import redirect


class RedirectToHome:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user home', request.user.pk)

        return super().dispatch(request, *args, **kwargs)
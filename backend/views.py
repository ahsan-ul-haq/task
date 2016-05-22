"""
View to render form on frontend.
"""
from django.shortcuts import render
from django.views.generic import View

from backend.forms import UserInfoForm


class UserInfoView(View):

    def get(self, request):
        """Get form and render to frontend."""
        form = UserInfoForm()
        return render(request, 'home.html', {'form': form})

    def post(self, request):
        """Get data from form post method and pass it to form to save data."""
        form = UserInfoForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except ValueError:
                return render(request, 'home.html', {'form': form})
        else:
            return render(request, 'home.html', {'form': form})

        return render(request, 'display.html', {'name': request.POST['name']})

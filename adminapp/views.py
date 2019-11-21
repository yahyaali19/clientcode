from django.views.generic import TemplateView

from .models import Representative
from .utils import calculate_progress_bar


class RepresentativeView(TemplateView):
    template_name = "adminapp/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['representative_data'] = Representative.objects.all().order_by('monthly_FTD')
        context['progress_bar'] = calculate_progress_bar()
        return context

from django.views.generic import TemplateView

from .models import Representative
from .utils import calculate_progress_bar, all_sum


class RepresentativeView(TemplateView):
    template_name = "adminapp/home.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['progress_bar'] = calculate_progress_bar()
        context['representative_data'] = Representative.objects.all().order_by('-monthly_FTD')
        context['target_total'], context['monthly_FTD_total'], context['monthly_amount_total'], context['daily_FTD_total'], context['daily_amount_total'] = all_sum()
        return context

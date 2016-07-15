from django.views.generic.base import TemplateView
from resources.models import UseControl

class UseControlView(TemplateView):
    template_name = "usecontrol_list.html"

    def get_context_data(self, **Kwargs):
        context = super(UseControlView, self).get_context_data(**Kwargs)
        usecontrol = UseControl.objects.all().first()

        context['vehicle'] = usecontrol.vehicle.name,
        context['drive'] = usecontrol.driver.name,
        context['date_started'] = usecontrol.date_started

        return context

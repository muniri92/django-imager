"""Views for the Imager Site."""
from django.views.generic import TemplateView
from imager_images.models import Photo


class ClassView(TemplateView):
    """Home page template."""

    template_name = 'home.html'

    def get_context_data(self):
        """Pass image to the homepage."""
        try:
            img = Photo.objects.all().order_by("?")[0]
        except IndexError:
            img = None
        return {'img': img}

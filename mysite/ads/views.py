from ads.models import Advertisement
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView


class AdListView(OwnerListView):
    model = Advertisement
    # By convention:
    # template_name = "myarts/article_list.html"


class AdDetailView(OwnerDetailView):
    model = Advertisement


class AdCreateView(OwnerCreateView):
    model = Advertisement
    fields = ['title', 'text', 'price']


class AdUpdateView(OwnerUpdateView):
    model = Advertisement
    fields = ['title', 'text', 'price']


class AdDeleteView(OwnerDeleteView):
    model = Advertisement
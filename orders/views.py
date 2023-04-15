from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from common.views import TitleMixin
from orders.forms import OrderForm
from products.models import Basket


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order_create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(OrderCreateView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.request.user)
        return context

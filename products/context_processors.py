from products.models import Basket


def baskets(request):
    user = request.user
    return {'baskets': Basket.objects.filter(user=request.user if user.is_authenticated else [])}

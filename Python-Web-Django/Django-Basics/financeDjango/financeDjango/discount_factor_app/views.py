from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import FormView

from financeDjango.mixins import OperationNameContextMixin


# Create your views here.

class CalculateDiscountFactor(LoginRequiredMixin, OperationNameContextMixin, FormView):
    pass


class DiscountingPresentValue(LoginRequiredMixin, OperationNameContextMixin, FormView):
    pass
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from financeDjango.mixins import PlaceholderMixin
from financeDjango.personal_actions_app.forms import TransactionForm
from financeDjango.personal_actions_app.models import Transaction


class CreateTransactionView(LoginRequiredMixin, CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'personal_actions_templates/transaction_templates/create_transaction.html'
    success_url = reverse_lazy('show-transactions')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = 'personal_actions_templates/transaction_templates/transaction_list.html'
    context_object_name = 'transactions'
    paginate_by = 5

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by('-date')


class CreatePortfolioView(LoginRequiredMixin, CreateView):


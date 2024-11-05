class OperationNameContextMixin:
    operation_name = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['operation_name'] = self.operation_name
        return context

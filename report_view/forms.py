from django import forms
from report_view.models import Report
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Button
from crispy_forms.bootstrap import FormActions


class ReportForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.add_input(Submit('save', 'Save'))
        self.helper.add_input(Button('cancel', 'Cancel'))
        FormActions(
            Submit('save', 'Save changes'),
            Button('cancel', 'Cancel'),
        )

    class Meta:
        model = Report

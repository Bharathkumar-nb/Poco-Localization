from django import forms
from codemirror import CodeMirrorTextarea

class CodeForm(forms.Form):
    codemirror_widget = CodeMirrorTextarea(mode="python", theme="cobalt", config={ 'fixedGutter': True })
    document = forms.CharField(widget=codemirror_widget)

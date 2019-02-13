from django import forms


class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'style': 'height:150px;width:95%;', 'placeholder': "写点什么", 'class': "form-control",
               'id':"reply_content","required":"required"}), required=True)
    parent_comment_id = forms.CharField(widget=forms.TextInput(attrs={"id":"reply_id","class":"d-none",}),required=False)

from django import forms
from .models import ModelPP

# Model Form (모델 폼)
class ModelPPForm(forms.ModelForm):
	class Meta:
		model = ModelPP
		#fields = ['__all__'] # '__all__' 설정시 전체 필드 추가
		fields = ['tid', 'vuser','tests','sucessTest','meanResp','flag','dateTime']
from django.shortcuts import render
from googletrans import Translator
from .forms import TranslateForm

def translate_text(request):
    if request.method == 'POST':
        form = TranslateForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            target_language = form.cleaned_data['target_language']
            translator = Translator()
            translation = translator.translate(text, dest=target_language)
            translated_text = translation.text
            return render(request, 'translate.html', {'form': form, 'translated_text': translated_text})
    else:
        form = TranslateForm()
    return render(request, 'translate.html', {'form': form})

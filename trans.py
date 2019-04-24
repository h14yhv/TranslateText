from googletrans import Translator
translator = Translator()
 
translation = translator.translate('안녕하세요.', dest='vi')
print(translation.text)
# <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>

print(translator.translate('안녕하세요.', dest='vi'))
print(translation.text)
# <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>

print(translator.translate('veritas lux mea', src='la', dest='vi'))
print(translation.text)
# <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
import aspose as ocr

''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.PreprocessingFilter()
#filters.add(ocr.PreprocessingFilter.invert())


''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add("Data\\OCR\\sample.png")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.set_detect_areas_mode(ocr.DetectAreasMode.PHOTO)


''' run recognition '''
res = api.recognize(input)
print(res[0].recognition_text)

''' print corrected text '''
print(res[0].get_spell_check_corrected_text(ocr.SpellCheckLanguage.ENG))

''' print errors'''
errors = res[0].get_spell_check_error_list(ocr.SpellCheckLanguage.ENG)
for error in errors:
    print('-----word------')
    print(error.word)
    for correction in error.suggested_words:
        print('-----suggested_words------')
        print(correction.word)
        print(correction.distance)
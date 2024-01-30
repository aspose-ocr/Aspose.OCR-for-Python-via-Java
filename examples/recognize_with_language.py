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
input.add("Data\\OCR\\chinese.png")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.set_language(ocr.Language.CHI)


''' run recognition '''
res = api.recognize(input, settings)
print(res[0].recognition_text)

api.save_multipage_document("chinese1.txt", ocr.Format.TEXT, res)
res[0].save("chinese.json", ocr.Format.JSON)
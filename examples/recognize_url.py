import aspose as ocr

''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
filters = ocr.PreprocessingFilter()
filters.add(ocr.PreprocessingFilter.auto_skew())


''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.URL, filters)
url = "https://assets.accessible-digital-documents.com/uploads/2017/03/justified-text.gif"
input.add(url)


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.set_detect_areas_mode(ocr.DetectAreasMode.DOCUMENT)


''' run recognition '''
res = api.recognize(input)
print(res[0].recognition_text)
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
input = ocr.OcrInput(ocr.InputType.DIRECTORY, filters)
input.add("Data\\OCR\\OCR")


''' change recognition options if you need '''
settings = ocr.RecognitionSettings()
settings.set_detect_areas_mode(ocr.DetectAreasMode.DOCUMENT)


''' run recognition '''
res = api.recognize(input, settings)

''' print result '''
for r in res:
    print('------------------')
    print(r.recognition_text)
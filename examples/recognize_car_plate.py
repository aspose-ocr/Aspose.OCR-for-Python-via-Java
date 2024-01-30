import aspose as ocr

''' set license '''

#lic = ocr.license.License()
#lic.set_license('path')


''' initialize main class '''
api = ocr.AsposeOcr()


''' add filters if you need '''
#filters = ocr.PreprocessingFilter()
#filters.add(ocr.PreprocessingFilter.auto_skew())

''' initialize image collection and put images into it '''
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add("Data\\OCR\\car.jfif")

''' change recognition options if you need '''
settings = ocr.CarPlateRecognitionSettings()

''' run recognition '''
res = api.recognize_car_plate(input, settings)

''' print result '''
print(res[0].recognition_text)
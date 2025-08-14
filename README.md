![PyPI](https://img.shields.io/pypi/v/aspose-ocr-python-java) ![PyPI](https://img.shields.io/pypi/dm/aspose-ocr-python-java) ![GitHub](https://img.shields.io/github/license/aspose-ocr/Aspose.OCR-for-Python-via-Java)

# Optical Character Recognition (OCR) Python API via Java

This is a standalone OCR API that enhances your Python applications to [perform OCR on JPEG, PNG, GIF, BMP & TIFF images](https://docs.aspose.com/ocr/python-java/supported-file-formats/) for extraction of text content in multiple languages.

[Aspose.OCR for Python via Java](https://products.aspose.com/ocr/python-java) not only provides the Optical Character Recognition engine but more. You can also apply Blur, Gaussian Blur, and Median filter to reduce noise before document recognition and can set the OcrEngine to ignore non-textual blocks, maintain correct text order during document text recognition & automatically correct spellings of the document text.

<p align="center">
  <a href="https://github.com/aspose-ocr/Aspose.OCR-for-Python-via-Java/archive/master.zip">
    <img src="http://i.imgur.com/hwNhrGZ.png" />
  </a>
</p>

Directory | Description
--------- | -----------
[examples](examples)  | A collection of Python examples that help you learn the product features.

## Image OCR API Features

- Programmatically [detect, identify and read characters](https://docs.aspose.com/ocr/python-java/recognition/) from images.
- Currently, it supports 140+ languages based on Latin, Cyrillic, Asian, Arabic, and other scripts.
- Detect and read popular font faces such as Arial, Times New Roman, Courier New, Tahoma, Calibri & Verdana.
- Supports regular, bold and italic font styles.
- Scan whole image or only a specific portion of the image.
- Scan rotated images.
- Application of various noise removal filters to assist image recognition.
- Calculate the bounding boxes of lines, paragraphs, words.
- Get possible choices for each recognized character.
- Pass URI and recognize the image from it.
- Recognize multiple images in a folder, zip archive or in the list.
- Get result in JSON or XML format.
- Save results in text, DOCX, PDF, XLSX, XML, JSON formats

Aspose.OCR can recognize a large number of languages and all popular writing scripts, including texts with mixed languages.

## Load Images for OCR

**Raster Formats:** JPEG, PNG, GIF, BMP, TIFF

## Platform Independence

You can use Aspose.OCR for Python via Java to develop applications in any development environment that supports Python 3.8 and higher with Java Runtime Environment (JRE) 8 or above. The library is built on top of Java, providing cross-platform compatibility.

## System Requirements

- **Python:** 3.8 or higher
- **Java Runtime Environment (JRE):** 8 or above
- **Operating Systems:** Microsoft Windows, Linux, and macOS

## Get Started with Aspose.OCR for Python via Java

Are you ready to give Aspose.OCR for Python via Java a try? Simply execute `pip install aspose-ocr-python-java` to fetch the package from PyPI. If you already have Aspose.OCR for Python via Java and want to upgrade the version, please execute `pip install --upgrade aspose-ocr-python-java` to get the latest version.

## Quick Setup

1. **Install the package:**
   ```bash
   pip install aspose-ocr-python-java
   pip install Jpype1
   ```

2. **Run examples:**
   ```bash
   # Windows
   run.cmd
   
   # Linux/Mac
   ./run.sh
   ```

## Perform OCR on PNG Image via Python Code

```python
import aspose as ocr

# initialize main class
api = ocr.AsposeOcr()

# add filters if you need
filters = ocr.PreprocessingFilter()
filters.add(ocr.PreprocessingFilter.invert())

# initialize image collection and put images into it
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add('Data/OCR/sample.png')

# change recognition options if you need
settings = ocr.RecognitionSettings()
settings.set_detect_areas_mode(ocr.DetectAreasMode.PHOTO)

# run recognition
res = api.recognize(input)
print(res[0].recognition_text)
```

## Available Examples

This repository contains the following Python examples:

- **Basic Recognition:**
  - `recognize.py` - Basic image recognition
  - `recognize_line.py` - Line-by-line text recognition
  - `recognize_images_batch.py` - Batch processing of multiple images

- **Specialized Recognition:**
  - `recognize_table.py` - Table structure recognition
  - `recognize_passport.py` - Passport document recognition
  - `recognize_car_plate.py` - License plate recognition
  - `recognize_street_photo.py` - Street sign recognition

- **Advanced Features:**
  - `recognize_with_language.py` - Multi-language recognition
  - `recognize_with_spell_check.py` - Spell-checking during recognition
  - `recognize_with_detect_areas_mode.py` - Custom area detection modes
  - `calculate_skew.py` - Image skew calculation and correction
  - `image_text_finder.py` - Text location detection

- **Input Sources:**
  - `recognize_url.py` - Recognition from URL
  - `recognize_folder.py` - Recognition from folder
  - `recognize_archive.py` - Recognition from archive files

- **Output Options:**
  - `recognize_and_save_result_as_file.py` - Save results to various formats

## Data Directory

The `examples/Data/` directory contains sample images and resources for testing the examples:
- Various image formats (PNG, JPEG, BMP, etc.)
- Multi-language text samples
- Table structures
- Document samples (passports, etc.)

## Installation and Setup

### Prerequisites
- Python 3.8 or higher
- Java Runtime Environment (JRE) 8 or above
- pip package manager

### Installation Steps
1. **Install the required packages:**
   ```bash
   pip install aspose-ocr-python-java
   pip install Jpype1
   ```

2. **Verify installation:**
   ```python
   import aspose as ocr
   print("Aspose.OCR for Python via Java is ready!")
   ```

### Running Examples
Navigate to the `examples` directory and run:
- **Windows:** `run.cmd`
- **Linux/Mac:** `./run.sh`

## Project Structure

```
Aspose.OCR-for-Python-via-Java/
├── examples/                    # Python example scripts
│   ├── Data/                   # Sample images and test data
│   │   ├── OCR/               # OCR-specific test images
│   │   └── ...                # Various image formats
│   ├── recognize.py           # Basic OCR example
│   ├── recognize_line.py      # Line-by-line recognition
│   ├── recognize_table.py     # Table structure recognition
│   ├── run.cmd               # Windows execution script
│   └── run.sh                # Linux/Mac execution script
├── LICENSE                    # Project license
└── README.md                 # This file
```

## Key Features

### Advanced Recognition Capabilities
- **Multi-language Support:** Recognize text in 153 languages
- **Font Recognition:** Supports popular fonts (Arial, Times New Roman, etc.)
- **Style Detection:** Regular, bold, and italic text styles
- **Layout Analysis:** Automatic detection of text areas, lines, and paragraphs
- **Noise Reduction:** Built-in filters for image preprocessing

### Input Flexibility
- **Multiple Formats:** JPEG, PNG, GIF, BMP, TIFF
- **Batch Processing:** Process multiple images simultaneously
- **Remote Sources:** Recognize images from URLs
- **Archive Support:** Extract and process images from ZIP files

### Output Options
- **Text Extraction:** Plain text output
- **Structured Data:** JSON and XML formats
- **Document Formats:** DOCX, PDF, XLSX export
- **Detailed Results:** Character confidence scores and alternatives

## Common Use Cases

- **Document Digitization:** Convert scanned documents to searchable text
- **Data Extraction:** Extract information from forms and invoices
- **Content Analysis:** Analyze text content in images
- **Automation:** Integrate OCR into automated workflows
- **Multi-language Processing:** Handle documents in various languages

## Troubleshooting

### Common Issues
1. **Java Runtime Error:** Ensure JRE 8+ is installed and accessible
2. **Import Error:** Verify both `aspose-ocr-python-java` and `Jpype1` are installed
3. **Memory Issues:** Large images may require increased memory allocation

### Performance Tips
- Use appropriate image preprocessing filters for better accuracy
- Consider image resolution and quality for optimal results
- Batch process multiple images for efficiency

## Contributing

We welcome contributions! Please feel free to submit issues, feature requests, or pull requests.

## Support

- **Documentation:** [Aspose.OCR for Python via Java Documentation](https://docs.aspose.com/ocr/python-java/)
- **Forum:** [Aspose.OCR Forum](https://forum.aspose.com/c/ocr)
- **Examples:** [GitHub Examples Repository](https://github.com/aspose-ocr/Aspose.OCR-for-Python-via-Java)

## Additional Examples

### Multi-language Text Recognition

```python
import aspose as ocr

# Initialize OCR API
api = ocr.AsposeOcr()

# Set recognition settings for multiple languages
settings = ocr.RecognitionSettings()
settings.set_language(ocr.Language.AUTO) 

# Create input with settings
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add('Data/OCR/multilingual_text.png')

# Perform recognition
result = api.recognize(input, settings)
print("Recognized text:", result[0].recognition_text)
```

### Table Structure Recognition

```python
import aspose as ocr

# Initialize OCR API
api = ocr.AsposeOcr()

# Configure settings for table recognition
settings = ocr.RecognitionSettings()
settings.set_detect_areas_mode(ocr.DetectAreasMode.TABLE)

# Process table image
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)
input.add('Data/OCR/table.png')

# Recognize table structure
result = api.recognize(input, settings)

```

### Document Preprocessing with Filters

```python
import aspose as ocr

# Initialize OCR API
api = ocr.AsposeOcr()

# Create preprocessing filters
filters = ocr.PreprocessingFilter()
filters.add(ocr.PreprocessingFilter.auto_denoising())  # Remove noise
filters.add(ocr.PreprocessingFilter.contrast(10))      # Enhance contrast
filters.add(ocr.PreprocessingFilter.scale(1.5))        # Scale image

# Apply filters to input
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE, filters)
input.add('Data/OCR/low_quality_document.jpg')

# Recognize with enhanced preprocessing
result = api.recognize(input)
print("Enhanced recognition result:", result[0].recognition_text)
```

### Batch Processing with Progress Tracking

```python
import aspose as ocr
import os

# Initialize OCR API
api = ocr.AsposeOcr()

# Get all images from directory
image_dir = "Data/OCR/batch_images/"
image_files = [f for f in os.listdir(image_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Create input collection for batch processing
input = ocr.OcrInput(ocr.InputType.SINGLE_IMAGE)

# Add all images to the input collection
for i, image_file in enumerate(image_files, 1):
    print(f"Adding {i}/{len(image_files)}: {image_file}")
    input.add(os.path.join(image_dir, image_file))

# Process all images in batch
print("Processing images...")
result = api.recognize(input)

# Save results using the API's save method
# Save as plain text
result.save("batch_results.txt", ocr.Format.TEXT)

# Save as JSON format
result.save("batch_results.json", ocr.Format.JSON)

# Save as XML format  
result.save("batch_results.xml", ocr.Format.XML)

# Save as DOCX document
result.save("batch_results.docx", ocr.Format.DOCX)

# Save as PDF with original images as background
result.save_pdf("batch_results.pdf", "", ocr.PdfOptimizationMode.NONE)

print("Results saved in multiple formats:")
print("- batch_results.txt (plain text)")
print("- batch_results.json (JSON)")
print("- batch_results.xml (XML)")
print("- batch_results.docx (Word document)")
print("- batch_results.pdf (searchable PDF)")
```

## Supported Languages

Aspose.OCR for Python via Java supports 140+ languages based on Latin, Cyrillic, Asian, Arabic, and other scripts, including:

### Latin-based Languages
- **English (ENG)** - English alphabet
- **German (DEU)** - German alphabet
- **Portuguese (POR)** - Portuguese alphabet
- **Spanish (SPA)** - Spanish alphabet
- **French (FRA)** - French alphabet
- **Italian (ITA)** - Italian alphabet
- **Czech (CES)** - Czech alphabet
- **Danish (DAN)** - Danish alphabet
- **Dutch (NLD)** - Dutch alphabet
- **Estonian (EST)** - Estonian alphabet
- **Finnish (FIN)** - Finnish alphabet
- **Latvian (LAV)** - Latvian alphabet
- **Lithuanian (LIT)** - Lithuanian alphabet
- **Norwegian (NOR)** - Norwegian alphabet
- **Polish (POL)** - Polish alphabet
- **Romanian (RON)** - Romanian alphabet
- **Serbo-Croatian (HBS)** - Serbo-Croatian alphabet
- **Slovak (SLK)** - Slovak alphabet
- **Slovene (SLV)** - Slovene alphabet
- **Swedish (SWE)** - Swedish alphabet
- **Hungarian (HUN)** - Hungarian alphabet
- **Turkish (TUR)** - Turkish alphabet
- **Indonesian (IND)** - Indonesian alphabet
- **Vietnamese (VIE)** - Vietnamese alphabet
- **Catalan (CAT)** - Catalan alphabet
- **Afrikaans (AFR)** - Afrikaans alphabet
- **Albanian (ALN)** - Albanian alphabet
- **Galician (GLG)** - Galician alphabet
- **Low German (NDS)** - Low German alphabet

### Cyrillic-based Languages
- **Belorussian (BEL)** - Belorussian alphabet
- **Bulgarian (BUL)** - Bulgarian alphabet
- **Kazakh (KAZ)** - Kazakh alphabet
- **Russian (RUS)** - Russian alphabet
- **Serbian (SRP)** - Serbian alphabet
- **Ukrainian (UKR)** - Ukrainian alphabet
- **Bosnian (BOS)** - Bosnian alphabet
- **Croatian (HRV)** - Croatian alphabet
- **Chechen (CHE)** - Chechen alphabet
- **Kabardian (KBD)** - Kabardian alphabet

### Asian Languages
- **Chinese (CHINESE)** - Universal Chinese recognition
- **Mandarin (CMN)** - Mandarin Chinese alphabet
- **Cantonese (YUE)** - Cantonese alphabet
- **Min Nan (NAN)** - Min Nan alphabet
- **Hakka (HAK)** - Hakka alphabet
- **Gan (GAN)** - Gan alphabet
- **Min Bei (MNP)** - Min Bei alphabet
- **Min Dong (CDO)** - Min Dong alphabet
- **Pu-Xian (CPX)** - Pu-Xian alphabet
- **Korean (KOR)** - Korean alphabet
- **Japanese (JPN)** - Japanese alphabet
- **Vietnamese (VIE)** - Vietnamese alphabet

### Indic Languages
- **Hindi (HIN)** - Hindi alphabet
- **Marathi (MAR)** - Marathi alphabet
- **Bhojpuri (BHO)** - Bhojpuri alphabet
- **Maithili (MAI)** - Maithili alphabet
- **Awadhi (AWA)** - Awadhi alphabet
- **Magahi (MAG)** - Magahi alphabet
- **Haryanvi (BGC)** - Haryanvi alphabet
- **Chattisgarhi (HNE)** - Chattisgarhi alphabet
- **Dhundari (DHD)** - Dhundari alphabet
- **Kanauji (BJJ)** - Kanauji alphabet
- **Kumauni (KFY)** - Kumauni alphabet
- **Garhwali (GBM)** - Garhwali alphabet
- **Lamani (LMN)** - Lamani alphabet
- **Rajbanshi (RJB)** - Rajbanshi alphabet
- **Marwari (RWR)** - Marwari alphabet
- **Tamil (TAM)** - Tamil alphabet
- **Telugu (TEL)** - Telugu alphabet
- **Kannada (KAN)** - Kannada alphabet
- **Nepali (NEP)** - Nepali alphabet
- **Konkani (KNN)** - Konkani alphabet
- **Malayalam (MLY)** - Malay alphabet
- **Sundanese (SUN)** - Sundanese alphabet
- **Tagalog (TGL)** - Tagalog alphabet
- **Cebuano (CEB)** - Cebuano alphabet
- **Ilocano (ILO)** - Ilocano alphabet
- **Hiligaynon (HIL)** - Hiligaynon alphabet
- **Kapampangan (PAM)** - Kapampangan alphabet
- **Pangasinan (PAG)** - Pangasinan alphabet
- **Waray-Waray (WAR)** - Waray-Waray alphabet
- **Bikol (BCL)** - Bikol alphabet
- **Palembang (PLM)** - Palembang alphabet
- **Musi (MUI)** - Musi alphabet
- **Minangkabau (MIN)** - Minangkabau alphabet
- **Sasak (SAS)** - Sasak alphabet
- **Makassar (MAK)** - Makassar alphabet
- **Betawi (BEW)** - Betawi alphabet

### African Languages
- **Hausa (HAU)** - Hausa alphabet
- **Swahili (SWH)** - Swahili alphabet
- **Yoruba (YOR)** - Yoruba alphabet
- **Oromo (GAX)** - Oromo alphabet
- **Malagasy (BHR)** - Malagasy alphabet
- **Somali (SOM)** - Somali alphabet
- **Zulu (ZUL)** - Zulu alphabet
- **Xhosa (XHO)** - Xhosa alphabet
- **Tswana (TSN)** - Tswana alphabet
- **Sotho (SOT)** - Sotho alphabet
- **Ndebele (NBL)** - Ndebele alphabet
- **Swati (SSW)** - Swati alphabet
- **Tsonga (TSO)** - Tsonga alphabet
- **Venda (VND)** - Venda alphabet
- **Chichewa (NYA)** - Chichewa alphabet
- **Rwanda (KIN)** - Rwanda alphabet
- **Tumbuka (TUM)** - Tumbuka alphabet
- **Bemba (BEM)** - Bemba alphabet
- **Nandi (KLN)** - Nandi alphabet
- **Umbundu (UMB)** - Umbundu alphabet
- **Northern Sotho (NSO)** - Northern Sotho alphabet
- **Yao (YAO)** - Yao alphabet
- **Gusii (GUZ)** - Gusii alphabet
- **Meru (MER)** - Meru alphabet
- **Wolaytta (WAL)** - Wolaytta alphabet
- **Luo (LUO)** - Luo alphabet
- **Sukuma (SUK)** - Sukuma alphabet
- **Kikongo (KON)** - Kikongo alphabet
- **Makua (VMW)** - Makua alphabet
- **Kanuri (KNC)** - Kanuri alphabet
- **Serer-Sine (SRR)** - Serer-Sine alphabet
- **Tonga (TOI)** - Tonga alphabet
- **Luguru (RUF)** - Luguru alphabet
- **Shona (SNA)** - Shona alphabet
- **Mewati (WTM)** - Mewati alphabet

### Middle Eastern Languages
- **Arabic (ARA)** - Arabic alphabet
- **Persian (PES)** - Persian (Farsi) alphabet
- **Urdu (URD)** - Urdu alphabet
- **Uyghur (UIG)** - Uyghur alphabet
- **Kurdish (KMR)** - Kurdish (Kurmanji) alphabet
- **Azerbaijani (AZB)** - Azerbaijani (Azeri) alphabet
- **Turkmen (TUK)** - Turkmen alphabet
- **Gilaki (GLK)** - Gilaki alphabet
- **Dimli (DIQ)** - Dimli alphabet

### Other Languages
- **Mongolian (MON)** - Mongolian alphabet
- **Quechua (QXA)** - Quechua alphabet
- **Hmong (HMN)** - Hmong alphabet
- **Occitan (LNC)** - Occitan alphabet
- **Muong (MTQ)** - Muong alphabet
- **K'iche' (QUC)** - K'iche' alphabet
- **Malvi (MUP)** - Malvi alphabet
- **Mewari (MTR)** - Mewari alphabet
- **Wagdi (WBR)** - Wagdi alphabet
- **Dong (DOC)** - Dong alphabet
- **Bouyei (PCC)** - Bouyei alphabet
- **Zhuang (CCX)** - Zhuang alphabet
- **Tumbuka (TUM)** - Tumbuka alphabet
- **Chichewa (NYA)** - Chichewa alphabet
- **Rwanda (KIN)** - Rwanda alphabet
- **Zulu (ZUL)** - Zulu alphabet
- **Xhosa (XHO)** - Xhosa alphabet
- **Tswana (TSN)** - Tswana alphabet
- **Sotho (SOT)** - Sotho alphabet
- **Ndebele (NBL)** - Ndebele alphabet
- **Swati (SSW)** - Swati alphabet
- **Tsonga (TSO)** - Tsonga alphabet
- **Venda (VND)** - Venda alphabet
- **Bemba (BEM)** - Bemba alphabet
- **Nandi (KLN)** - Nandi alphabet
- **Umbundu (UMB)** - Umbundu alphabet
- **Northern Sotho (NSO)** - Northern Sotho alphabet
- **Yao (YAO)** - Yao alphabet
- **Gusii (GUZ)** - Gusii alphabet
- **Meru (MER)** - Meru alphabet
- **Wolaytta (WAL)** - Wolaytta alphabet
- **Luo (LUO)** - Luo alphabet
- **Sukuma (SUK)** - Sukuma alphabet
- **Kikongo (KON)** - Kikongo alphabet
- **Makua (VMW)** - Makua alphabet
- **Kanuri (KNC)** - Kanuri alphabet
- **Serer-Sine (SRR)** - Serer-Sine alphabet
- **Tonga (TOI)** - Tonga alphabet
- **Luguru (RUF)** - Luguru alphabet
- **Shona (SNA)** - Shona alphabet
- **Mewati (WTM)** - Mewati alphabet

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[Home](https://www.aspose.com/) | [Product Page](https://products.aspose.com/ocr/python-java) | [Docs](https://docs.aspose.com/ocr/python-java/) | [Demos](https://products.aspose.app/ocr/family) | [API Reference](https://apireference.aspose.com/ocr/python-java) | [Examples](https://github.com/aspose-ocr/Aspose.OCR-for-Python-via-Java) | [Blog](https://blog.aspose.com/category/ocr/) | [Search](https://search.aspose.com/) | [Free Support](https://forum.aspose.com/c/ocr) | [Temporary License](https://purchase.aspose.com/temporary-license)
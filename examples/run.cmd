python -m venv ./venv
call ./venv/Scripts/activate

REM /// download package aspose_ocr_python_java-23.12.0-py3-none-any.whl
pip install aspose_ocr_python_java-23.12.0-py3-none-any.whl
pip install Jpype1

python recognize.py
REM python calculate_skew.py
REM python image_text_finder.py
REM python recognize_and_save_result_as_file.py
REM python recognize_archive.py
REM python recognize_car_plate.py
REM python recognize_folder.py
REM python recognize_images_batch.py
REM python recognize_line.py
REM python recognize_passport.py
REM python recognize_street_photo.py
REM python recognize_table.py
REM python recognize_url.py
REM python recognize_with_detect_areas_mode.py
REM python recognize_with_language.py
REM python recognize_with_spell_check.py

pause()
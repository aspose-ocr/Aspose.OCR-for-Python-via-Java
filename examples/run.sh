
#sudo apt-get install openjdk-8-jre

python3 -m venv ./venv
source ./venv/Scripts/activate
pip install aspose-ocr-python-java
pip install Jpype1

python3 recognize.py
# python3 calculate_skew.py
# python3 image_text_finder.py
# python3 recognize_and_save_result_as_file.py
# python3 recognize_archive.py
# python3 recognize_car_plate.py
# python3 recognize_folder.py
# python3 recognize_images_batch.py
# python3 recognize_line.py
# python3 recognize_passport.py
# python3 recognize_street_photo.py
# python3 recognize_table.py
# python3 recognize_url.py
# python3 recognize_with_detect_areas_mode.py
# python3 recognize_with_language.py
# python3 recognize_with_spell_check.py

read -p "Press enter to continue"
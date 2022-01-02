import zipfile
import shutil

f1 = open('fileone.txt', 'w+')
f1.write('FILE NO. ONE')
f1.close()

f2 = open('filetwo.txt', 'w+')
f2.write('FILE NO. TWO')
f2.close()

comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

dir_to_zip = '/home/aditya/vicky/coding/python/python-jose/advanced-python-modules/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename,'zip',dir_to_zip)
shutil.unpack_archive('example.zip','final_unzip','zip')

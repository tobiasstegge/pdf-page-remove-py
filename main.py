from PyPDF2 import PdfFileWriter, PdfFileReader
import os

source_dir = '/Users/tobiassteggemann/Documents/thyssenkrupp/Upload Onepager'
destination_dir = '/Users/tobiassteggemann/Documents/thyssenkrupp/Upload Onepager/only_first_page'

if not os.path.exists(destination_dir):
    os.makedirs(destination_dir)


def delete_page(page):
    for filename in os.listdir(source_dir):
        if filename.endswith('.pdf'):
            print(filename)
            infile = PdfFileReader(os.path.join(source_dir, filename))
            output = PdfFileWriter()
            page_to_keep = infile.getPage(page)
            output.addPage(page_to_keep)

            with open(os.path.join(destination_dir, filename), 'wb') as file:
                output.write(file)


def rename_files():
    for filename in os.listdir(destination_dir):
        if filename.endswith('.pdf'):
            new_filename = filename.replace('One-Pager ', '')
            os.rename(os.path.join(destination_dir, filename), os.path.join(destination_dir, new_filename))


def check_if_complete():
    source_ids = [file.split(" ")[0] for file in os.listdir(source_dir) if file.split(" ")[0].isdigit()]
    destination_ids = [file.split(" ")[0] for file in os.listdir(destination_dir) if file.split(" ")[0].isdigit()]
    difference = set(source_ids).difference(destination_ids)

    if len(difference) > 0:
        print("These files were not edited and copied:")
        print(difference)
    else:
        print("All files copied successfully")


if __name__ == '__main__':
    delete_page(0)
    rename_files()
    check_if_complete()

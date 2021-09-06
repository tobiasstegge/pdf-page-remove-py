from PyPDF2 import PdfFileWriter, PdfFileReader
import os

workdir = '/Users/tobiassteggemann/Documents/thyssenkrupp/Upload Onepager'

if not os.path.exists(workdir + '/only_first_page'):
    os.makedirs(workdir + '/only_first_page')


def delete_page(page):
    for filename in os.listdir(workdir):
        if filename.endswith('.pdf'):
            print(filename)
            infile = PdfFileReader(os.path.join(workdir, filename))
            output = PdfFileWriter()
            page_to_keep = infile.getPage(page)
            output.addPage(page_to_keep)

            with open(workdir + '/only_first_page/' + filename, 'wb') as file:
                output.write(file)


if __name__ == '__main__':
    delete_page(0)

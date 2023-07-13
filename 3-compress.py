import os
from PIL import Image
import csv
import shutil

def compress_png(input_file_path, output_file_path):

    # Load the original PNG image
    img = Image.open(input_file_path)

    # Reduce the quality and save with different compression levels
    quality = 80  # starting quality
    while True:
        # Save the image with current quality level
        img.save(output_file_path, optimize=True, quality=quality)

        # Check the file size of the compressed image
        file_size = os.path.getsize(output_file_path) / 1024  # in kilobytes

        # If the file size is less than 100kb, break out of the loop
        if file_size < 100:
            break

        # If the file size is still too large, reduce the quality and try again
        quality -= 5

# def compress_pdf(input_file, output_file_path, power=4):

#     """Function to compress PDF via Ghostscript command line interface"""
#     try:
#         quality = {
#         0: '/default',
#         1: '/prepress',
#         2: '/printer',
#         3: '/ebook',
#         4: '/screen'
#         }
#         input_file = f'./{input_file}'
#         output_file_path = f'./{output_file_path}'
#         print("input_file: ",input_file,"output_file_path: ",output_file_path)
#         # Check if valid path o file is a PDF by extension
#         if not os.path.isfile(input_file) or input_file.split('.')[-1].lower() != 'pdf':
#         # self.logger.error(f'{uid} - Exception: invalid file path provided to pdf compressor', exc_info=True)
#             return None

#         output_filename = output_file_path#f'{uid}-result.pdf'
#         subprocess.call(["C:/Program Files/gs/gs10.01.1/bin/gswin64c.exe", '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
#                      '-dPDFSETTINGS={}'.format(quality[power]),
#                      '-dNOPAUSE', '-dQUIET', '-dBATCH',
#                      '-sOutputFile={}'.format(output_filename),input_file], shell=True)
#         with open(output_filename, "rb") as pdf_file:
#             return pdf_file.read()
#     except Exception as e:
#         print("error:",e)


from PIL import Image, ImageDraw, ImageFont
import os

def compress_tif(input_file_path, output_folder_path, i=0):

    image = Image.open(input_file_path)

 
    image = image.convert('RGB')
    # Save the TIFF file with LZW compression
    # image.save(output_path, compression='tiff_lzw')
    image.save(output_folder_path, format='JPEG', quality=50)
 
    # Close the image
    image.close()
    
    size_in_bytes = os.path.getsize(output_folder_path)

    print("size of output file", int(size_in_bytes/1024), i)

    if i<3:

        if int(size_in_bytes / 1024) > 100:

            i = i+1

            compress_tif(output_folder_path, output_folder_path, i)

        else:
            pass    
    else:
        pass





# def compress_tif(input_file_path, output_file_path):

#     # Open the TIFF file
#     image = Image.open(input_file_path)

#     # Set the quality factor for compression
#     quality = 50

#     # Save the compressed image in JPEG format with the given quality factor
#     image.save(output_file_path, 'TIFF', quality=quality, compression='tiff_deflate')

#     # Resize the compressed image if its size is still greater than 100 KB
#     while (os.stat(output_file_path).st_size / 1024) > 100:
#         width, height = image.size
#         new_width = int(width * 0.9)
#         new_height = int(height * 0.9)
#         image = image.resize((new_width, new_height), Image.ANTIALIAS)
#         image.save(output_file_path, 'TIFF', quality=quality, compression='tiff_deflate')


def compress_jpg(input_file_path, output_file_path):
    # input_file_path = 'input.jpg'
    # output_file_path = 'output.jpg'
    max_size_in_bytes = 100000

    # Open the input file
    with Image.open(input_file_path) as im:
        # Set the quality to reduce the size of the image
        quality = 95
        prev_value = 0
        # Reduce the quality until the image is under the specified size
        while True:
            # Save the image to the output file
            im.save(output_file_path, optimize=True, quality=quality)
            
            # Get the size of the output file
            output_size_in_bytes = os.path.getsize(output_file_path)
            print(output_size_in_bytes)


            if output_size_in_bytes == prev_value:
                print("Same value detected. Breaking out of the loop.")
                break
            
            prev_value = output_size_in_bytes

            # If the output file is under the specified size, break out of the loop
            if output_size_in_bytes < max_size_in_bytes:
                break
            
            # Decrease the quality and try again
            quality -= 5
            
    # Delete the input file
    # os.remove(input_file_path)

def main(input_folder_path, output_folder_path, failed_folder_path):
    
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
        print("Directory created successfully")
    else:
        print("Directory already exists")

    if not os.path.exists(failed_folder_path):
        os.makedirs(failed_folder_path)
        print("Directory created successfully")
    else:
        print("Directory already exists")

    with open('compression_failed.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        # Loop through all files in the folder
        for file_name in os.listdir(input_folder_path):
            size_in_bytes = os.path.getsize(input_folder_path + '/' + file_name)
            # Get the file extension

            # print(input_folder_path + '/' + file_name, size_in_bytes / 1024)        

            file_extension = os.path.splitext(file_name)[1]
            # print(file_extension)

            # Apply a condition based on the file extension
            if file_extension == ".tif" or file_extension == ".TIF":
                if int(size_in_bytes / 1024) > 100:
                # Do something with PDF files
                    try:
                        print("input and output file:",input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)

                        compress_tif(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)

                        size_in_bytes = os.path.getsize(output_folder_path + '/' + file_name)
                        if int(size_in_bytes / 1024) < 100:
                            pass
                        else:
                            writer.writerow([file_name, 'compression failed'])
                            shutil.copy(output_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)
                            os.remove(output_folder_path + '/' + file_name)

                    except Exception as e:
                        print(input_folder_path + '/' + file_name, e)
                        writer.writerow([file_name, 'compression failed'])
                        shutil.copy(input_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)
                else:
                    shutil.copy(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)
            

            # if file_extension == ".jpg" or '.jpeg':
            #     # Do something with text files
            #     try:
            #         compress_jpg(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)
            #     except Exception as e:
            #         print(input_folder_path + '/' + file_name, e)
            #         writer.writerow([file_name, 'compression failed'])
            #         shutil.copy(input_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)

            # if file_extension == ".png":
            #     # Do something with text files
            #     try:
            #         compress_jpg(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)
            #     except Exception as e:
            #         print(input_folder_path + '/' + file_name, e)
            #         writer.writerow([file_name, 'compression failed'])
            #         shutil.copy(input_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)

            # if file_extension == ".pdf":
            #     if size_in_bytes > 100*1024:
            #         print("pdf_file")
            #         try:
            #             # print("pdf")
            #             compress_pdf(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name, power=4)
            #         except Exception as e:
            #             print(input_folder_path + '/' + file_name, e)
            #             writer.writerow([file_name, 'compression failed'])
            #             shutil.copy(input_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)
            #     else:
            #         shutil.copy(input_folder_path + '/' + file_name, output_folder_path + '/' + file_name)
   

            # if file_extension != ".pdf" and file_extension != ".jpg" and file_extension != '.jpeg' and file_extension != '.png' and file_extension != '.tif':
            #     # Handle other file types or do nothing
            #     writer.writerow([file_name, 'invalid file type'])
            #     shutil.copy(input_folder_path + '/' + file_name, failed_folder_path + '/' + file_name)

if __name__ == '__main__':
    input_folder_path = "batch2-files"
    output_folder_path = 'batch2-files'
    failed_folder_path = 'batch4-failed'

    main(input_folder_path, output_folder_path, failed_folder_path)
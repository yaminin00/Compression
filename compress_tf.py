from PIL import Image
import io
im = Image.open("batch4-tif-images/Srishti_proof03023139.tif")
im = im.convert('YCbCr')
quality = 40
buffer = io.BytesIO()
im.save(buffer, format='TIFF', compression='jpeg', quality=quality)
with open("batch-compressed-tif-images/Srishti_proof03023139.tif", "wb") as f:
    f.write(buffer.getvalue())



# from PIL import Image
# import os
# def reduce_tif_size(input_path, output_path, quality=90):
#     with Image.open(input_path) as image:
#         original_format = image.format
#         if original_format == 'TIFF':
#             output_format = 'TIFF'
#         else:
#             output_format = 'JPEG'
#         options = {
#             'quality': quality,
#             'compress_level': 6,
#             'optimize': True
#         }
#         image.save(output_path, format=output_format, **options)
#     print(f"{os.path.basename(input_path)} successfully compressed and saved to {output_path}.")
# input_path = "batch4-tif-images/Ajitkumar_proof11745666.TIF"
# output_path = "batch4-compressed-tif-images/Ajitkumar_proof11745666.TIF"
# reduce_tif_size(input_path, output_path, quality=80)





# # Importing Image class from PIL module
# from PIL import Image
 
# # Opens a image in RGB mode
# im = Image.open('batch3-tif-images/HarshaVardhan_pan24034276.tif')
 
# # Size of the image in pixels (size of original image)
# # (This is not mandatory)
# width, height = im.size
 
# # Setting the points for cropped image
# # left = 4
# # top = height / 5
# # right = 154
# # bottom = 3 * height / 5
# # Cropped image of above dimension
# # (It will not change original image)
# # im1 = im.crop((left, top, right, bottom))
# newsize = (190,190)
# im1 = im.resize(newsize)
# # Shows the image in image viewer
# im1.save('batch3-compressed-tif-images/HarshaVardhan_pan24034276.tif')




# import os
# from PIL import Image
# import io

# input_folder = "batch4-tif-images"
# output_folder = "batch4-compressed-tif-images"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)

# for file_name in os.listdir(input_folder):
#     if file_name.endswith('.tif') or file_name.endswith('.tiff'):
#         input_path = os.path.join(input_folder, file_name)
#         output_path = os.path.join(output_folder, file_name)
#         with Image.open(input_path) as image:
#             image = image.convert('YCbCr')
#             quality = 60
#             buffer = io.BytesIO()
#             image.save(buffer, format='TIFF', compression='jpeg', quality=quality)
#             with open(output_path, "wb") as f:
#                 f.write(buffer.getvalue())
#          print(f"Compressed {input_path} and saved as {output_path}")






# import os
# from PIL import Image
# import io

# input_folder = "batch4-tif-images/Ajay_proof01841557.tif"
# output_folder = "batch-compressed-tif-images/Ajay_proof01841557.tif"

# if not os.path.exists(output_folder):
#     os.makedirs(output_folder)
# # loop through all tif files in the input folder
# for filename in os.listdir(input_folder):
#     if filename.endswith(".tif"):
#         input_path = os.path.join(input_folder, filename)
#         output_path = os.path.join(output_folder, filename)
        
#         # open the tif file, convert to YCbCr mode and compress
#         with Image.open(input_path) as image:
#             image = image.convert('YCbCr')
#             quality = 80
#             buffer = io.BytesIO()
#             image.save(buffer, format='TIFF', compression='jpeg', quality=quality)
            
#             # save the compressed image to the output folder if file size is below 100KB
#             if buffer.tell() < 100000:
#                 with open(output_path, "wb") as f:
#                     f.write(buffer.getvalue())
                    
#         print(f"{filename} processed.")





# import os
# from PIL import Image
# import io

# input_folder = "batch4-tif-images/Ajay_proof01841557.tif"
# output_folder = "batch-compressed-tif-images/Ajay_proof01841557.tif"

# for filename in os.listdir(input_folder):
#     if filename.endswith(".tif"):
#         input_path = os.path.join(input_folder, filename)
#         output_path = os.path.join(output_folder, filename)
        
#         with Image.open(input_path) as image:
#             image = image.convert('YCbCr')
#             buffer = io.BytesIO()
#             image.save(buffer, format='TIFF', compression='jpeg')
            
#             # Compress the image until the size is below 100KB
#             while buffer.tell() > 100000:
#                 quality = 5
#                 buffer = io.BytesIO()
#                 image.save(buffer, format='TIFF', compression='jpeg', quality=quality)
            
#             with open(output_path, "wb") as f:
#                 f.write(buffer.getvalue())

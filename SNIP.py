import PIL.Image as pilimg
import os
import tkinter.messagebox as msg
# Using Pillow and EasyTkinter

# making a new folder in the working directory
current_directory = os.getcwd()
folder_name = os.path.join(current_directory, r'cropped_images')
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
else:
    msg.showinfo("ERROR", "The folder 'cropped_images' already exists. Delete it and start this script again.")
    assert ()

# cropping every image
for file in os.listdir(current_directory):
    file_name = 'cropped_' + file
    print(file_name)
    if file.endswith('.jpg') or file.endswith('.JPG') or file.endswith('.PNG') or file.endswith('.png') or file.endswith('.jpeg') or file.endswith('.JPEG'):
        # img = Image.open(file).convert('RGB')
        img = pilimg.open(file).convert('RGB')
        w, h = img.size
        img_crop = img.crop((7, 170, w-10, h-35))
        # making a new folder with cropped files
        current_directory = os.path.join(folder_name, file_name)
        img_crop.save(current_directory)
    else:
        msg.showinfo("ERROR", "The %s file is not image file." % file_name)



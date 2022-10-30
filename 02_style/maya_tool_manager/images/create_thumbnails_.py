# python -m pip show pillow
# pip install pillow


# draw_text.py
import os
from PIL import Image, ImageDraw, ImageFont
# import maya.cmds as cmds

# maybe use __file__
SCRIPTS_DIR = 'C:/Users/Vaccari/Documents/maya/2022/scripts/'    # cmds.internalVar(usd=True)
MTM_DIR = SCRIPTS_DIR + 'maya_tool_manager'
IMAGES_DIR= MTM_DIR + '/images'
THUMBNAILS_DIR = IMAGES_DIR + '/thumbnails'

thumbnail_path = THUMBNAILS_DIR + '/test.png'
'''
def create_thumbnail(text, color, fill, output_path):
    
    #settings: image
    im_width  = 1024
    im_height = 1024
    # color     = (200, 45, 79) # use integer from 0 to 255 (not fractions of 255)
    mode      = 'RGB'
    
    # settings: text
    font      = 'arial.ttf'
    fontsize  = 200
    # text      = 'MTM'
    alignment = 'center'
    # fill      = 'white'

    image = Image.new(mode=mode, size=(im_width, im_height), color=color)
    draw  = ImageDraw.Draw(image)
    font_object  = ImageFont.truetype(font=font, size=fontsize)

    print('AAAAA')
    print(draw.textbbox((0,0), text))
    
    text_bbox = font_object.getbbox(text)
    # text_length = font_object.getlength(text))
    print(text_bbox)
    left, top, right, bottom = text_bbox
    font_width = right - top
    font_height = bottom - left
    new_width = (im_width - font_width) / 2
    new_height = (im_height - font_height) / 2
    
    text_xy = (new_width, new_height)
    draw.text(text_xy, text, font=font_object, align=alignment)
    image.save(output_path)


create_thumbnail('MTM', (200, 45, 79), 'white', thumbnail_path)


# FROM UI SCRIPT
# import os
# CREATE_THUMB_PATH = 'C:/Users/Vaccari/Documents/maya/2022/scripts/maya_tool_manager/images/create_thumbnails_.py'
# os.system('python ' + CREATE_THUMB_PATH)

'''






# import os
# import sys
# import subprocess as sp

# def access_pil_from_maya():
#     command = 'python -m pip show pillow'
#     output = sp.getoutput(command)
#     print(output)
#     print('222222')
#     first_split = output.split('Location: ', 1)
#     first_split = first_split[1]
#     print(first_split)
#     print(len(first_split))
#     print('222222')
#     second_split = first_split.split('Requires:', 1)
#     second_split = second_split[0]
#     third_split = second_split.split('\n')

#     PYTHON_SITE_PACKAGES_PATH = third_split[0]
#     PYTHON_SITE_PACKAGES_PATH.replace('c:', 'C:')
#     PIL1_PATH = PYTHON_SITE_PACKAGES_PATH + '\\PIL'
#     PIL2_PATH = PYTHON_SITE_PACKAGES_PATH + '\\Pillow-9.2.0.dist-info'
#     print(PIL1_PATH)
#     print(PIL2_PATH)
    

#     if PIL1_PATH not in sys.path:
#         sys.path.append(PIL1_PATH)

#     if PIL2_PATH not in sys.path:
#         sys.path.append(PIL2_PATH)

#     from PIL import Image, ImageDraw, ImageFont

# access_pil_from_maya()


def center_text(img, font, text, color=(255, 255, 255)):
    draw = ImageDraw.Draw(img)
    text_width, text_height = draw.textsize(text, font)
    position = ((strip_width-text_width)/2,(strip_height-text_height)/2)
    draw.text(position, text, color, font=font)
    return img

strip_width, strip_height = 1254, 2324
text = "Foooo Barrrr!!"

background = Image.new('RGB', (strip_width, strip_height)) #creating the black strip
font = ImageFont.truetype("times", 100)
center_text(background, font, "Foooo Barrrr!")
background.save(thumbnail_path)

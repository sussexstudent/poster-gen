from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

import random
import textwrap

from color_map import color_map

def generate_poster(poster_width, poster_height, bg_image, title,footer,background):

    poster = Image.new('RGB', (poster_width, poster_height), color = background)
    draw = ImageDraw.Draw(poster)

    if bg_image != None:
        rect_color = background
        text_color = color_map[background]

        bg_img = Image.open(bg_image, 'r')
        bg_img_w, bg_img_h = bg_img.size

        while bg_img_w < poster_width or bg_img_h < poster_height:
            bg_img = bg_img.resize((int(bg_img_w*1.5),int(bg_img_h*1.5)), resample = 0)
            bg_img_w, bg_img_h = bg_img.size

        offset = ((poster_width - bg_img_w) // 2, (poster_height - bg_img_h) // 2)
        poster.paste(bg_img,offset)
    
    else:
        rect_color = color_map[background]
        text_color = background

    title_font = ImageFont.truetype("./typeface.otf", 180)
    title_text_x = 120
    title_text_y = 180

    title_lines = (textwrap.fill(title,int(poster_width/100))).split('\n')

    for line in title_lines:
        text_length,text_height = title_font.getsize(line)
        line_num = title_lines.index(line)
        rect_co = [title_text_x-35,title_text_y-20+(line_num*185),title_text_x+40+text_length,title_text_y+190+(line_num*185)]
        draw.rectangle(rect_co,rect_color)
    
    for line in title_lines:
        line_num = title_lines.index(line)
        draw.text((title_text_x, title_text_y+(line_num*180)), line, text_color, font=title_font)
    
    #footer
    if footer != '':
        footer_text_x = title_text_x
        footer_text_y = poster_height - 300
        footer_font = ImageFont.truetype("./typeface.otf", 120)
        footer_lines = (textwrap.fill(footer,int((poster_width/100)*1.3))).split('\n')
        footer_lines.reverse()

        for line in footer_lines:
            text_length,text_height = footer_font.getsize(line)
            line_num = footer_lines.index(line)

            rect_co = [footer_text_x-20,footer_text_y+140-(line_num*125),footer_text_x+40+text_length,footer_text_y-(line_num*125)-30]

            draw.rectangle(rect_co,rect_color)

        for line in footer_lines:
            line_num = footer_lines.index(line)
            draw.text((footer_text_x, footer_text_y-(line_num*120)), line, text_color, font=footer_font)

    logo = Image.open("su_logo.png")
    logo = logo.convert("RGBA")
    logo_width, logo_height = logo.size
    logo = logo.resize((logo_width * 2 ,logo_height* 2),resample = 0)

    pixdata = logo.load()
    for y in range(logo.size[1]):
        for x in range(logo.size[0]):
            if pixdata[x,y][3] > 10:
                pixdata[x,y] = rect_color

    poster.paste(logo,(poster_width-400,poster_height-400),logo)

    return poster
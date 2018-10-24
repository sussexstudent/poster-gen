import img2pdf
from generation import generate_poster
from color_map import theme_map,color_map
from verify import verify_text

colors = list(theme_map.keys())
v_colors = list(theme_map.values())

poster_type = input('Baisc, Image or Everything: ')

if poster_type.lower() == 'everything':
    bg_image = input('Image File: ')
    poster_title = input('Title: ')
    poster_footer = input('Footer: ')

    posters = []

    for color in v_colors:
        posters.append(generate_poster(2480,3508,bg_image,poster_title,poster_footer,color))
    for color in v_colors:
        posters.append(generate_poster(3508,2480,bg_image,poster_title,poster_footer,color))
    for color in v_colors:
        posters.append(generate_poster(2480,3508,None,poster_title,poster_footer,color))
    for color in v_colors:
        posters.append(generate_poster(3508,2480,None,poster_title,poster_footer,color))

    for x in range(0,len(posters)):
        posters[x].save(f'Output/{poster_title}{x+1}.jpg')
        pdf_bytes = img2pdf.convert(f'Output/{poster_title}{x+1}.jpg')
        file = open(f'PDF/{poster_title}_{x+1}_{colors[x%5]}.pdf','wb')
        file.write(pdf_bytes)
        file.close()
        print(f'Successfully created {colors[x%5]} poster!')

else:
    if poster_type.lower() == 'image':
        bg_image = input('Image File: ')
    elif poster_type.lower() == 'basic':
        bg_image = None

    poster_orientation = input('Portrait or Landscape: ')
    if poster_orientation.lower() == 'portrait':
        poster_width,poster_height = 2480,3508
    elif poster_orientation.lower() == 'landscape':
        poster_width,poster_height = 3508,2480

    poster_title = input('Title: ')
    poster_footer = input('Footer: ')

    bg_color = input('Background Color: Yellow, Red, Blue, Green or Pink:')

    try:
        poster_color = theme_map[bg_color.lower()]
    except KeyError:
        print('Colour not recognised!')


    poster = generate_poster(poster_width,poster_height,bg_image,poster_title,poster_footer,poster_color)

    poster.save(f'Output/{poster_title}.jpg')
    pdf_bytes = img2pdf.convert(f'Output/{poster_title}.jpg')
    file = open(f'PDF/{poster_title}.pdf','wb')
    file.write(pdf_bytes)
    file.close()
    print('Successfully created')

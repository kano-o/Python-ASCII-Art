from PIL import Image
#insert file name in this string
picture_name = 'typing-man-typing.gif'
im = Image.open(picture_name)


print('Successfully loaded image!')

rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

hgt = im.height
wdh = im.width

pixel_matrix = [[0 for x in range(wdh)] for y in range(hgt)] 

for w in range(wdh):
    for h in range(hgt):
        r, g, b = rgb_im.getpixel((w, h))
        pixel_matrix[h][w] = (r, g, b)

#print(pixel_matrix)

print('Pixel matrix size:', len(pixel_matrix), 'x', len(pixel_matrix[0]))

brightness_matrix = [[0 for x in range(wdh)] for y in range(hgt)] 

for w in range(wdh):
    for h in range(hgt):
        r, g, b = pixel_matrix[h][w]
        brightness = (r + g + b) / 3
        pixel_matrix[h][w] = round(brightness)

#64 chars
raw_chars = r'`^",:;Il!i~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$'


for w in range(wdh):
    for h in range(hgt):
        brightness = pixel_matrix[h][w]
        ratio = 256 / len(raw_chars)
        index = brightness / ratio
        
        pixel_matrix[h][w] = raw_chars[int(index)]

output = ''

for x in range(len(pixel_matrix)):
    output += '\n'
    for y in range(len(pixel_matrix[x])):
        pixel = pixel_matrix[x][y]
        output += pixel
              
open(picture_name + '.txt', 'x')
with open(picture_name + '.txt', 'w') as text_file:
    text_file.write(output)
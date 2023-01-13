from PIL import Image
im = Image.open('ascii-pineapple.jpg')

print('Successfully loaded image!')

rgb_im = im.convert('RGB')
r, g, b = rgb_im.getpixel((1, 1))

hgt = im.height
wdh = im.width

pixel_matrix = [[0 for y in range(hgt)] for x in range(wdh)] 

for h in range(hgt):
    for w in range(wdh):
        r, g, b = rgb_im.getpixel((w, h))
        pixel_matrix[w][h] = (r, g, b)

#print(pixel_matrix)

print('Pixel matrix size:', len(pixel_matrix), 'x', len(pixel_matrix[0]))
print('Iterating through pixel contents:')


for x in range(len(pixel_matrix)):
    for y in range(len(pixel_matrix[x])):
        pixel = pixel_matrix[x][y]
        print(pixel)

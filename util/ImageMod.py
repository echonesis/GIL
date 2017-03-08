from PIL import Image
import sys

def ChangeOpacity(img, transparency=None):
    img = img.convert("RGBA")
    data = img.load()
    w, h = img.size

    for y in xrange(h):
        for x in xrange(w):
            (r_pix, g_pix, b_pix, alpha) =  data[x, y]
            if transparency is None:
                data[x, y] = (r_pix, g_pix, b_pix, 100)
            else:
                data[x, y] = (r_pix, g_pix, b_pix, transparency)

    return img

if __name__ == '__main__':
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]

    img = Image.open(inputFile)
    img2 = ChangeOpacity(img)

    img2.save(outputFile)

from PIL import Image, ImageDraw
import math

def Draw(imgStr, dim=None):
    if dim is None:
        nRow = int(math.sqrt(len(imgStr)))
        nCol = nRow

    else:
        nRow = int(dim[0])
        nCol = int(dim[1])

    
    imgDim = (nRow, nCol)
    img = Image.new('RGBA', imgDim, (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    for i in xrange(len(imgStr)):
        y = i % nRow
        x = i // nRow
        if imgStr[i] == '1':
            draw.point((x, y), fill=(0, 0, 0, 0))

    return img

if __name__ == '__main__':
    testStr = '0000100011001110111111111'
    result = Draw(testStr)
    result.show()

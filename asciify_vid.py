from PIL import Image, ImageDraw, ImageFont
import cv2
import os
import math
def asciify_img():
    # chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]
    # chars = "Ñ@#W$9876543210?!abc;:+=-,._ "[::-1]
    chars = "#Wo- "[::-1]
    charArray = list(chars)
    charLength = len(charArray)
    interval = charLength/256
    scale_factor=0.7
    def getChar(inputInt):
        return charArray[math.floor(inputInt*interval)]

    im = Image.open('frame_in.jpg')    
    fnt = ImageFont.truetype('segoepr.ttf', 15)
    width, height = im.size
    # text_file = open("Output.txt", "w")
    im = im.resize((int(scale_factor*width), int(scale_factor*height*(2/3))), Image.NEAREST)
    width, height = im.size
    pix = im.load()
    outputImage = Image.new('RGB', (int(6 * width), int(9 * height)), color = (0, 0, 0))
    d = ImageDraw.Draw(outputImage)
    for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int(r/3 + g/3 + b/3)
                pix[j, i] = (h, h, h)
                # text_file.write(getChar(h))
                d.text((j*6, i*9), getChar(h), font = fnt, fill = (r, g, b))

            # text_file.write('\n')

    outputImage.save('frame_out.jpg')

def asc_vid():
    vidcap=cv2.VideoCapture('video.mp4')
    success,image=vidcap.read()
    cv2.imwrite('frame_in.jpg',image)
    while os.path.exists('frame_in.jpg')==False:
        vidcap=cv2.VideoCapture('video.mp4')
        success,image=vidcap.read()
        cv2.imwrite('frame_in.jpg',image)
    count=1
    asciify_img()
    imo =Image.open('frame_out.jpg')
    width,height=imo.size
    size =(width,height)
    out = cv2.VideoWriter('result.mp4',cv2.VideoWriter_fourcc(*'mp4v'),15,size )
    ascfrm=cv2.imread('frame_out.jpg')
    out.write(ascfrm)
    while success:
        print("Frame no = %d"%count)
        success,image=vidcap.read()
        if image is None:
            break
        cv2.imwrite('frame_in.jpg',image)
        asciify_img()
        ascfrm=cv2.imread('frame_out.jpg')
        out.write(ascfrm)
        count+=1

    out.release()

if __name__=='__main__':
    # asciify_img()
    asc_vid()

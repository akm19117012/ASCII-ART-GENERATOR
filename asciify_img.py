import numpy as np
# import pandas
import cv2
from numpy.ma.core import zeros, indices


class ASCIIFY_IMG:
    chars=None
    charArray=[]
    charLength = 0
    interval=0
    scaleFactor=0

    @classmethod
    def __setVariable__(cls):
        print('Setting ASCIIFY_IMG variables')
        ASCIIFY_IMG.chars = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,"^`\'.'''[::-1]
        ASCIIFY_IMG.charArray = list(ASCIIFY_IMG.chars)
        ASCIIFY_IMG.charLength = len(ASCIIFY_IMG.charArray)
        ASCIIFY_IMG.interval = ASCIIFY_IMG.charLength / 256
        ASCIIFY_IMG.scaleFactor = 0.05
        print(f'Scale Factor: {ASCIIFY_IMG.scaleFactor}')
        print(f'Characters: {ASCIIFY_IMG.chars}')

    @classmethod
    def __getChar(cls,val):
        if ASCIIFY_IMG.charLength==0:
            ASCIIFY_IMG.__setVariable__()

        idx = int(val * ASCIIFY_IMG.interval)
        if idx >= ASCIIFY_IMG.charLength:
            idx = ASCIIFY_IMG.charLength - 1
        return ASCIIFY_IMG.charArray[idx]



    def __init__(self, arg):

        self.src_ndarr: np.ndarray =None
        self.res_ndarr: np.ndarray = None
        if ASCIIFY_IMG.chars is None:
            ASCIIFY_IMG.__setVariable__()

        if type(arg) is str:
            try:
                self.src_ndarr = cv2.imread(arg, cv2.IMREAD_COLOR)
            except Exception as e:
                raise e
        elif type(arg) is np.ndarray:
            self.src_ndarr = arg
        else:
            raise TypeError("Invalid argument type, must be str or numpy.ndarray")

    def asciify(self, recalculate=False) -> np.ndarray:

        if self.res_ndarr is not None and not recalculate:

            return self.res_ndarr
        h, w, c = self.src_ndarr.shape

        new_h,new_w=int(h*ASCIIFY_IMG.scaleFactor),int(w*ASCIIFY_IMG.scaleFactor)
        step_x,step_y=h/new_h,w/new_w
        indices_x=[int(i*step_x) for i in range(new_h)]
        indices_y=[int(i*step_y) for i in range(new_w)]
        img_small=np.zeros((new_h,new_w,3),dtype=np.uint8)
        x=int(0)
        for i in indices_x:
            y=int(0)
            for j in indices_y:
                img_small[x,y]=self.src_ndarr[i,j]
                y+=1
            x+=1


        gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)

        out_h = new_h * 9
        out_w = new_w * 6
        self.res_ndarr = np.zeros( (out_h, out_w, 3), dtype=np.uint8)

        for i in range(new_h):
            for j in range(new_w):
                pixel_val = gray[i, j]
                char = ASCIIFY_IMG.__getChar(pixel_val)

                color = img_small[i, j].tolist()
                cv2.putText(self.res_ndarr,char,(j * 6, i * 9),cv2.FONT_HERSHEY_SIMPLEX,0.3,color,1,cv2.LINE_AA)
        print(self.res_ndarr)
        return self.res_ndarr

    def asciify_img(self) -> np.ndarray:
        """
        Input:  img (H x W x 3) numpy array (BGR format if from cv2)
        Output: ASCII rendered image as numpy array
        """

        # Character set
        chars = "#Wo- "[::-1]
        charArray = list(chars)
        charLength = len(charArray)
        interval = charLength / 256

        def getChar(val):
            idx = int(val * interval)
            if idx >= charLength:
                idx = charLength - 1
            return charArray[idx]

        scale_factor = 0.7

        h, w = self.src_ndarr.shape[:2]

        # Resize (equivalent to PIL NEAREST)
        new_w = int(scale_factor * w)
        new_h = int(scale_factor * h * (2 / 3))
        img_small = cv2.resize(self.src_ndarr, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

        # Convert to grayscale
        gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)

        # Create output canvas
        out_h = new_h * 9
        out_w = new_w * 6
        self.res_ndarr = np.zeros((out_h, out_w, 3), dtype=np.uint8)

        # Draw ASCII characters
        for i in range(new_h):
            for j in range(new_w):
                pixel_val = gray[i, j]
                char = getChar(pixel_val)

                color = img_small[i, j].tolist()

                cv2.putText(
                    self.res_ndarr,
                    char,
                    (j * 6, i * 9),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.3,
                    color,
                    1,
                    cv2.LINE_AA
                )

        return self.res_ndarr

    def asciify_img_url(self,):
        pass

    def asciify_img_dir(self,dirpath='./assets/downloads'):
        pass

    # def asciify_img_batch():

    def show(self):
        cv2.imshow("Input", self.src_ndarr)
        cv2.imshow("Output", self.res_ndarr)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def save(self, path='output.jpg'):
        cv2.imwrite(path, self.res_ndarr)


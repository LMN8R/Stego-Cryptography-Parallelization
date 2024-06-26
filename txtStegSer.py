
import os
import random

from PIL import Image
import time
import matplotlib.pyplot as plt

# Convert encoding data into 8-bit binary
# form using ASCII value of characters
from numpy import double


def genData(data):
    # list of binary codes
    # of given data
    newd = []

    for i in data:
        newd.append(format(ord(i), '08b'))
    return newd


# Pixels are modified according to the
# 8-bit binary data and finally returned
def modPix(pix, data):
    datalist = genData(data)
    lendata = len(datalist)
    imdata = iter(pix)

    for i in range(lendata):

        # Extracting 3 pixels at a time
        pix = [value for value in imdata.__next__()[:3] +
               imdata.__next__()[:3] +
               imdata.__next__()[:3]]

        # Pixel value should be made
        # odd for 1 and even for 0
        for j in range(0, 8):
            if (datalist[i][j] == '0' and pix[j] % 2 != 0):
                pix[j] -= 1

            elif (datalist[i][j] == '1' and pix[j] % 2 == 0):
                if (pix[j] != 0):
                    pix[j] -= 1
                else:
                    pix[j] += 1
            # pix[j] -= 1

        # Eighth pixel of every set tells
        # whether to stop ot read further.
        # 0 means keep reading; 1 means thec
        # message is over.
        if (i == lendata - 1):
            if (pix[-1] % 2 == 0):
                if (pix[-1] != 0):
                    pix[-1] -= 1
                else:
                    pix[-1] += 1

        else:
            if (pix[-1] % 2 != 0):
                pix[-1] -= 1

        pix = tuple(pix)
        yield pix[0:3]
        yield pix[3:6]
        yield pix[6:9]


def encode_enc(newimg, data):
    w = newimg.size[0]
    (x, y) = (0, 0)

    for pixel in modPix(newimg.getdata(), data):

        # Putting modified pixels in the new image
        newimg.putpixel((x, y), pixel)
        if (x == w - 1):
            x = 0
            y += 1
        else:
            x += 1


# Encode data into image
def encode(image1, datatxt):

    if not os.path.isfile(image1):
        try:
            time.sleep(random.randint(1))
        except:
            raise ValueError('Image Does not exist')
            quit()

    img = image1
    image = Image.open(img, 'r')

    data = datatxt
    if (len(data) == 0):
        raise ValueError('Data is empty')

    newimg = image.copy()
    encode_enc(newimg, data)

    return newimg


# Decode the data in the image
def decode(image1):

    if not os.path.isfile(image1):
        try:
            time.sleep(random.randint(1))
        except:
            raise ValueError('Image Does not exist')
            quit()


    img = image1
    image = Image.open(img, 'r')

    data = ''
    imgdata = iter(image.getdata())

    while (True):
        pixels = [value for value in imgdata.__next__()[:3] +
                  imgdata.__next__()[:3] +
                  imgdata.__next__()[:3]]

        # string of binary data
        binstr = ''

        for i in pixels[:8]:
            if (i % 2 == 0):
                binstr += '0'
            else:
                binstr += '1'

        data += chr(int(binstr, 2))
        if (pixels[-1] % 2 != 0):
            return data


# Main Function
def main():
    a = int(input(":: Welcome to Text Steganography ::\n"
                  "1. Encode\n2. Decode\n"))
    if (a == 1):

        plt.axis([0, 16, 0, 0.05])
        mapp = []
        lss = []
        timesumserial = 0
        stg = ''
        for i in range(15):
            img2 = 'small/s' + str(i + 1) + '.png'
            stg += str(i + 1)
            output = 'textserout/ts' + str(
                i + 1) + '.png'

            start = time.time()
            merged_image = encode(img2, stg)
            merged_image.save(output)
            end = time.time()

            timesumserial += end - start
            lss.append(timesumserial)

            mapp.append(end - start)

        # print(mapp)
        gg = "Total Serial Text Encoding Time 15 img " + str(timesumserial)
        print(" Serial Encoding process ended")
        plt.xlabel('Number of images')
        plt.ylabel('Serial Time')
        plt.title(gg)

        for i in range(1, len(mapp) + 1):
            format_float = "{:.2f}".format(mapp[i - 1])
            plt.text(i, mapp[i - 1], '({}, {})'.format(i, str(format_float)))
            plt.scatter(i, mapp[i - 1])
            plt.pause(0.5)

        plt.show()




    elif (a == 2):
        plt.axis([0, 16, 0, 0.05])
        mapp = []
        lss = []
        timesumserial = 0
        file1 = open("textdecodeser.txt", "w")
        for i in range(15):
            output = 'textserout/ts' + str(
                i + 1) + '.png'

            start = time.time()
            unmerged_text = decode(output)
            lss.append(unmerged_text + "\n")

            end = time.time()

            timesumserial += end - start

            mapp.append(end - start)

        # print(mapp)
        file1.writelines(lss)
        file1.close()
        gg = "Total Serial Text Decoding Time 15 imgs " + str(timesumserial)
        print(" Serial decoding process ended")
        plt.xlabel('Number of images')
        plt.ylabel('Serial Time')
        plt.title(gg)

        for i in range(1, len(mapp) + 1):
            format_float = "{:.5f}".format(mapp[i - 1])
            plt.text(i, mapp[i - 1], '({}, {})'.format(i, str(format_float)))
            plt.scatter(i, mapp[i - 1])
            plt.pause(0.5)
        plt.show()



    else:
        raise Exception("Enter correct input")


# Driver Code
if __name__ == '__main__':
    # Calling main function
    main()

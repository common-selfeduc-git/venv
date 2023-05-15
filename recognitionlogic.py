import matplotlib.pyplot as plt
import pytesseract
import cv2
import pathlib

class recognitor:
    pytesseract.pytesseract.tesseract_cmd = 'E:/Tesseract-OCR/tesseract.exe'
    p=pathlib.Path(r'cars\polo_dirty.jpg')
    cascade_path=pathlib.Path(r'E:\UNIVERSITY\VKR\CarNumberRecognizer\CarNumberRecognizer\PyModule\haarcascade_russian_plate_number\haarcascade_russian_plate_number.xml')
    def open_img(img_path):
        carplate_img = cv2.imread(img_path)
        carplate_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2RGB)
        plt.axis('off')
        plt.imshow(carplate_img)
        plt.show()
        return carplate_img

    def carplate_extract(image, carplate_haar_cascade):
        carplate_rects = carplate_haar_cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5)

        for x, y, w, h in carplate_rects:
            carplate_img = image[y+15:y+h-15, x+25:x+w-15]
        
        return carplate_img

    def enlarge_img(image, scale_percent):
        width = int(image.shape[1]  * scale_percent / 100)
        height = int(image.shape[0]  * scale_percent / 100)
        dim = (width, height)
        plt.axis('off')
        resized_image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

        return resized_image

    def recognize():
        carplate_img_rgb = recognitor.open_img(img_path=str(recognitor.p))
        carplate_haar_cascade = cv2.CascadeClassifier(str(recognitor.cascade_path))

        carplate_extract_img = recognitor.carplate_extract(carplate_img_rgb, carplate_haar_cascade)
        carplate_extract_img = recognitor.enlarge_img(carplate_extract_img, 150)
        plt.imshow(carplate_extract_img)
        #plt.show()

        carplate_extract_img_gray = cv2.cvtColor(carplate_extract_img, cv2.COLOR_RGB2GRAY)
        plt.axis('off')
        plt.imshow(carplate_extract_img_gray, cmap='gray')
        plt.show()

        print('Номер авто: ', pytesseract.image_to_string(
            carplate_extract_img_gray,
            config='--psm 6 --oem 3 -c tessedit_char_whitelist=ABCEHKMOPTXY0123456789'
        ))

if __name__ == '__main__':
    recognitor.recognize()
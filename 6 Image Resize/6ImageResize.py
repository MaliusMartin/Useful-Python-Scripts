import cv2

def resize_image(image, width, height, save_path=None):
    resized_image = cv2.resize(image, (width, height))
    if save_path:
        cv2.imwrite(save_path, resized_image)
    return resized_image


image_path = '2.jpg'
image = cv2.imread(image_path)


resized_image_path = 'resized_2.jpg'
resized_image = resize_image(image, 640, 640, resized_image_path)

cv2.imshow('Resized Image', resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()

import cv2

def image_display_example(img_path):
    """
    Example function to display an image

    img_path: path of image to display
    """
    img = cv2.imread(img_path, 1)

    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.imshow('image',img)
    keyPress = cv2.waitKey(0)

    if keyPress == 27:
        cv2.destroyAllWindows()


def image_scale_down_example(img_path):
    """
    Example to scale down image to process faster
    """

    img = cv2.imread(img_path, 1)

    scale_factor = 0.1
    new_height = int(len(img)*scale_factor)
    new_width = int(len(img[0])*scale_factor)

    img = cv2.resize(img, (new_height, new_width))

    cv2.imshow('scaled_down', img)
    cv2.waitKey(0)
    if keyPress == 27:
        cv2.destroyAllWindows()

image_scale_down_example('example.jpg')

def image_transform_example(img_path):
    """
    Example function to transform into image using an energy function.

    Energy function used:

    delta_x = sum of sqaured difference between rgb wise intensities, between (left,right pixel)
    delta_y = sum of sqaured difference between rgb wise intensities, between (top_bot pixel)

    func = delta_x + delta_y
    """


# image_transform_example('example.jpg')

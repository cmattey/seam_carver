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

def image_transform_example(img_path):
    """
    Example function to transform into image using an energy function.

    Energy function used:

    delta_x = sum of sqaured difference between rgb wise intensities, between (left,right pixel)
    delta_y = sum of sqaured difference between rgb wise intensities, between (top_bot pixel)

    func = delta_x + delta_y
    """

    

image_display_example('example.jpg')

import cv2

def get_filtered_image(image):
    opencv_color_model = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    resulting_image = cv2.cvtColor(opencv_color_model, cv2.COLOR_BGR2GRAY)
    return resulting_image
import cv2

def get_filtered_image(image, action):
    opencv_color_model = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    if action == 'NO_FILTER':
        resulting_image = opencv_color_model
    elif action == 'GRAYSCALE':
        resulting_image = cv2.cvtColor(opencv_color_model, cv2.COLOR_BGR2GRAY)
    return resulting_image
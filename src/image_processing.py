def apply_filter(image, filter_type):
    if filter_type == 'grayscale':
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    elif filter_type == 'blur':
        return cv2.GaussianBlur(image, (5, 5), 0)
    elif filter_type == 'edge':
        return cv2.Canny(image, 100, 200)
    else:
        return image

def adjust_brightness(image, brightness_factor):
    return cv2.convertScaleAbs(image, alpha=1, beta=brightness_factor)
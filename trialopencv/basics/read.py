import cv2 as cv

   
def resizeFrame(frame, scale=0.75):
    width = frame.shape[1] * scale
    height = frame.shape[0] * scale
    
    dimensions = [width, height]
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)


def changeRes(height, width):
    
    capture.set(3, width) #3 refers to the width (properties of the class)
    capture.set(4, height) #4 refers to the width (properties of the class)

# Read an image

img = cv.imread('/Users/aaditya/Desktop/trialopencv/24.png')

# cv.imshow('Background', img)

cv.waitKey(0) 


img_resize = resizeFrame(img)

cv.imshow('resized_background', img_resize) 


# Read a video 

# capture = cv.VideoCapture('/Users/aaditya/Desktop/trialopencv/speech.mp4')

# while True:
#     isTrue, frame = capture.read()
#     cv.imshow('speech Video', frame)
    
#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
    
    

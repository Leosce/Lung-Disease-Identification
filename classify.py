import numpy as np
import cv2
def classify(image, model):
    image = np.array(image) 
    if len(image.shape)==3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.resize(image, (224,224))
    image = np.expand_dims(image,0)
    image = image/255.0
    
    yhat_test = model.predict(image)
    pred_class = np.argmax(yhat_test, axis=1)
    
    return yhat_test, pred_class
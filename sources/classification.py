import numpy as np
from PIL import Image
import tensorflow as tf

class Classifier:
    def __init__(self, model_path, labels):
        self.labels = labels

        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()

        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

        self.height = self.input_details[0]['shape'][1]
        self.width = self.input_details[0]['shape'][2]

    def preprocess(self, img):
        img = img.resize((self.width, self.height))
        img = np.array(img).astype(np.float32)

        img = (img / 127.5) - 1.0

        return np.expand_dims(img, axis=0)

    def predict(self, picture):
        img = picture.img

        input_data = self.preprocess(img)

        self.interpreter.set_tensor(self.input_details[0]['index'], input_data)
        self.interpreter.invoke()

        output = self.interpreter.get_tensor(self.output_details[0]['index'])[0]

        pred_index = int(np.argmax(output))

        return pred_index == 0

classi = Classifier("data/mobilenet_v1_1.0_224_quant.tflite", [
    "A nutria",
    "An animal",
    "An empty cage",
    "A cat",
    "A rabbit",
    "A dog",
    "A mouse",
    "A rat"
])
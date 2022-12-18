# Vision-Sehyog

Vision-Sehyog is a powerful and innovative application that uses the latest technologies in computer vision and text-to-speech to assist the visually impaired. The use of the React.js framework and YOLO model allows the application to run smoothly and accurately detect objects in real-time using a webcam. The text-to-speech feature is a valuable addition that helps those with visual impairments to understand and interact with their surroundings. Overall, Vision-Sehyog is a valuable tool that enhances accessibility and improves the lives of those with visual impairments

## Important Links
- [Demo Video]()
- [Presentation]()
- [Download Model Weights]()


## Deep-Learning model - YOLO v5
YOLO (You Only Look Once) is a popular real-time object detection algorithm developed by Joseph Redmon and Ali Farhadi. It uses a single neural network to predict bounding boxes and class probabilities directly from full images in one forward pass. This makes it much faster and more efficient than other object detection algorithms that require multiple passes or separate components for detection and classification.
One of the key features of YOLO is that it can process images in real-time, making it suitable for applications that require fast object detection, such as video surveillance and self-driving cars. YOLO also achieves high accuracy on a variety of object detection benchmarks and has been widely adopted in a variety of applications. The YOLO architecture consists of a convolutional neural network (CNN) that processes an input image and predicts the location and class of objects within the image.
The YOLO architecture has several key features that contribute to its efficiency and performance:
- Single-shot detection: YOLO processes the entire image in a single forward pass of the CNN, making it much faster than traditional object detection algorithms that require multiple forward and backward passes.

- Predicts bounding boxes directly: Unlike other object detection algorithms that first detect candidate regions and then classify them, YOLO predicts bounding boxes and class probabilities directly from the input image. This eliminates the need for separate region proposal and classification stages.

- Grid-based prediction: YOLO divides the input image into a grid of cells, and each cell predicts a set of bounding boxes and class probabilities. This allows YOLO to handle objects of different sizes and aspect ratios effectively.

- Anchor boxes: YOLO uses anchor boxes to handle objects of different shapes and sizes. Anchor boxes are predefined bounding boxes that are used as references to predict the locations and sizes of objects in the image.

Overall, the YOLO architecture is a fast and effective solution for object detection tasks, and has been widely adopted in a variety of applications

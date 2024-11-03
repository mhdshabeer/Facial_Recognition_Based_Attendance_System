import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread

def load_images_and_labels(folder_path):
    """
    Load images and their corresponding IDs from the specified folder.
    """
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    # Initialize empty lists for faces and IDs
    faces = []
    ids = []

    # Loop through all image paths to load images and extract IDs
    for image_path in image_paths:
        # Load the image and convert it to grayscale
        pil_image = Image.open(image_path).convert('L')
        image_np = np.array(pil_image, 'uint8')

        # Extract ID from the image filename
        image_id = int(os.path.split(image_path)[-1].split(".")[1])

        # Append the face and ID to their respective lists
        faces.append(image_np)
        ids.append(image_id)

    return faces, ids


def train_face_recognizer():
    """
    Train the LBPH face recognizer using images from the 'TrainingImage' folder.
    """
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    haarcascade_path = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(haarcascade_path)

    # Load images and labels
    faces, ids = load_images_and_labels("TrainingImage")

    # Start a thread for training the recognizer
    Thread(target=recognizer.train, args=(faces, np.array(ids))).start()

    # Start a thread for the image counter display
    Thread(target=display_image_count, args=("TrainingImage",)).start()

    # Save the trained model
    recognizer.save(os.path.join("TrainingImageLabel", "Trainner.yml"))
    print("Training complete for all images.")


def display_image_count(folder_path):
    """
    Display the count of images being trained in the console.
    """
    img_counter = 1
    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path)]

    for _ in image_paths:
        print(f"{img_counter} Images Trained", end="\r")
        time.sleep(0.008)
        img_counter += 1

# Example usage (Uncomment to use)
# if __name__ == "__main__":
#     train_face_recognizer()

import csv
import cv2
import os

def is_number(s):
    """Check if the input is a number."""
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def take_images():
    """Capture images from webcam and save them with corresponding IDs and names."""
    user_id = input("Enter Your ID: ")
    name = input("Enter Your Name: ")

    if is_number(user_id) and name.isalpha():
        cam = cv2.VideoCapture(0)
        haarcascade_path = "haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(haarcascade_path)
        sample_num = 0

        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
                sample_num += 1
                cv2.imwrite(os.path.join("TrainingImage", f"{name}.{user_id}.{sample_num}.jpg"), gray[y:y + h, x:x + w])
                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q') or sample_num > 100:
                break

        cam.release()
        cv2.destroyAllWindows()

        # Save student details to CSV
        save_student_details(user_id, name)
    else:
        if is_number(user_id):
            print("Please enter an alphabetical name.")
        if name.isalpha():
            print("Please enter a numeric ID.")

def save_student_details(user_id, name):
    """Save student ID and name to a CSV file."""
    header = ["ID", "Name"]
    row = [user_id, name]
    file_path = os.path.join("StudentDetails", "StudentDetails.csv")

    if os.path.isfile(file_path):
        with open(file_path, 'a+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(row)
    else:
        with open(file_path, 'w+', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(header)
            writer.writerow(row)

# Example usage (Uncomment to use)
# if __name__ == "__main__":
#     take_images()

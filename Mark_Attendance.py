import datetime
import os
import time
import cv2
import pandas as pd


def recognize_attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("./TrainingImageLabel/Trainner.yml")
    cascade_path = "haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(cascade_path)
    student_data = pd.read_csv("StudentDetails" + os.sep + "StudentDetails.csv")
    font_style = cv2.FONT_HERSHEY_SIMPLEX
    attendance_columns = ['Id', 'Name', 'Date', 'Time']
    attendance_records = pd.DataFrame(columns=attendance_columns)

    # Initialize and start the video capture in real-time
    camera = cv2.VideoCapture(0)
    camera.set(3, 640)  # video width
    camera.set(4, 480)  # video height

    # Define minimum window size for face recognition
    min_width = 0.1 * camera.get(3)
    min_height = 0.1 * camera.get(4)

    while True:
        _, frame = camera.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detected_faces = face_cascade.detectMultiScale(
            gray_frame, 1.2, 5, minSize=(int(min_width), int(min_height)), flags=cv2.CASCADE_SCALE_IMAGE
        )

        for (x, y, w, h) in detected_faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (10, 159, 255), 2)
            Id, confidence = recognizer.predict(gray_frame[y:y + h, x:x + w])

            if confidence < 50:
                student_name = student_data.loc[student_data['Id'] == Id, 'Name'].values
                confidence_text = "  {0}%".format(round(100 - confidence))
                display_text = f"{Id}-{student_name}"

            else:
                Id = 'Unknown'
                display_text = str(Id)
                confidence_text = "  {0}%".format(round(100 - confidence))

            # Record attendance if confidence is above a threshold
            if (100 - confidence) > 50:
                current_time = time.time()
                date_today = datetime.datetime.fromtimestamp(current_time).strftime('%Y-%m-%d')
                timestamp = datetime.datetime.fromtimestamp(current_time).strftime('%H:%M:%S')
                student_name = str(student_name)[2:-2]
                attendance_records.loc[len(attendance_records)] = [Id, student_name, date_today, timestamp]

            display_text = str(display_text)[2:-2]
            if (100 - confidence) > 50:
                display_text += " [Verified]"
                cv2.putText(frame, display_text, (x + 5, y - 5), font_style, 1, (255, 255, 255), 2)
            else:
                cv2.putText(frame, display_text, (x + 5, y - 5), font_style, 1, (255, 255, 255), 2)

            # Confidence level display based on threshold
            if (100 - confidence) > 50:
                cv2.putText(frame, confidence_text, (x + 5, y + h - 5), font_style, 1, (0, 255, 0), 1)
            else:
                cv2.putText(frame, confidence_text, (x + 5, y + h - 5), font_style, 1, (0, 0, 255), 1)

        attendance_records = attendance_records.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('Attendance System', frame)

        if cv2.waitKey(1) == ord('q'):
            break

    # Save the attendance record
    timestamp = time.time()
    date_today = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
    time_str = datetime.datetime.fromtimestamp(timestamp).strftime('%H-%M-%S')
    attendance_file = f"Attendance{os.sep}Attendance_{date_today}_{time_str}.csv"
    attendance_records.to_csv(attendance_file, index=False)
    print("Attendance saved successfully.")
    camera.release()
    cv2.destroyAllWindows()

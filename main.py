import os
import Cam_Checker  # Updated module name
import Take_Photos  # Updated module name
import Model_Train  # Updated module name
import Mark_Attendance  # Updated module name
import SendToMail  # Updated module name


def display_title():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


def show_main_menu():
    display_title()
    print("\n", "*" * 10, "MAIN MENU", "*" * 10)
    print("[1] Check Camera\n[2] Capture Faces\n[3] Train Images")
    print("[4] Recognize & Record Attendance\n[5] Send Automatic Email\n[6] Exit")

    while True:
        try:
            choice = int(input("Select an option: "))

            if choice == 1:
                camera_check()
            elif choice == 2:
                capture_faces()
            elif choice == 3:
                train_images()
            elif choice == 4:
                recognize_faces()
            elif choice == 5:
                send_email()
            elif choice == 6:
                print("Exiting the system. Thank you for using it!")
                break
            else:
                print("Invalid selection. Please enter a number between 1 and 6.")

        except ValueError:
            print("Error: Please enter a valid number.")
    exit()


def camera_check():
    Cam_Checker.camer()  # Updated to match the new function name
    input("Press Enter to return to the main menu.")
    show_main_menu()


def capture_faces():
    Take_Photos.takeImages()  # Updated to match the new function name
    input("Press Enter to return to the main menu.")
    show_main_menu()


def train_images():
    Model_Train.TrainImages()  # Updated to match the new function name
    input("Press Enter to return to the main menu.")
    show_main_menu()


def recognize_faces():
    Mark_Attendance.recognize_attendance()  # Updated to match the new function name
    input("Press Enter to return to the main menu.")
    show_main_menu()


def send_email():
    SendToMail.mails()  # Updated to match the new function name
    input("Press Enter to return to the main menu.")
    show_main_menu()


if __name__ == "__main__":  # Added to allow for import without running
    show_main_menu()

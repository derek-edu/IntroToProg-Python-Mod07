# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   Derek Lau,2026-03-05,Created Script
# ------------------------------------------------------------------------------------------ #
import json
# import _io

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str  # Hold the choice made by the user.


# TODO Create a Person Class
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The student's first name.
    - last_name (str): The student's last name.

    ChangeLog:
    - Derek Lau,2026-03-05: Created the class.
    """

    # TODO Add first_name and last_name properties to the constructor
    def __init__(self, first_name: str = '', last_name: str = ''):
        self.first_name = first_name
        self.last_name = last_name

    # TODO Create a getter and setter for the first_name property
    @property  # (Use this decorator for the getter or accessor)
    def first_name(self):
        return self.__first_name.title()  # formatting code

    @first_name.setter
    def first_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    # TODO Create a getter and setter for the last_name property
    @property
    def last_name(self):
        return self.__last_name.title()  # formatting code

    @last_name.setter
    def last_name(self, value: str):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    # TODO Override the __str__() method to return Person data
    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# TODO Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection data about students inherits from Person.

    ChangeLog: (Who, When, What)
    Derek Lau,2026-03-05: Created the class.
    """

    # TODO call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, first_name: str = '', last_name: str = '', course_name: str = ''):
        # self.first_name = first_name
        # self.last_name = last_name
        super().__init__(first_name=first_name, last_name=last_name)

        # TODO add a assignment to the course_name property using the course_name parameter
        self.course_name = course_name

    # TODO add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.upper()  # keeping a consistent capitalized course name

    # TODO add the setter for course_name
    @course_name.setter
    def course_name(self, value: str):
        if value.replace(" ", "").isalnum() or value == "":  # is character or empty string
        # allowing space but check for no special characters
            self.__course_name = value
        else:
            raise ValueError("Course names should only contain letters and numbers.")



    # TODO Override the __str__() method to return the Student data
    def __str__(self):
        return f'{super().__str__()},{self.course_name}'


# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Derek Lau,2026-03-05: Created the class.
    """

    @staticmethod
    def read_data_from_file(file_name: str,student_data: list):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.

        :param file_name: string data with name of file to read from

        :return: list
        """
        file = None

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            student_data = []
            # TODO replace this line of code to convert dictionary data to Student data
            # student_objects = json_students

            for student in json_students:
                student_object: Student = Student(first_name=student['FirstName']
                                                  , last_name=student['LastName']
                                                  , course_name=student['CourseName'])
                student_data.append(student_object)

            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file is not None and file.closed == False:
                file.close()

        return student_data

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """
        file = None

        try:
            # TODO Add code to convert Student objects into dictionaries (Done)
            list_of_dictionary_data: list = []
            for student in student_data:  # Convert List of Student objects to list of dictionary rows.
                student_json: dict \
                    = {"FirstName": student.first_name, "LastName": student.last_name,
                       "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file, indent=2)  # add indent

            # add file save confirmation
            print()
            print(f"Success: Data saved to {file_name}!")
            print()

            IO.output_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message, error=e)
        finally:
            if file is not None and file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Derek Lau,2026-03-05: Created the class.
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays a custom error messages to the user

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.
        Derek Lau,2026-03-05: Updated to show comma-separated values

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print()
        print('Student(s) currently registered:')
        print("-" * 50)
        for student in student_data:
            # TODO Add code to access Student object data instead of dictionary data
            # print(f'Student {student["FirstName"]} '
            #       f'{student["LastName"]} is enrolled in {student["CourseName"]}')
            # print(f'Student {student.first_name} '
            #       f'{student.last_name} is enrolled in {student.course_name}')
            print(f'{student.first_name},{student.last_name},{student.course_name}')

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Derek Lau,2026-03-05: Created the function.

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # student_first_name = input("Enter the student's first name: ")
            # if not student_first_name.isalpha():
            #     raise ValueError("The last name should not contain numbers.")
            # student_last_name = input("Enter the student's last name: ")
            # if not student_last_name.isalpha():
            #     raise ValueError("The last name should not contain numbers.")
            # course_name = input("Please enter the name of the course: ")

            # TODO Replace this code to use a Student objects instead of a dictionary objects
            # student = {"FirstName": student_first_name,
            #            "LastName": student_last_name,
            #            "CourseName": course_name}

            student = Student()
            student.first_name = input("Enter your first name: ")
            student.last_name = input("Enter your last name: ")
            student.course_name = input("Enter your course name: ")

            student_data.append(student)
            print()
            print(f"You have registered {student.first_name} {student.last_name} for {student.course_name}.")
        except ValueError as e:
            IO.output_error_messages(message="One of the values was not the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME,student_data=students)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")

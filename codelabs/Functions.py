import re
import Constraints
import pandas as pd
import tensorflow as tf
from tensorflow import keras
import csv



def generate_email(className):

    df = pd.read_excel(Constraints.INPUT_FILE, sheet_name=className)
    student_emails = [
        ['Student Number','Student Name', 'Email']
    ]
    pattern = r'[^a-zA-Z@.\s]'
    # students = df["Student Name"]
    for index,student in df.iterrows():
        # print(student)
        email = "@gmail.com"
        student_names = student['Student Name'].split(" ")
        print(student_names)
        if len(student_names) < 2:
            email = student_names[0][0].lower() + student_names[-1].lower() + email
        else:
            email = student_names[0][0].lower() + student_names[-1].lower() + email

        clean_email = re.sub(pattern, '', email)

        if clean_email not in student_emails:
            student_emails.append([student["Student Number"], student["Student Name"], clean_email])
            print(clean_email)
        else:
            print(clean_email + " EMAIL EXISTS")
            break

    with open(Constraints.EMAIL_TSV_OUTPUT, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        for student in student_emails:
            writer.writerow(student)

def get_male_students(className):
    columns_to_read = ["Student Number", "Student Name", "Gender"]
    file = "Test Files.xlsx"
    df = pd.read_excel(file, sheet_name=className, usecols=columns_to_read)
    male_students = [
        ['Student Number','Student Name', 'Gender']
    ]
    for index,student in df.iterrows():
        if student["Gender"] == "M":
            male_students.append([student["Student Number"], student["Student Name"], student["Gender"]])

    print(male_students)
    with open(Constraints.MALE_TSV_OUTPUT, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        for s in male_students:
            writer.writerow(s)

def get_female_students(className):
    columns_to_read = ["Student Number", "Student Name", "Gender"]
    file = "Test Files.xlsx"
    df = pd.read_excel(file, sheet_name=className, usecols=columns_to_read)
    male_students = [
        ['Student Number','Student Name', 'Gender']
    ]
    for index,student in df.iterrows():
        if student["Gender"] == "F":
            male_students.append([student["Student Number"], student["Student Name"], student["Gender"]])

    print(male_students)
    with open(Constraints.FEMALE_TSV_OUTPUT, mode="w", newline='') as file:
        writer = csv.writer(file, delimiter='\t')
        for s in male_students:
            writer.writerow(s)
def one_time_shuffle(className):
    data = pd.read_excel(Constraints.INPUT_FILE, sheet_name=className)
    df = pd.DataFrame(data)
    shuffle_df = df.sample(frac=1.0, random_state=42)
    shuffle_df.to_json(Constraints.SHUFFLE_OUTPUT, orient='records')
    # print(shuffle_df)
def tensorflow_test():
    a = tf.constant(5)
    b = tf.constant(2)
    c = tf.add(a,b)
    result = c.numpy()
    print("Result: ",result)
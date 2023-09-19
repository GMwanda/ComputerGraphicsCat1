import pandas as pd

# Read the original Excel file into a DataFrame
df = pd.read_excel('Test_files.xlsx')  # Replace 'your_file.xlsx' with the actual file path

# Extract the relevant columns
student_data = df[['No.', 'Student Name', 'DoB', 'Gender']]

# Generate unique email addresses in the specified format
email_addresses = set()  # Use a set to store unique email addresses

for index, row in df.iterrows():
    # Split the full name into parts
    name_parts = row['Student Name'].split(', ')

    # Check if the parts list contains at least two elements
    if len(name_parts) >= 2:
        # Extract the first letter of the first name and concatenate with the last name
        first_letter = name_parts[1][0]  # First Name
        last_name = name_parts[0]  # Last Name

        # Create the email address
        email = first_letter + last_name + '@gmail.com'

        # Check if the email address is already in the set
        while email in email_addresses:
            # If email is not unique, append a number to make it unique
            email = first_letter + last_name + str(len(email_addresses) + 1) + '@gmail.com'

        # Add the unique email address to the set
        email_addresses.add(email)

    # Add the new email address to the DataFrame
    student_data.at[index, 'Email Address'] = email

# Save the student data to a new Excel file
student_data.to_excel('student_data_with_emails.xlsx', index=False)

# Display the student data
print(student_data)

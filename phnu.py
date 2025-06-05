import tkinter as tk
from tkinter import messagebox
import csv
import re  # Regular expression module

# Dictionary of emergency numbers in India
emergency_numbers = {
    "Police": "100",
    "Fire": "101",
    "Ambulance": "102",
    "Women Helpline": "1091",
    "Child Helpline": "1098",
    "Traffic Police": "103",
    "Disaster Management": "1078",
    "Health Helpline" : "104",
    "Tourist Helpline":"1363",
    "Road Accident Helpline":"1073",
    "Air Accident Helpline":"1071",
    "Gas Leakage":"1906",
    "Earthquake Helpline":"1072",
    "Anti-Terrorism Helpline":"1090",
    "Anti-Drug Helpline":"1093",
    "Anti-Human Trafficking Helpline":"1094",
    "Anti-Corruption Helpline":"1095",
    "Anti-Smuggling Helpline":"1096",
    "Anti-Black Money Helpline":"1097",
    "Anti-Child Labour Helpline":"1099",
    "National Emergency Number":"112"
}

# Function to get the emergency number based on the problem
def get_emergency_number(problem):
    return emergency_numbers.get(problem, "Emergency service not found.")

# Function to validate and format phone number
def validate_and_format_phone_number(phone_number):
    # Remove any non-digit characters
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Check if phone number is 10 digits long
    if len(phone_number)==10 and phone_number.isdigit():
            return phone_number
    else:
            print("Invalid input . Please enter exactly 10 digits .")

# Function to save user input to CSV
def save_user_info():
    name = entry_name.get()
    age = entry_age.get()
    phone_number = entry_phone_number.get()
    problem = combo_problem.get()        

    if name == "" or age == "" or phone_number == "" or problem == "":
        messagebox.showerror("Error", "All fields must be filled!")
        return
    
    # Validate and format phone number
    formatted_phone_number = validate_and_format_phone_number(phone_number)
    if formatted_phone_number is None:
        return  # Return if phone number is invalid
    
    # Get the emergency number
    emergency_number = get_emergency_number(problem)
    
    # Save the user information to CSV
    with open('user_info.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        
        # Write header if file is empty
        file.seek(0, 2)  # Move to the end of file
        if file.tell() == 0:  # Check if file is empty
            writer.writerow(["Name", "Age", "Phone Number", "Problem", "Emergency Number"])
        
        # Write user data to file
        writer.writerow([name, age, formatted_phone_number, problem, emergency_number])

    # Display emergency number to the user
    label_result.config(text=f"Emergency Number for {problem}: {emergency_number}")
    messagebox.showinfo("Success", "Your information has been saved successfully!")

# Setting up the main window
root = tk.Tk()
root.title("Emergency Information System")

# Creating the labels and entry widgets
label_name = tk.Label(root, text="Enter your Name:")
label_name.pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

label_age = tk.Label(root, text="Enter your Age:")
label_age.pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

label_phone = tk.Label(root, text="Enter your Phone Number:")
label_phone.pack(pady=5)
entry_phone_number = tk.Entry(root)
entry_phone_number.pack(pady=5)

label_problem = tk.Label(root, text="Select the Problem (e.g., Police, Fire, Ambulance):")
label_problem.pack(pady=5)

# Drop-down menu for emergency problem selection
combo_problem = tk.StringVar()
combo_problem.set("Police")  # Default value
dropdown = tk.OptionMenu(root, combo_problem, *emergency_numbers.keys())
dropdown.pack(pady=5)

# Button to submit the information
button_submit = tk.Button(root, text="Submit", command=save_user_info)
button_submit.pack(pady=10)

# Label to display the emergency number result
label_result = tk.Label(root, text="Emergency Number will appear here", fg="blue")
label_result.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

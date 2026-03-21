# Python example
import os
import sqlite3

conn = sqlite3.connect('instance/app.db')
cursor = conn.cursor()


basedir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join('/Users/mr.wolf/Desktop/insurance_claimer/backend', 'policies/abc_health_insurance_policy.txt')

policy_text = ""
# Open and read the file content
try:
    with open(file_path, 'r') as file:
        policy_text = file.read()
except IOError as e:
    policy_text = f"Error reading file: {e}"
# Execute the insert statement
# cursor.execute("alter table claims add column claimed_amount int8",)
# cursor.execute("Insert into policies (policy_number,policy_text) values (?,?)",(1,policy_text))
cursor.execute("DELETE FROM users WHERE id = ?", (4,))
# Commit the changes
conn.commit()

# Close the connection
conn.close()
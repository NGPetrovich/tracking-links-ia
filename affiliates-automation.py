import subprocess
import os
import glob

scripts = [
    'affiliates-1.py',
    'affiliates-2.py',
    'affiliates-3.py',
    'affiliates-4.py'
]

for script in scripts:
    print(f"Running {script}...")
    result = subprocess.run(['python', script], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{script} SUCCESS!")
        print(result.stdout)
    else:
        print(f"Error running {script}.")
        print(result.stderr)

# Delete all CSV files except for "final.csv"
csv_files = glob.glob('*.csv')
for file in csv_files:
    if file != 'final.csv':
        os.remove(file)

print("All CSV files except 'final.csv' have been deleted.")
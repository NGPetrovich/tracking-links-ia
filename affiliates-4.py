import csv

with open('subtotals_part_2.csv', 'r') as input_file:
    reader = csv.reader(input_file)
    data = list(reader)

new_data = []
for row in data:
    # Adding empty row after "Subtotal" rows
    new_data.append(row)
    if row[2] == "Subtotal":
        new_data.append([])

with open('final.csv', 'w', newline='') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(new_data)

print("CSV file updated successfully!")
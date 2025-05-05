import csv

def compare_and_organize(instance_csv):
    with open(instance_csv, "r") as file:
        reader = csv.reader(file)
        data = list(reader)
    
    header = data[0] + ["Matched Private IP"]  # Adding a new column for matched IPs
    rows = data[1:]
    
    # Create a mapping of Instance IDs (Column A) to Private IPs (Column B)
    instance_ip_map = {row[0]: row[1] for row in rows}  # {Instance ID -> Private IP}
    
    for row in rows:
        instance_id = row[0]  # Get Instance ID from Column A
        row.append(instance_ip_map.get(instance_id, "No Match"))  # Fill Column F with matched Private IP
    
    with open("organized_instances.csv", "w", newline="") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(rows)
    
    print("Comparison and organization completed. Check 'organized_instances.csv'.")

# Run the function
compare_and_organize("ec2_instances.csv")
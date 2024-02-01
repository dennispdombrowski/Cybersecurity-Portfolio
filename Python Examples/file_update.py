# Assign import_file to the name of the file
import_file = "allow_list.txt"

with open(import_file, "r") as file:
    # Use read to store contents in the ip_addresses variable
    ip_addresses = file.read
    
    # Convert from sting to list.
    ip_addresses = ip_addresses.split()

for element in remove_list:
    if element in ip_addresses: 
        ip_addresses.remove(element)

# Converts ip_addresses to str to be written back to the file.
ip_addresses - "\n".join(ip_addresses)

with open(import_file, "w") as file:
    file.write(ip_addresses)


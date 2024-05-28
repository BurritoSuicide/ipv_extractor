import csv
import ipaddress

# Define address type based on user input.
def extract_ip_addresses_user_defined(input_csv, output_csv):
    try:
        address_type = input("Enter 'v4' for IPv4 or 'v6' for IPv6 addresses: ").lower()
        if address_type not in ('v4', 'v6'):
            print("Invalid input. Please enter 'v4' or 'v6'.")
            return
# Reading file.
        with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            for row in reader:
                for item in row:
                    try:
                        ip = ipaddress.ip_network(item, strict=False)
                        if (address_type == 'v4' and ip.version == 4) or (address_type == 'v6' and ip.version == 6):
                            if '/' in item:
                                # Handle CIDR range
                                print("Writing " + str(ip.network_address) + " to output.csv..")
                                writer.writerow([ip.network_address] + row)
                            else:
                                # Individual IP address
                                writer.writerow([ip] + row)
                    except ValueError:
                        pass  # Ignore non-IP addresses
        print(f"{address_type.upper()} addresses (including CIDR ranges) and corresponding rows extracted from '{input_csv}' and saved to '{output_csv}'.")
    except FileNotFoundError:
        print(f"File '{input_csv}' not found.")

# Example usage:
input_file = 'input.csv'
output_file = 'output.csv'
extract_ip_addresses_user_defined(input_file, output_file)

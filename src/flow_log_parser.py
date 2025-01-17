import csv

PROTOCOL_MAP = {
    "6": "tcp",
    "17": "udp",
    "1": "icmp"
}

def load_lookup_table(filepath):
    lookup = {}
    with open(filepath, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = (int(row['dstport']), row['protocol'].lower())
            lookup[key] = row['tag']
    return lookup

def process_flow_logs(log_filepath, lookup):
    tag_counts = {}
    port_protocol_counts = {}
    untagged_count = 0

    with open(log_filepath, 'r') as file:
        for line in file:
            log_parts = line.strip().split()
            dstport = int(log_parts[5])  # Assuming 6th field is dstport
            protocol_number = log_parts[7]  # Assuming 8th field is protocol
            protocol = PROTOCOL_MAP.get(protocol_number, protocol_number).lower()

            # Tag matching
            key = (dstport, protocol)
            if key in lookup:
                tag = lookup[key]
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
            else:
                untagged_count += 1

            # Port/protocol count
            port_protocol_key = (dstport, protocol)
            port_protocol_counts[port_protocol_key] = port_protocol_counts.get(port_protocol_key, 0) + 1

    return tag_counts, port_protocol_counts, untagged_count

def write_output(tag_counts, untagged_count, port_protocol_counts):
    # Write Tag Counts
    with open("output/tag_counts.csv", "w") as file:
        file.write("Tag,Count\n")
        for tag, count in tag_counts.items():
            file.write(f"{tag},{count}\n")
        file.write(f"Untagged,{untagged_count}\n")

    # Write Port/Protocol Counts
    with open("output/port_protocol_counts.csv", "w") as file:
        file.write("Port,Protocol,Count\n")
        for (port, protocol), count in port_protocol_counts.items():
            file.write(f"{port},{protocol},{count}\n")

if __name__ == "__main__":
    lookup_table_path = "input/lookup_table.csv"
    flow_logs_path = "input/flow_logs.txt"

    lookup_table = load_lookup_table(lookup_table_path)
    tag_counts, port_protocol_counts, untagged_count = process_flow_logs(flow_logs_path, lookup_table)
    write_output(tag_counts, untagged_count, port_protocol_counts)

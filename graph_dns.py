import scapy.all as scapy
import matplotlib.pyplot as plt

# Read the PCAP file
packets = scapy.rdpcap(".pcap")

# Extract the DNS queries from the packets
dns_queries = []
for packet in packets:
    if packet.haslayer(scapy.DNS):
        dns_query = packet[scapy.DNS].qd.qname.decode()
        dns_queries.append(dns_query)

# Create a dictionary to count the frequency of each DNS query
dns_query_counts = {}
for dns_query in dns_queries:
    if dns_query in dns_query_counts:
        dns_query_counts[dns_query] += 1
    else:
        dns_query_counts[dns_query] = 1

# Create a bar graph showing the frequency of each DNS query
plt.bar(range(len(dns_query_counts)), list(dns_query_counts.values()), align='center')
plt.xticks(range(len(dns_query_counts)), list(dns_query_counts.keys()), rotation=90)
plt.xlabel("DNS Query")
plt.ylabel("Frequency")
plt.title("DNS Request Frequencies")
plt.show()
import pyshark as ps
import sys


nbPackets = 10
# Get the nbPackets to capture from the user when calling the script
if len(sys.argv) > 1:
    nbPackets = int(sys.argv[1])

# Create a filter to capture only the packets we want
capture_filter = "tcp.port == 80 and ip.src == 192.168.10.158 and ip.version == 4"

# Capture packets from interface 
cap = ps.LiveCapture(interface='wlp1s0', output_file='test.pcap', capture_filter=capture_filter)

# show the packets
for pkt in cap.sniff_continuously(packet_count=nbPackets):
    print(pkt)

# write pkt to a file pcap
# captureFile = ps.FileCapture('test.pcap', output_file='test.pcap')

# Start the capture
# captureFile.sniff(timeout=10)

# Stop the capture
# captureFile.close()

# Save the packets to a file
# captureFile.save()

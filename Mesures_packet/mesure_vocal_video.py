import pyshark
import datetime
import matplotlib.pyplot as plt

def packets_per_minute(pcap_file):
    capture = pyshark.FileCapture(pcap_file)
    packet_count = 0
    start_time = None
    end_time = None
    packet_times = []
    
    for packet in capture:
        if start_time is None:
            start_time = packet.sniff_time
        else:
            end_time = packet.sniff_time
            packet_times.append(end_time)
            packet_count += 1
            
    capture.close()
    
    print("Start Time: {}".format(start_time))
    print("End Time: {}".format(end_time))
    time_diff = (end_time.timestamp() - start_time.timestamp()) / 60.0
    packets_per_min = packet_count / time_diff
    return packets_per_min

vocal = "Appel_mesures.pcap"
video = "Appel_video_mesures.pcap"

avg_packets_per_min1 = packets_per_minute(vocal)
avg_packets_per_min2 = packets_per_minute(video)

# Print the results
print("Average Packets per Minute for Appel audio: {}".format(avg_packets_per_min1))
print("Average Packets per Minute for Appel vidéo: {}".format(avg_packets_per_min2))

# plot the results as a bar graph
plt.bar([1, 2], [avg_packets_per_min1, avg_packets_per_min2], tick_label=['Appel audio', 'Appel vidéo'], color=['blue', 'green'])
plt.ylabel('Average Packets per Minute')
plt.title('Packet Analysis')

# Save the graph as pdf
plt.savefig('packet_analysis.pdf')

# Show the graph
plt.show()
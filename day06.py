with open(file='data.txt') as file:
    data = file.read()


def detect_packet_marker(packet_window: int, datastream_buffer: str) -> int:
    marker_index, start = 0, 0
    # use sliding window to traverse string
    for end, character in enumerate(datastream_buffer):
        if end - start + 1 == packet_window:
            if len(set(datastream_buffer[start:end+1])) == packet_window:  # packet found
                marker_index = end + 1
                return marker_index

            start += 1

    # if no packet found
    return 0


# part one:
print(detect_packet_marker(4, data))
# part two:
print(detect_packet_marker(14, data))

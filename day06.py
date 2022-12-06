with open(file='data.txt') as file:
    data = file.read()


def detect_first_marker(window_length: int, datastream_buffer: str) -> int:
    marker_index, start = 0, 0
    # use sliding window to traverse string
    for end, character in enumerate(datastream_buffer):
        if end - start + 1 == window_length:
            if len(set(datastream_buffer[start:end+1])) == window_length:  # packet, or message found
                marker_index = end + 1
                return marker_index

            start += 1

    # if no marker found
    return 0


# part one:
print(detect_first_marker(4, data))
# part two:
print(detect_first_marker(14, data))

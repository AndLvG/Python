import wave
import struct


def break_the_silence():
    source = wave.open("in_mono.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = []

    n = frames_count // 4

    for i in range(n * 2, n * 3):
        newdata.append(data[i])
    for i in range(n):
        newdata.append(data[i])
    for i in range(n * 3, frames_count):
        newdata.append(data[i])
    for i in range(n, n * 2):
        newdata.append(data[i])

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)

    # frames_coun = dest.getnframes()
    source.close()
    dest.close()

break_the_silence()

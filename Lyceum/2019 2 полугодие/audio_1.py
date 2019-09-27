import wave
import struct


def break_the_silence():
    source = wave.open("in.wav", mode="rb")
    dest = wave.open("out.wav", mode="wb")

    dest.setparams(source.getparams())
    frames_count = source.getnframes()
    # channels = source.getnchannels()

    # data = struct.unpack("<" + str(frames_count * channels) + "h", source.readframes(frames_count))
    data = struct.unpack("<" + str(frames_count) + "h", source.readframes(frames_count))
    newdata = []

    for i in range(len(data)):
        amp = abs(data[i])
        if amp > 5:
            newdata.append(data[i])
        # if amp <= 5:
        #     newdata.append(0)
        # else:
        #     newdata.append(data[i])

    newframes = struct.pack("<" + str(len(newdata)) + "h", *newdata)

    dest.writeframes(newframes)

    # frames_coun = dest.getnframes()
    source.close()
    dest.close()

# break_the_silence()

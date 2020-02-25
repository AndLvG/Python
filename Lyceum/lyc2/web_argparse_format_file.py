import argparse


def format_text_block(frame_height, frame_width, file_name):
    try:
        with open(file_name, 'r', encoding="UTF-8") as file:
            # data = file.read().split("\n")
            h = 1
            w = 0
            result = ""
            while h < frame_height:
                line = file.readline().replace("\n", "")
                # result += 'len' + str(len(line)) + 'width' + str(frame_width) +" - " + line+ "\n"
                if len(line) > frame_width:
                    while w < len(line):
                        # result += '1  ' + str(h) + " - " + line[w:w+frame_width] + "\n"
                        result += line[w:w + frame_width] + "\n"
                        w += frame_width
                        h += 1
                        if h > frame_height:
                            return result[:-1]
                else:
                    # result += '2  ' + str(h) + " - " + line + "\n"
                    result += line + "\n"
                    h += 1
                w = 0
        return result

    except Exception as pe:
        return pe


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str)
    parser.add_argument('--frame-height', type=int)
    parser.add_argument('--frame-width', type=int)
    args = parser.parse_args()
    print(format_text_block(args.frame_height, args.frame_width, args.file))

#  python web_argparse_format_file.py --frame-height 10 --frame-width 30 filename.txt
# python web_argparse_format_file.py --frame-height 10 --frame-width 30 file.txt

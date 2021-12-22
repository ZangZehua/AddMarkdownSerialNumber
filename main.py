import argparse
import re


def get_common_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help='the path of the input markdown file')
    parser.add_argument('-o', type=str, help='the path of the output markdown file, '
                                             'the output path cannot be the same as the input path')
    parser.add_argument('-m', type=int, default=0, help='0: end without .; 1: end with .')
    args = parser.parse_args()
    return args


def generate_serial_number(serial_number_list, level, mode):
    serial_number = ""
    if mode == 0:
        for sn in serial_number_list[:level-1]:
            serial_number += str(sn) + "."
        serial_number += str(serial_number_list[level-1])
        serial_number += " "
    elif mode == 1:
        for sn in serial_number_list[:level]:
            serial_number += str(sn) + "."
    return serial_number


def add_serial_number(args):
    try:
        output_file = open(args.o, "w", encoding='UTF-8')
        print("successfully open output file")
    except Exception as e:
        print("fail to open file" + args.o)
        exit()

    with open(args.i, "r", encoding='UTF-8') as input_file:
        serial_number_list = [0]*5
        temp_line = input_file.readline()
        counter = 0
        # in_code = False
        while temp_line is not None and counter < 1000:
            # if re.match("```", temp_line) is not None:
            #     temp_line = input_file.readline()
            #     counter += 1
            #     in_code = not in_code
            #     print(in_code)
            # elif in_code:
            #     temp_line = input_file.readline()
            #     counter += 1
            #     print("still in code")
            #     continue
            if re.match("###### ", temp_line) is not None:
                serial_number_list[4] += 1
                serial_number = generate_serial_number(serial_number_list, 5, args.m)
                temp_line = temp_line.replace("###### ", "###### " + str(serial_number), 1)
                output_file.write(temp_line)
            elif re.match("##### ", temp_line) is not None:
                serial_number_list[3] += 1
                serial_number_list[4:5] = [0]
                serial_number = generate_serial_number(serial_number_list, 4, args.m)
                temp_line = temp_line.replace("##### ", "##### " + str(serial_number), 1)
                output_file.write(temp_line)
            elif re.match("#### ", temp_line) is not None:
                serial_number_list[2] += 1
                serial_number_list[3:5] = [0, 0]
                serial_number = generate_serial_number(serial_number_list, 3, args.m)
                temp_line = temp_line.replace("#### ", "#### " + str(serial_number), 1)
                output_file.write(temp_line)
            elif re.match("### ", temp_line) is not None:
                serial_number_list[1] += 1
                serial_number_list[2:5] = [0, 0, 0]
                serial_number = generate_serial_number(serial_number_list, 2, args.m)
                temp_line = temp_line.replace("### ", "### " + str(serial_number), 1)
                output_file.write(temp_line)
            elif re.match("## ", temp_line) is not None:
                serial_number_list[0] += 1
                serial_number_list[1:5] = [0, 0, 0, 0]
                serial_number = generate_serial_number(serial_number_list, 1, args.m)
                temp_line = temp_line.replace("## ", "## " + str(serial_number), 1)
                output_file.write(temp_line)
            else:
                output_file.write(temp_line)
            output_file.flush()
            temp_line = input_file.readline()
            counter += 1
    output_file.close()
    print("serial number added")


if __name__ == '__main__':
    args = get_common_args()
    add_serial_number(args)



import argparse


def get_common_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', type=str, help='the path of the input markdown file')
    parser.add_argument('-o', type=str, help='the path of the output markdown file, '
                                             'the output path cannot be the same as the input path')
    parser.add_argument('-m', type=int, default=0, help='0: end without .; 1: end with .')
    args = parser.parse_args()
    return args


def generate_serial_number(serial_number_list, mode):
    serial_number = ""
    if mode == 0:
        for sn in serial_number_list[:-1]:
            serial_number += str(sn) + "."
        serial_number += str(serial_number_list[-1])
    elif mode == 1:
        for sn in serial_number_list:
            serial_number += str(sn) + "."
    return serial_number

def add_serial_number(input_path, output_path):
    try:
        output_file = open(output_path, "w")
    except Exception as e:
        print("fail to open file" + output_path)

    with open(input_path, "r") as input_file:
        serial_number_list = [1]*6
        temp_line = input_file.readline()




if __name__ == '__main__':
    args = get_common_args()
    print(args)
    serial_number_list = [1] * 6
    print(serial_number_list)
    print(generate_serial_number(serial_number_list, args.m))


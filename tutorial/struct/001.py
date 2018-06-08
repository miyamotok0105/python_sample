import struct
#エラーなってるじゃねーかー
def main():
    print("main")
    binary_data_int = 'xFFxFF'
    binary_data_char = 'x41'
    binary_data_string = 'x61x62x63'
 
    print(binary_data_int.encode('utf-8'))

    print(struct.unpack("H", binary_data_int.encode('utf-8')))
    # print(struct.unpack("h", binary_data_int))
    # print(struct.unpack('c', binary_data_char))
    # print(struct.unpack("3s", binary_data_string))
 
    # c_data_int_1 = 65535
    # c_data_int_2 = -1
    # c_data_char = 'A'
    # c_data_string = "abc"
 
    # print(repr( struct.pack("H", c_data_int_1) ))
    # print(repr( struct.pack("h", c_data_int_2) ))
    # print(repr( struct.pack("c", c_data_char) ))
    # print(repr( struct.pack("3s", c_data_string) ))
 
if __name__ == '__main__':
    main()


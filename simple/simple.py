import simple_pb2 as simple_pb2

def write():
    file = open("simple.bin", "wb")
    bytesAsString = simple_message.SerializeToString()
    file.write(bytesAsString)
    file.close()

def read():
    file = open("simple.bin", "rb")
    # instanc - fill values and reading
    simple_message_read = simple_pb2.SimpleMessage().FromString(file.read())
    # showing
    print(simple_message_read)
    # particular value
    print("Is Simple?: " + str(simple_message_read.id))

if __name__ == "__main__":
    # object
    simple_message = simple_pb2.SimpleMessage()
    # calling attributes
    simple_message.id = 123
    simple_message.is_simple = True
    simple_message.name = "Python's simple message"
    # repeated
    sample_list = simple_message.sample_list
    sample_list.append(3)
    sample_list.append(4)
    sample_list.append(5)
    # printing object
    print(simple_message)
    # writing mode
    print("Write as binary")
    write()
    # reading
    print("Read as Binary")
    read()

with open('brainfuck_src.txt') as f:
    src = f.read()

arr = [0 for i in range(30000)]

symbols = "<>+-,.[]"


def normalize(ind):
    if arr[ind] > 255:
        arr[ind] = arr[ind] % 255
    while arr[ind] < 0:
        arr[ind] += 256


def loop(src_i):
    global index
    end_of_loop = 0
    while arr[index] != 0:
        i = src_i
        while True:
            i += 1
            if src[i] == ">":
                index += 1
            if src[i] == "<":
                index -= 1
            if src[i] == "+":
                arr[index] += 1
                normalize(index)
            if src[i] == "-":
                arr[index] -= 1
                normalize(index)
            if src[i] == ".":
                print(chr(arr[index]), end="")
            if src[i] == ",":
                arr[index] = ord(input())
                normalize(index)
            if src[i] == "]":
                end_of_loop = i
                break
            if src[i] == "[":
                i = loop(i)
    return end_of_loop


index = 0
source_index = -1
print("Source file:")
print(src)
print("Output:")
while True:
    source_index += 1
    if src[source_index] == ">":
        index += 1
    if src[source_index] == "<":
        index -= 1
    if src[source_index] == "+":
        arr[index] += 1
        normalize(index)
    if src[source_index] == "-":
        arr[index] -= 1
        normalize(index)
    if src[source_index] == ".":
        print(chr(arr[index]), end="")
    if src[source_index] == ",":
        arr[index] = ord(input())
        normalize(index)
    if src[source_index] == "[":
        source_index = loop(source_index)
    if source_index >= len(src) - 1:
        break

from random import randint

def do_sort(input, output=[]):

    # compute the gap
    h = 1
    l = len(input)

    while h < l/3: h = int(h*3 + 1)

    while h > 0:

        for i in range(h, l):

            j = i
            saved = input[j]

            while j > 0 and input[j-h] > saved:
                input[j-h], input[j] = input[j], input[j-h]
                j -= h

        h = int(h/3)

    return input



if __name__ == '__main__':

    print(do_sort([randint(1,50) for _ in range(50)]))
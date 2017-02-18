def do_sort(input, outputs=[]):


    for x in range(len(input)):

        minIndx = x

        for j in range(x+1,len(input)):

            if input[j] < input[minIndx]:
                minIndx = j


        input[x], input[minIndx] = input[minIndx], input[x]
        #outputs.append((minIndx, list(input)))

    return input


if __name__ == '__main__':
    print(do_sort([5,3,6,1,4,2]))
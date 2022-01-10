def do_sort(input, outputs=[]):

    for i in range(1,len(input)):

        j = i

        # extract the value being compared
        saved = input[i]

        # now list isn't being accessed twice unnecessarily
        while(j > 0 and input[j-1] > saved):

            # don't actually perform the intermediate swaps,
            # just let the cursor settle into the final position
            # input[j - 1], input[j] = input[j], input[j - 1]
            j-=1


        # now insert it and let the hardware do the actual shifting of the values in the list
        input.insert(j,input.pop(i))


    return input





if __name__ == '__main__':
    print(do_sort(['S','O','R','T ','E','X','A','M','P','L','E']))
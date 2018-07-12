def ulam_sequence(u0, u1, n):
    """
    u0 = first number
    u1 = second numberr
    n  = final number of elements in the sequence
    """
    final_list=[u0,u1]
    counter=2
    while counter<n:
        index=0
        sum=final_list[counter-1]
        while index!=1:
            sum=sum+1
            index=0
            for x in range(0,len(final_list)-1):
                for y in range(x+1,len(final_list)):
                    if final_list[x]+final_list[y] == sum:
                        index=index+1

        counter=counter+1
        final_list.append(sum)
    return   final_list 
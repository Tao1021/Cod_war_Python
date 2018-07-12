
# Fibo akin
# Python:
def fibo_a(n):

	my_fibo_dic={1:1, 2:1}

	for x in range(3,n+1): 

		my_fibo_dic[x] =  my_fibo_dic[x - my_fibo_dic[x-1]]+ my_fibo_dic[x - my_fibo_dic[x-2]]

	return my_fibo_dic
def length_sup_u_k(n, k):
    count = 0
    dic=fibo_a(n)
    for item in range(1, n+1):
        if dic[item]>= k :
            count=count+1
            
    return count 
def comp(n):
    count=0
    dic=fibo_a(n)
    for x in range(2,n+1):
        if dic[x-1]> dic[x] :
            count=count+1
    return count
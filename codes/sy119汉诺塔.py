def move(n,from_,to_,mid_):
    if n == 0:
        return
    else:
        move(n-1,from_,mid_,to_)
        print('{}->{}'.format(from_,to_))
        move(n-1,mid_,to_,from_)
n = int(input())
print(2**n-1)
move(n,'A','C','B')
# Basic of List in Python------->

# 1. Square of list elements----->
lis = [1,2,3,4,5,6,7,8,9,10]
s_lis = []
def square_lis(l):
    for i in l:
        s_lis.append(i**2)
    return s_lis
square_lis(lis)   

# 2. Reverse elements in list------>
# a. using slicing mathod---->
lis_ = list(range(1,11))
rev_lis = []
def reverse(l):
    rev_lis = lis_[::-1]
    return rev_lis
print(reverse(lis_))
# b. using append() & pop()---->
lis_ = list(range(1,11))
rev_lis = []
def reverse(l):
    for i in range(len(l)):
        rev_lis.append(l.pop())
    return rev_lis     
print(reverse(lis_))

# 3. Reverse of string as list elements------>
word_lis = ["abc","def","ghi"]
R_R_word_lis = []
def r_r_word(l):
    for i in range(len(l)):
        R_R_word_lis.append(l[i][::-1]) 
    return R_R_word_lis
print(r_r_word(word_lis))

# 4. Filter func of Odd & Even numbers------->
unfi_lis = list(range(1,11))
odd_lis = []
ev_lis = []
fi_lis = []
def Filte_Od_Ev(l):
    for i in l:
        if i%2==0:
            ev_lis.append(i)
        else:
            odd_lis.append(i)
    fi_lis.append(odd_lis)
    fi_lis.append(ev_lis)
    return fi_lis
print(Filte_Od_Ev(unfi_lis))

# 5. Common value filer fun()
f_l = [1,10,3,4,5,11]
s_l = [1,2,6,7,8,11,12]
c_l = []
def comm(l_1,l_2):
    for i in l_1:
        for j in l_2:
            if i == j:
               c_l.append(i)
    return c_l
print(comm(f_l,s_l))

# 6. count List of List fun()
new_l = [1,2,3,[4,5,6],[7,8,9]]
def lis_of_lis(l):
    count = 0
    for i in l:
        if type(i)==list:
            count+=1
    return count
print(lis_of_lis(new_l))

# 7. string checker fun()
st_1 = "priya"
st_2 = "ayirp"
def app(s_1,s_2):
    for i in range(len(s_1)):
        s_2_i = s_1.find(s_1[i])
        s_1_i = s_2.find(s_1[i])
        if s_1[s_2_i] ==s_2[s_1_i]:
            continue
        else:
            return "Not Match"
            break
    return "Match"
print(app(st_1,st_2))

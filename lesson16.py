
def rangeofnum(start, end):
    lst = []
    for i in range(start, end):
        if i > start:
            lst.append(i)
    return lst

print(rangeofnum(2, 4))
print(rangeofnum(5, 9))
print(rangeofnum(2, 11))



def isfourletters(lst):
    lst1 = []
    for x in lst:
        if len(x) == 4:
            lst1.append(x)
    return lst1

print(isfourletters(["tomato","potato","pair"]))
print(isfourletters(["Kangaroo","Bear","fox"]))
print(isfourletters(["Ryan","Kieren","Jason", "Matt"]))



def firstlast(lst):
    lst1 = []
    for x in lst:
        if x == lst[0]:
            lst1.append(x)
        if x == lst[-1]:
            lst1.append(x)
    return lst1


print(firstlast([5,10,15,20,25]))
print(firstlast(["Edabit",13,"null",False,True]))
print(firstlast(["undefined",4,"6","hello","null"]))



def get_budgets(lst):
    for x in lst:
        pass
print(get_budgets([{"name": "John", "age": 21, "budget": 23000},
                   {"name": "Steve", "age": 32, "budget": 40000},
                   {"name": "Martin", "age": 16, "budget": 2700}
]))


















#init
cond = [1,0,0]
# print(target[0])
def post_event_probability (a,b):
    post_event = a*b
    return post_event
def conditional_probability (condition,probability):
    p = post_event/condition
    return p
def bi(ai,biai):
    out = ai*biai
    return out
def bayes (ai,biai,bi):
    aibi = ai*biai/bi
    return aibi


# def change_guess():
#     b3a1 = 1/(all_target-1)
# #open b3
# if cond[0] == True:
#     b3a1 = 1/(all_target-1)
#     b3a2 = 1/(all_target-1-1)


#init base probability
all_target = len(cond)
a1 = 1/all_target
a2 = 1/all_target
a3 = 1/all_target

b3a1 = 1/2
b3a2 = 1
b3a3 = 0

r1 = bi(a1, b3a1)
r2 = bi(a2, b3a2)
r3 = bi(a3, b3a3)
pb3 = r1 + r2 +r3

a1b3 = bayes(a1, b3a1, pb3)
a2b3 = bayes(a2, b3a2, pb3)

print(a1b3)
print(a2b3)
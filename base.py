#init
target = [1,0,0]
# print(target[0])
def post_event_probability (a,b):
    post_event = a*b
    return post_event
def conditional_probability (condition,probability):
    p = post_event/condition
    return p

#init base probability
all_target = len(target)
a1 = 1/all_target
a2 = 1/all_target
a3 = 1/all_target


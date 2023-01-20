#init
target = [1,0,0]
# print(target[0])
def post_event_probability (a,b):
    post_event = a*b
    return post_event
def conditional_probability (condition,probability):
    p = post_event/condition
    return p
#post_event_probability and conditional_probability module test;

a = 1/2
b = 1/3
pa1 = 1/3
post_event = post_event_probability(a, b)
result = conditional_probability(post_event, pa1)
print(result)




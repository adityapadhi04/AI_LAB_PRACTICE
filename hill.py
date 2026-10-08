#Hill clambing algorithm
'''
f(x)=-(x-4)**2+16
f(0)=0
f(1)=25
f(2)=20
f(3)=15
f(4)=16
f(5)=15
f(6)=12
f(7)=7
f(8)=0
f(9)=-9
'''

'''

f(x)=-(x-8)**2+64
f(0)=0
f(1)=7
f(2)=28
f(3)=39
f(4)=48
f(5)=55
f(6)=60
f(7)=63
f(8)=64
f(9)=63
'''


'''
f(x)=-0.5(x-6)**2+40
f(0)=22
f(1)=27.5
f(2)=32
f(3)=35.5
f(4)=38
f(5)=39.5
f(6)=40
f(7)=39.5
f(8)=38
f(9)=35.5
'''
#objective function
def objective_function(x):
    return -(x**2)+10

#Hill climbing algorithm
def hill_climbing(start,step,max_iterations):
    current=start
    current_value=objective_function(current)
    for i in range(max_iterations):
        left=current-step
        right=current+step
        left_value=objective_function(left)
        right_value=objective_function(right)

        #move to the bettter neighbor
        if left_value > current_value:
            current=left
            current_value=left_value
        elif right_value > current_value:
            current=right
            current_value=right_value
        else:
            break
    return current,current_value
#main program
start=int(input("Enter the starting value: "))
step=int(input("Enter the step size: "))
max_iterations=int(input("Enter the maximum iterations: "))
best_position,best_value=hill_climbing(start,step,max_iterations)
print("\nBest position=",best_position)
print("Maximum value=",best_value)
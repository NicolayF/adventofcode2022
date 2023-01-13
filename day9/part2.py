#Get data
with open("input.in") as f:
    input = f.read().strip().split("\n")

#10 knots each with its position
knots = [[0, 0] for _ in range(10)]

#Are the tail and the head touching?
#Only if they are at most 1 space afar
def touching(x1, y1, x2, y2):
    return abs(x1-x2) <= 1 and abs(y1-y2) <= 1

def move(x, y):
    global knots
    #First knot
    knots[0][0] += x
    knots[0][1] += y
    
    for i in range(1, 10):
        head_x, head_y = knots[i-1]
        tail_x, tail_y = knots[i]
        #Moving tail.
        #dif_x: if they are in the same column then don't move
        #       else move right if 1 or left if -1
        #dif_y: if they are in the same row then don't move
        #       else move up if 1 or down if -1
        #Divided by absolute of head - tail to return a single unit
        #beacuse there is no case in which the tail moves more tan 1 unit at times.
        if not touching(head_x, head_y, tail_x, tail_y):
            dif_x = 0 if head_x == tail_x else (head_x - tail_x) / abs(head_x - tail_x)
            dif_y = 0 if head_y == tail_y else (head_y - tail_y) / abs(head_y - tail_y)
            tail_x += dif_x
            tail_y += dif_y
        
        knots[i] = [tail_x, tail_y]
    
#Direction dict
dd = {
    "R": [1, 0],
    "L": [-1, 0],
    "U": [0, 1],
    "D": [0, -1]
}

#Set to store unique tail positions
tail_pos = set()
#Add starting position
tail_pos.add(tuple(knots[-1]))

#Resolve for input
for direction in input:
    dir, amt = direction.split(" ")
    amt = int(amt)
    dx, dy = dd[dir]
    
    for _ in range(amt):
        move(dx, dy)                    #First move is head then 9 follow each other
        tail_pos.add(tuple(knots[-1]))  #Just add the 10th knot now

print(len(tail_pos))
        
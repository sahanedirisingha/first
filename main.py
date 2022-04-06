from turtle import *
speed(1)
width(4)

bgcolor('black')
color('blue')

# moving turtle to starting point
goto(-50,60)
pendown()
# going to right top
goto (100,100)
# going to right bottom
goto (100,-100)
# going to left bottom
goto(-50,-60)
# going to starting point
goto(-50,60)

# starting from left middle
goto(-50,0)
pendown()
# ending at right middle
goto(100, 0)



# cutting the shape into two halves vertically
# starting from upper middle
goto (25,80)
pendown()
# ending at bottom middle
goto(25,-80)

done()













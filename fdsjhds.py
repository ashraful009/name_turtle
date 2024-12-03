import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
t = turtle.Turtle()
t.pensize(5)
t.color("blue")

# Write "Ashraful"
t.penup()
t.goto(-100, 0)  # Position to start writing
t.pendown()

# Write the text
t.write("Ashraful", font=("Arial", 36, "bold"))

# Hide the turtle and keep window open
t.hideturtle()
screen.mainloop()

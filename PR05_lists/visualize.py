import turtle

def draw_point(color, x, y):
  ''' 
      Parameters: a color (string), an x-coord (float) and a y-coord (float)
      Returns: nothing

      Does: Draws a single point at the (x,y) indicated in the color indicated.
  '''

  turtle.color(color)
  turtle.penup()
  turtle.goto(x, y)
  turtle.pendown()
  turtle.dot()
  

def get_corner(i):
  '''
  Parameters: i (int), between 0-11 (inclusive)
  Returns: tuple (float, float), gives x, y coordinates indicating the 
           lower lefthand corner of a single plot's canvass

  Does: Defines a canvass corner for subplot in position i
  '''

  corners = { 
  0 : (-300, 150),
  1: (-150, 150), 
  2 : (0, 150),
  3: (150, 150),
  4 : (-300, -50),
  5: (-150, -50), 
  6 : (0, -50),
  7: (150, -50),
  8 : (-300, -250),
  9: (-150, -250), 
  10 : (0, -250),
  11: (150, -250),
  }

  return corners[i]


def adjust(i, x, y):
  '''
  Parameters: i (int), between 0-11 (inclusive)
                x (float), a single x coordinate
                y (floay), a single y coordinate 
  Returns: new_x (float), an adjusted x coordinate
             new_y (float), an adjusted y coordinate

  Does: Adjusts given xy coordinates for the canvanss in position i
  '''

  x_corner, y_corner = get_corner(i)

  new_x = x_corner + x
  new_y = y_corner + y

  return new_x, new_y


def write_stats(i, x_mean, y_mean, x_sd, y_sd):
  '''
    Parameters: i (int), between 0-11 (inclusive)
                x_mean, y_mean, x_sd, y_sd (all floats)
    Returns: nothing

    Does: Prints summary statistics for the plot in position i
  '''

  x_corner, y_corner = get_corner(i)

  turtle.penup()
  turtle.goto(x_corner, y_corner + 160)
  turtle.pendown()
  turtle.write('x mean: %.2f' %x_mean, font=("Arial", 14, "normal"))

  turtle.penup()
  turtle.goto(x_corner, y_corner + 145)
  turtle.pendown()
  turtle.write('y mean: %.2f' %y_mean, font=("Arial", 14, "normal"))

  turtle.penup()
  turtle.goto(x_corner, y_corner + 130)
  turtle.pendown()
  turtle.write('x sd: %.2f' %x_sd, font=("Arial", 14, "normal"))

  turtle.penup()
  turtle.goto(x_corner, y_corner + 115)
  turtle.pendown()
  turtle.write('y sd: %.2f' %y_sd, font=("Arial", 14, "normal"))




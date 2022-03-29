import turtle
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count = 0
    while(n != 1):
        count = count + 1
        if(n % 2) == 0:
             n = n // 2
            
        else:            
            n = n * 3 + 1
    return count                    



def graphing_of_data(upperbound):
    wn = turtle.Screen()
    wn.setworldcoordinates(0,0,10,10)
    writer = turtle.Turtle()
    writer.speed(3)
    graph = turtle.Turtle()
    graph.speed(3)
    writer.penup()
    graph.up()
    writer.goto(0,0)
    writer.down()
    current_max=0
    for i in range(1,upperbound):
      result=seq3np1(i)
      if(result>current_max):
        current_max=result
        graph.clear()
        graph.goto(0,current_max)
        str="Maximum so far: {}, {}".format(0,current_max)
        graph.write(str)
      writer.goto(i,result)
      wn.setworldcoordinates(0,0,i+10,current_max+10)
  #wn.exitonclick()

def main():
    start = int(input("Upper Bound Of Range: "))
    if start <= 0 :
      exit()
    for i in range(1,(start + 1)):   
      iterations = seq3np1(i)
      print("Current Maximum So Far Is", i, "And Number Of Iterations Is",  iterations)
    graphing_of_data(upperbound=start)


main()
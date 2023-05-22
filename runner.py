from board_tile import *
import turtle

def start_game():
    window = turtle.Screen()
    window.title("Cryptid")
    turtle.speed(0)
    turtle.tracer(0,0)
    turtle.hideturtle()
    my_board = Board()
    my_board.draw_board()
    turtle.update()
    turtle.done()

if __name__ == "__main__":
    start_game()
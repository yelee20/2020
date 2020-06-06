from graphics import *

def main():
    win = GraphWin("Number Baseball Game",500,500)
    win.setBackground('black')
    
    input_box = Entry(Point(250,250),10)
    input_box.draw(win)
    s = input_box.getText()

    txt = Text(Point(250,280), s)
    txt.draw(win)
    
    win.getMouse()
    win.close()

main()
"""
This is a simple snake game .
Author : userAnonymous
GitHub : https://github.com/ramimk0bir

You can import and run the game from Python code:

```python
import windoows_snake_game as snake_game

snake_game.play()
```
## Parameters of `play` function

| Parameter     | Type            | Default | Description                                      |
| ------------- | --------------- | ------- | ------------------------------------------------ |
| `speed`       | int             | 5       | Controls the game speed (higher = faster).       |
| `food_emoji`  | str             | "🍎"   | Emoji to represent the food on the grid.         |
| `grid_size`   | tuple (int,int) | (15,12) | Size of the game grid as (width, height).        |
| `block_emoji` | str             | "🟫"   | Emoji or character to represent the grid blocks. |

"""
import random
import os
import threading
import time




import sys
if sys.platform.startswith('win'):
    import msvcrt
elif sys.platform.startswith('linux'):
    import tty
    import termios
class KeyboardHandling :
    def __init__(self) :
        pass
    def windows():
        key=-1
        first_char= msvcrt.getche()
        if first_char == b'\xe0':
            second_char = msvcrt.getch()
            if second_char == b'H':
                key =0
            elif second_char == b'M' :
                key=3
            elif second_char == b'P' :
                key=2
            elif second_char == b'K' :
                key=1

        elif  first_char == b'w' or \
            first_char== b'8' :
            key =0
        elif  first_char == b'd' or \
            first_char== b'6' :
            key=3
        elif  first_char == b's' or \
            first_char== b'2' :
            key=2
        elif  first_char == b'a' or \
            first_char== b'4' :
            key=1
        elif first_char ==b' '  :
            key=4
        return key
    def linux():
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)

        try:
            tty.setraw(fd)
            ch1 = sys.stdin.read(1)
            if ch1 == '\x1b':
                ch2 = sys.stdin.read(1)
                if ch2 == '[':
                    ch3 = sys.stdin.read(1)
                    if ch3 == 'A':
                        return 0
                    elif ch3 == 'B':
                        return 2
                    elif ch3 == 'C':
                        return 3
                    elif ch3 == 'D':
                        return 1
                return -1
            elif  str(ch1) == "w" :
                return 0
            elif  str(ch1) == "d" :
                return 3
            elif  str(ch1) == "s" :
                return 2
            elif  str(ch1) == "a" :
                return 1
            elif str(ch1) == " ":
                return 4

            else :
                return -1

        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)


def handle_keyboard() :
    __KeyboardHandling=KeyboardHandling()
    if sys.platform.startswith('win'):
        return KeyboardHandling.windows()
    elif sys.platform.startswith('linux'):
        return KeyboardHandling.linux()


    else:
        raise "This game made for windows and linux "
        exit()


class Snake_Game :
    def __init__(self,invisible_wall=False):
        self.invisible_wall=invisible_wall
        self.pressedKey=-1
        self.operationalKey=-1
        self.snake_body=[(1,1)]
        self.isGamePaused=0
        self.food=-1
        self.__score=-2
        self.game_over_var=False



    def __score_bar(self,score,length:int=20):

        if length  <= 5 :
            length=5
        else :
            length=length
        return f"""{"".join(["-" for x in range(length*2+2)  ])}
|{f"Score:{score+1}".center(length*2)}|
{"".join(["-" for x in range(length*2+2)  ])}
"""



    def __base_replace(self,base_text,text,x,y):
        x-=1
        y-=1
        base=base_text

        base2=[]
        for index,line in enumerate(base.split('\n')):
            if index == y:
                line= line [:x+1]+text+ line[x+2:]
            base2.append(line)
        return  '\n'.join(base2)

    def print_loop(self,speed:int=5,food_emoji :str= "🍎" ,grid_size : tuple = (20,20) ,block_emoji:str= "🔲" ):

        
        length=grid_size[0]
        width=grid_size[1]


        base_line=  f"|{''.join([block_emoji for x in range(length)])}|"
        base=""
        for anything in range(width):
            base+=base_line+"\n"

        line="-"*(2*(length+1))

        while True:

            lastNode=self.snake_body[-1]
            x=self.snake_body[0][0]
            y=self.snake_body[0][1]
            if self.isGamePaused  :
                pass
            elif (abs(self.operationalKey-self.pressedKey)==2)  :
                X=x
                Y=y
                if self.pressedKey==0:
                    Y+=1
                elif self.pressedKey==2:
                    Y-=1
                elif self.pressedKey==1:
                    X+=1
                elif self.pressedKey==3:
                    X-=1
                self.snake_body.insert(0,(X,Y))
                self.snake_body.pop()
            elif self.pressedKey==0  :
                self.snake_body.insert(0,(x,y-1))
                self.snake_body.pop()
                self.operationalKey=0
            elif self.pressedKey==1:
                self.snake_body.insert(0,(x-1,y))
                self.snake_body.pop()
                self.operationalKey=1
            elif self.pressedKey==2 :
                self.snake_body.insert(0,(x,y+1))
                self.snake_body.pop()
                self.operationalKey=2
            elif self.pressedKey==3 :
                self.snake_body.insert(0,(x+1,y))
                self.snake_body.pop()
                self.operationalKey=3

            temp_base=self.__base_replace(base,"+",0,0)
            for index,item in enumerate (self.snake_body):
                if index == 0:
                    temp_base=self.__base_replace(temp_base, "🐸", item[0], item[1])
                    continue
                temp_base=self.__base_replace(temp_base,"🟩", item[0], item[1])
            if self.food == -1 :
            # if 1==1:
                self.food=( random.randint(1,length),random.randint(1,width)       )
                self.__score+=1
            else :
                if self.food==self.snake_body[0] :
                    temp_base=self.__base_replace(temp_base,   "\033[31m🐸\033[32m"      , self.food[0], self.food[1])
                elif self.food in self.snake_body :
                    temp_base=self.__base_replace(temp_base,   "\033[31m❌\033[32m"      , self.food[0], self.food[1])
                else :  
                    temp_base=self.__base_replace(temp_base,   f"\033[31m{food_emoji}\033[32m"      , self.food[0], self.food[1])
            if length  <= 5 :
                cli_length=5
            else :
                cli_length=length
            game_over =f"""
    {"".join(["-" for x in range(cli_length*2+2)  ])}
    |{"Game Over".center(cli_length*2)}|
    |{f"Score:{self.__score+1}".center(cli_length*2)}|
    {"".join(["-" for x in range(cli_length*2+2)  ])}
    Press crtl+c to end the game .
    """
            

            if self.snake_body[0][1] >=width+1 or not self.snake_body[0][1] :
                print("\033[H\033[J", end="")  # ANSI escape code to clear screen
                print("\033[91m" +game_over+"\033[0m\n")
                self.game_over_var=True
                break
            elif self.snake_body[0][0] >=length+1 or not self.snake_body[0][0]  :
                print("\033[H\033[J", end="") 
                print("\033[91m" +game_over+"\033[0m\n")
                self.game_over_var=True
                break
            elif any( not self.snake_body.count(x)<=1  for x in self.snake_body  ) :
                print("\033[H\033[J", end="") 
                print("\033[91m" +game_over+"\033[0m\n")
                self.game_over_var=True
                break
            if self.food == self.snake_body[0]:
            # if 1==1 :
                self.snake_body.insert(-1,self.snake_body[-1])
                self.food=-1
            main_base = self.__score_bar(self.__score,length=length)+ line+'\n'+temp_base+line
            print("\033[H\033[J", end="")  # ANSI escape code to clear screen
            print("\033[92m" +main_base+"\033[0m\n")



            time.sleep(1 / speed if speed > 0 else 0.5)  # uses speed argument

    def check_keys(self):
        while (not self.game_over_var ):
            try :
                pressedKey=handle_keyboard()
                if pressedKey == -1 :
                    pass
                elif pressedKey == 4 :
                    self.isGamePaused = not self.isGamePaused
                if pressedKey == 0 or \
                        pressedKey == 1 or \
                        pressedKey == 2 or \
                        pressedKey == 3 :
                    self.pressedKey=pressedKey
            except KeyboardInterrupt:
                print("\nProgram stopped.")
                break






def play(speed:int=5,food_emoji :str= "🍎",grid_size : tuple = (15,12 ),block_emoji:str="🟫" ,invisible_wall=False,debug=False) :
    try :

        game=Snake_Game(invisible_wall=invisible_wall)
        threading.Thread(
        target=game.check_keys,
            daemon=True
        ).start()

        # Await the async print loop
        game.print_loop(
            speed=speed, 
            food_emoji=food_emoji, 
            grid_size=grid_size, 
            block_emoji=block_emoji
        )

    except  KeyboardInterrupt :
        print("Program stopped.") 
    except Exception as e :
        if debug:
            import traceback
            traceback.print_exc()  # Verbose error with full traceback
        else:
            print(f"{str(e)}\nIf user wants verbose error, set play's debug = True")
if __name__ == "__main__":
    try:
        speed=5

        # asyncio.run(main_async())
        play(debug=1)
    except KeyboardInterrupt:
        print("Program stopped.")


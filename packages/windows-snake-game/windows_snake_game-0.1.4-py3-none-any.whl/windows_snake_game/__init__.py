"""
This is a simple snake game .
Author : userAnonymous
GitHub : https://github.com/ramimk0bir

You can import and run the game from Python code:

```python
import windoows_snake_game as snake_game

snake_game.play(speed=5, food_emoji="🍎", grid_size=(20,20), block_emoji="▮")
```
## Parameters of `play` function

| Parameter     | Type            | Default | Description                                      |
| ------------- | --------------- | ------- | ------------------------------------------------ |
| `speed`       | int             | 5       | Controls the game speed (higher = faster).       |
| `food_emoji`  | str             | "🍎"   | Emoji to represent the food on the grid.         |
| `grid_size`   | tuple (int,int) | (15,12) | Size of the game grid as (width, height).        |
| `block_emoji` | str             | "🟫"   | Emoji or character to represent the grid blocks. |

"""
import asyncio
import random
import os


class Snake_Game :
    def __init__(self,invisible_wall=False):
        self.invisible_wall=invisible_wall
        self.pressedKey=-1
        self.operationalKey=-1
        self.snake_body=[(1,1)]
        self.isGamePaused=0
        self.food=-1
        self.__score=-2




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

    async def __print_loop(self,speed:int=5,food_emoji :str= "🍎" ,grid_size : tuple = (20,20) ,block_emoji:str= "🔲" ):

        
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
                break
            elif self.snake_body[0][0] >=length+1 or not self.snake_body[0][0]  :
                print("\033[H\033[J", end="") 
                print("\033[91m" +game_over+"\033[0m\n")
                break
            elif any( not self.snake_body.count(x)<=1  for x in self.snake_body  ) :
                print("\033[H\033[J", end="") 
                print("\033[91m" +game_over+"\033[0m\n")
                break
            if self.food == self.snake_body[0]:
            # if 1==1 :
                self.snake_body.insert(-1,self.snake_body[-1])
                self.food=-1
            main_base = self.__score_bar(self.__score,length=length)+ line+'\n'+temp_base+line
            print("\033[H\033[J", end="")  # ANSI escape code to clear screen
            print("\033[92m" +main_base+"\033[0m\n")



            await asyncio.sleep(1 / speed if speed > 0 else 0.5)  # uses speed argument

    async def __check_keys(self,custom_keyboard):
        custom_keyboard_handler=custom_keyboard()
        while True:

            if custom_keyboard_handler.is_pressed('up'):
                self.pressedKey=0
            elif custom_keyboard_handler.is_pressed('left'):
                self.pressedKey=1
            elif custom_keyboard_handler.is_pressed('down'):
                self.pressedKey=2
            elif custom_keyboard_handler.is_pressed('right'):
                self.pressedKey=3
            elif custom_keyboard_handler.is_pressed('space') :
                self.isGamePaused = not self.isGamePaused
            await asyncio.sleep(.1)

    async def main_async(self,custom_keyboard,speed:int=5,food_emoji :str= "🍎",grid_size : tuple = (1,1 ),block_emoji:str= "🔲" ):

        await asyncio.gather( self.__check_keys(custom_keyboard),self.__print_loop(speed=speed,food_emoji=food_emoji,grid_size=grid_size,block_emoji=block_emoji))

class custom_keyboard :
    def __init__(self):

        try :
            from pynput import keyboard
        # this is if module not found
        except ModuleNotFoundError:
            os.system("pip install pynput")
            from pynput import keyboard
        except Exception as e :
            print("install pynput with pip install pynput")
            raise e
        self.Key=keyboard.Key
        
        self.keyboard=keyboard
        self.pressed_keys = set()

        self.listener = self.keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
    def on_press(self,key):
        self.pressed_keys.add(key)

    def on_release(self,key):
        if key in self.pressed_keys:
            self.pressed_keys.remove(key)

    def is_pressed(self,key_name):
        # Convert string like "space" to pynput Key or character
        try:
            key = getattr(self.Key, key_name)
        except AttributeError:
            # Not a special key, check char key
            key = key_name

        return key in self.pressed_keys




def play(speed:int=5,food_emoji :str= "🍎",grid_size : tuple = (15,12 ),block_emoji:str="🟫" ,invisible_wall=False,debug=False) :
    try :

        game=Snake_Game(invisible_wall=invisible_wall)
        asyncio.run(game.main_async(custom_keyboard,speed=speed,food_emoji =food_emoji ,grid_size = grid_size,block_emoji=block_emoji ))    


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
        play()
    except KeyboardInterrupt:
        print("Program stopped.")


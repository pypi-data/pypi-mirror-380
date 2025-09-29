"""
This is a simple snake game .
Author : userAnonymous
GitHub : https://github.com/ramimk0bir

You can import and run the game from Python code:

```python
import windoows_snake_game as snake_game

snake_game.main(speed=5, food_emoji="🍎", grid_size=(20,20), block_emoji="▮")
```
## Parameters of `main` function

| Parameter     | Type            | Default | Description                                      |
| ------------- | --------------- | ------- | ------------------------------------------------ |
| `speed`       | int             | 5       | Controls the game speed (higher = faster).       |
| `food_emoji`  | str             | "🍎"   | Emoji to represent the food on the grid.         |
| `grid_size`   | tuple (int,int) | (20,20) | Size of the game grid as (width, height).        |
| `block_emoji` | str             | "🟫"   | Emoji or character to represent the grid blocks. |

"""
import asyncio
import random
import os


pressedKey=-1
operationalKey=-1
snake_body=[(1,1)]
isGamePaused=0

food=-1
score=-2






def score_bar(score,length:int=20):

    if length  <= 5 :
        length=5
    else :
        length=length
    return f"""
{"".join(["-" for x in range(length*2+2)  ])}
|{f"Score:{score+1}".center(length*2)}|
{"".join(["-" for x in range(length*2+2)  ])}
"""



def base_replace(base_text,text,x,y):
    x-=1
    y-=1
    base=base_text

    base2=[]
    for index,line in enumerate(base.split('\n')):
        if index == y:
            line= line [:x+1]+text+ line[x+2:]
        base2.append(line)
    return  '\n'.join(base2)

async def print_loop(speed:int=5,food_emoji :str= "🍎" ,grid_size : tuple = (20,20) ,block_emoji:str= "🔲" ):
    global pressedKey,operationalKey,snake_body,food,score,isGamePaused
    length=grid_size[0]
    width=grid_size[1]


    base_line=  f"|{''.join([block_emoji for x in range(length)])}|"
    base=""
    for anything in range(width):
        base+=base_line+"\n"

    line="-"*(2*(length+1))

    while True:
        
        lastNode=snake_body[-1]
        x=snake_body[0][0]
        y=snake_body[0][1]
        if isGamePaused  :
            pass
        elif (abs(operationalKey-pressedKey)==2)  :
            X=x
            Y=y
            if pressedKey==0:
                Y+=1
            elif pressedKey==2:
                Y-=1
            elif pressedKey==1:
                X+=1
            elif pressedKey==3:
                X-=1
            snake_body.insert(0,(X,Y))
            snake_body.pop()
        elif pressedKey==0  :
            snake_body.insert(0,(x,y-1))
            snake_body.pop()
            operationalKey=0
        elif pressedKey==1:
            snake_body.insert(0,(x-1,y))
            snake_body.pop()
            operationalKey=1
        elif pressedKey==2 :
            snake_body.insert(0,(x,y+1))
            snake_body.pop()
            operationalKey=2
        elif pressedKey==3 :
            snake_body.insert(0,(x+1,y))
            snake_body.pop()
            operationalKey=3

        temp_base=base_replace(base,"+",0,0)
        for index,item in enumerate (snake_body):
            if index == 0:
                temp_base=base_replace(temp_base, "🐸", item[0], item[1])
                continue
            temp_base=base_replace(temp_base,"🟩", item[0], item[1])
        if food == -1 :
        # if 1==1:
            food=( random.randint(1,length),random.randint(1,width)       )
            score+=1
        else :
            if food==snake_body[0] :
                temp_base=base_replace(temp_base,   "\033[31m🐸\033[32m"      , food[0], food[1])
            elif food in snake_body :
                temp_base=base_replace(temp_base,   "\033[31m❌\033[32m"      , food[0], food[1])
            else :  
                temp_base=base_replace(temp_base,   f"\033[31m{food_emoji}\033[32m"      , food[0], food[1])
        if length  <= 5 :
            cli_length=5
        else :
            cli_length=length
        game_over =f"""
{"".join(["-" for x in range(cli_length*2+2)  ])}
|{"Game Over".center(cli_length*2)}|
|{f"Score:{score+1}".center(cli_length*2)}|
{"".join(["-" for x in range(cli_length*2+2)  ])}
Press crtl+c to end the game .
"""
        

        if snake_body[0][1] >=width+1 or not snake_body[0][1] :
            print("\033[H\033[J", end="")  # ANSI escape code to clear screen
            print("\033[91m" +game_over+"\033[0m\n")
            break
        elif snake_body[0][0] >=length+1 or not snake_body[0][0]  :
            print("\033[H\033[J", end="") 
            print("\033[91m" +game_over+"\033[0m\n")
            break
        elif any( not snake_body.count(x)<=1  for x in snake_body  ) :
            print("\033[H\033[J", end="") 
            print("\033[91m" +game_over+"\033[0m\n")
            break
        if food == snake_body[0]:
        # if 1==1 :
            snake_body.insert(-1,snake_body[-1])
            food=-1
        main_base = score_bar(score,length=length)+ line+'\n'+temp_base+line
        print("\033[H\033[J", end="")  # ANSI escape code to clear screen
        print("\033[92m" +main_base+"\033[0m\n")
        await asyncio.sleep(1 / speed if speed > 0 else 0.5)  # uses speed argument

async def check_keys(custom_keyboard):
    global pressedKey,isGamePaused
    custom_keyboard_handler=custom_keyboard()
    while True:
        if custom_keyboard_handler.is_pressed('up'):
            pressedKey=0
        elif custom_keyboard_handler.is_pressed('left'):
            pressedKey=1
        elif custom_keyboard_handler.is_pressed('down'):
            pressedKey=2
        elif custom_keyboard_handler.is_pressed('right'):
            pressedKey=3
        elif custom_keyboard_handler.is_pressed('space') :
            isGamePaused = not isGamePaused
        await asyncio.sleep(.1)

async def main_async(custom_keyboard,speed:int=5,food_emoji :str= "🍎",grid_size : tuple = (20,20 ),block_emoji:str= "🔲" ):
    await asyncio.gather( check_keys(custom_keyboard),print_loop(speed=speed,food_emoji=food_emoji,grid_size=grid_size,block_emoji=block_emoji))




def main(speed:int=5,food_emoji :str= "🍎",grid_size : tuple = (15,12 ),block_emoji:str="🟫" ) :
    try :
        global    pressedKey,operationalKey, snake_body, isGamePaused, food,score
        pressedKey=-1
        operationalKey=-1
        snake_body=[(1,1)]
        isGamePaused=0

        food=-1
        score=-2

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
        


        asyncio.run(main_async(custom_keyboard,speed=speed,food_emoji =food_emoji ,grid_size = grid_size,block_emoji=block_emoji ))    
    except  KeyboardInterrupt :
        print("Program stopped.") 
    except Exception as e :
        raise e
        print(str(e))
if __name__ == "__main__":
    try:
        speed=5

        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("Program stopped.")


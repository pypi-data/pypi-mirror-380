"""


This is a simple snake game .
Author : userAnonymous
GitHub : https://github.com/ramimk0bir
## Author

* **userAnonymous**
* GitHub: [ramimK0bir](https://github.com/ramimk0bir)

---

## Installation

Install the game easily using pip:

```bash
pip install python-snake-game
```

---

## Usage



You can import and run the game from Python code:

```python
import python_snake_game as snake_game

snake_game.play()

```

---

## Parameters of `play` function

| Parameter     | Type            | Default | Description                                      |
| ------------- | --------------- | ------- | ------------------------------------------------ |
| `speed`       | int             | 5       | Controls the game speed (higher = faster).       |
| `food_emoji`  | str             | "🍎"   | Emoji to represent the food on the grid.         |
| `grid_size`   | tuple (int,int) | (15,12) | Size of the game grid as (width, height).        |
| `block_emoji` | str             | "🟫"   | Emoji or character to represent the grid blocks. |

---"""


import random 
import time 
from .utilities import   handle_keyboard  

import asyncio
import os

def clear_terminal():

    os.system('cls' if os.name == 'nt' else 'clear')
def get_scorebar(score, length):
    GREEN = "\033[92m"
    RESET = "\033[0m"
    if length < 5:
        length = 5

    return f"""{GREEN}{"".join("-" for x in range(2*length))}
|{f"score:{score}".center(2*length-2)}|
{"".join("-" for x in range(2*length))}{RESET}"""

def get_gameovere_bar(score, length):
    RED = "\033[91m"
    RESET = "\033[0m"
    clear_terminal()

    if length < 5:
        length = 5
    print(f"""{RED}{"".join("-" for x in range(2*length))}
|{"Game Over".center(2*length-1)}|
|{f"score:{score}".center(2*length-1)}|
{"".join("-" for x in range(2*length))}{RESET}""")


def get_text_from_charmap_only(char_map):

    xs = [x for (x, y) in char_map]
    ys = [y for (x, y) in char_map]

    max_x = max(xs)
    max_y = max(ys)

    result = ""
    for y in range(max_y + 1):
        row_str = ""
        for x in range(max_x + 1):
            row_str += char_map[(x, y)]  # assumes all cells filled
        result += row_str + "\n"
    return result

class SnakeGame :
    def __init__ (self,snake_food_emoji = "🍎",speed :int =2, snake_head_emoji :str ="" , background_emoji  :str =""  ,invisible_wall :bool =False ,grid_size :tuple[int, int] = (10,10) ,snake_body_emoji ="🟩"  ) :
        clear_terminal()
        self.snake_body_emoji=snake_body_emoji
        self.snake_head_emoji=snake_head_emoji
        self.background_emoji=background_emoji
        self.snake_food_emoji=snake_food_emoji
        self.invisible_wall=invisible_wall
        self.grid_size=grid_size
        self.board=[  ( i,x)   for i in range(grid_size[0]) for x in range(grid_size[1])   ] 
        self.__score=0
        self.speed=speed
        if self.speed > 10 :
            self.speed=10
        if self.speed < 1 :
            self.speed=1
        self.game_over=False
        self.pressed_key=-5
        self.second_last_pressed_key=-5
        self.snake_body=[(0,0)]
        self.game_paused=False
        self.food=-1
        self.last_keys=[]
    async def mainloop (self):
        while (not self.game_over) :
            try :
                if (
                     self.pressed_key==-1 or \
                    ( self.pressed_key==-5 and \
                        self.second_last_pressed_key==-5    ) 
                ):

                    pass
                else :
                    self.second_last_pressed_key = self.pressed_key
                    try :
                        if self.pressed_key != self.last_keys[0] and abs(self.pressed_key-self.last_keys[0])!=2 and \
                            self.pressed_key in [0,1,2,3] :
                            self.last_keys.insert(0, self.pressed_key)

                    except :
                        self.last_keys.insert(0,self.pressed_key) 
                if len(self.last_keys)>2 :
                    self.last_keys.pop()
                if len(self.last_keys)==1 :
                    if self.last_keys[0]==3 :
                        for index, item in enumerate (self.snake_body ):
                            if index==0 :
                                head=self.snake_body[0]
                                self.snake_body[index]=(item[0]+1, item[1])
                                self.snake_body.insert(1,head)
                                self.snake_body.pop()

                    elif self.last_keys[0]==2 :
                        for index, item in enumerate (self.snake_body ):
                            if index==0 :
                                head=self.snake_body[0]
                                self.snake_body[index]=(item[0], item[1]+1)
                                self.snake_body.insert(1, head)
                                self.snake_body.pop()
                    elif self.last_keys[0] in [0,1] and self.invisible_wall==False  :
                        self.game_over=True
                        get_gameovere_bar(self.__score, self.grid_size[0])

                elif len(self.last_keys) > 1 :
                    head=self.snake_body[0]
                    if self.last_keys.count(self.last_keys[0]) >1 :
                        pass


                    elif self.last_keys[0] == 3  :
                        
                        self.snake_body[0]=(head[0]+1, head[1])
                        self.snake_body.insert(1, head)
                        self.snake_body.pop()
                    elif self.last_keys[0]==0 :
                        self.snake_body[0]=(head[0], head[1]-1)
                        self.snake_body.insert(1, head)
                        self.snake_body.pop()      
                    elif self.last_keys[0] == 1 :
                        self.snake_body[0]=(head[0]-1, head[1])
                        self.snake_body.insert(1, head)
                        self.snake_body.pop()
                    elif self.last_keys[0] == 2 :
                        self.snake_body[0]=(head[0], head[1]+1)
                        self.snake_body.insert(1, head)
                        self.snake_body.pop()  
                    

                if len(set(self.snake_body)) < len(self.snake_body) :
                    self.game_over=True
                    get_gameovere_bar(self.__score , self.grid_size[0])
                if  self.food ==-1 :
                    self.food=random.choice(self.board)

                elif self.food ==self.snake_body[0] :
                    self.__score+=1
                    self.food=random.choice(self.board)
                    self.snake_body.append(self.snake_body[-1])

                if  not self.invisible_wall  :
                    if  any( x not in self.board  for x in  self.snake_body     ) :
                        self.game_over=True
                        get_gameovere_bar(self.__score,self.grid_size[0])
                        break
                else :
                    pass
                char_map = {
                    i : self.background_emoji for i in self.board 
                }

                for index,item in enumerate(self.snake_body) :
                    if index==0 :
                        char_map[item]=self.snake_head_emoji
                    else :
                        char_map[item]=self.snake_body_emoji

                if self.food not in self.snake_body :
                    char_map[self.food]=self.snake_food_emoji
                else :
                    char_map[self.food] = "❌"
                text = get_text_from_charmap_only( char_map) 
                lines = text.count("\n") + 4
                print(get_scorebar(self.__score,self.grid_size[0]))
                print(text)

                time.sleep((1 / self.speed if self.speed > 0 else 0.5)-0.1)
                await asyncio.sleep(.1)
                print("\033[F" * lines, end="")

            except KeyboardInterrupt :
                break



    async def keyboard_handling (self): 
        while (not self.game_over) :
            try :
                self.pressed_key= handle_keyboard()
                if self.pressed_key ==4 :
                    self.game_paused=True
                elif self.pressed_key==5 :
                    self.game_over=True
                    print("Game closed by user.")
                    break
            except KeyboardInterrupt :
                self.game_over=True
                get_gameovere_bar(self.__score,self.grid_size[0])
                break

            await asyncio.sleep(0.1)

    async def async_run (self) :
            await asyncio.gather(self.keyboard_handling(), self.mainloop())

    def run(self):
        try :
            asyncio.run(self.async_run())
        except KeyboardInterrupt :
            print("Game closed by user.")

def play (speed = 2 , snake_head_emoji = "🐸",snake_body_emoji="🟩",  background_emoji = "🟫" ,invisible_wall =False, grid_size=(15,12)) :
    snake_game=SnakeGame(speed=speed ,background_emoji=background_emoji ,grid_size= grid_size,invisible_wall=invisible_wall,snake_head_emoji=snake_head_emoji,snake_body_emoji=snake_body_emoji)
    snake_game.run()

if __name__== "__main__" :
    play(grid_size=(15,12),speed=5)
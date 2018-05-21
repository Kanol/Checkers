from tkinter import *


class Drawing:
    def __init__(self, width, height, pixel_size):
        self.width = width
        self.height = height
        self.pixel_size = pixel_size
        self.master = Tk()
        self.window = Canvas(self.master, width=self.width * self.pixel_size, height=self.height * self.pixel_size)
        for x in range(self.width):
            for y in range(self.height):
                if (x + y) % 2 == 0:
                    color = "white"
                else:
                    color = "black"
                self.window.create_rectangle(x * self.pixel_size, y * self.pixel_size,
                                             (x + 1) * self.pixel_size, (y + 1) * self.pixel_size,
                                             fill=color, width=0)

    def main(self):
        self.window.pack()
        self.master.mainloop()

    def draw_checkers(self, checkers_field):
        for checker in checkers_field:
            print(checker.x * self.pixel_size)
            self.window.create_oval(checker.x * self.pixel_size, checker.y * self.pixel_size, (checker.x + 1) * self.pixel_size - 1, (checker.y + 1) * self.pixel_size - 1,
                                             fill=checker.color, width=0)

    def clear_screen(self):
        for x in range(self.width):
            for y in range(self.height):
                if self.memory[x][y] != 0:
                    self.memory[x][y] = 0
                    self.update_pixel(x, y)

    def update_pixel(self, pixel_x, pixel_y):
        if self.memory[pixel_x][pixel_y] == 0:
            color = "black"
        else:
            color = "white"
        self.window.itemconfig(self.pixels[pixel_x][pixel_y], fill=color)

    def draw_sprite(self, x, y, sprite):
        output = 0
        for sprite_y in range(len(sprite)):
            for sprite_x in range(len(sprite[sprite_y])):  # Sprite is reversed
                if x + sprite_x >= self.width or y + sprite_y >= self.height:
                    continue
                if self.memory[x + sprite_x][y + sprite_y] == 1 and int(sprite[sprite_y][sprite_x]) == 1:
                    output = 1
                self.memory[x + sprite_x][y + sprite_y] ^= int(sprite[sprite_y][sprite_x])
                self.update_pixel(x + sprite_x, y + sprite_y)
        return output

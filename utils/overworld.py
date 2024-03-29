'''
Gurjas Dhillon
overworld.py
This file contains the Overworld class where the user can decide to switch between levels
'''

import pygame
from utils.support import import_sprite_sheet, import_csv
from utils.overworldTiles.terrain import Terrain
from utils.overworldTiles.player import Player
from utils.menu import Menu
from config import config

# normally the levels are in 16x16 style format but this one is scaled up by a factor of 2
TILESIZE = 32

class Overworld:
    def __init__(self, screen):
        self.screen = screen
        self.player = config.overworld_player

        # menu stuff (press q in overworld if you haven't already)
        self.game_paused = False
        self.menu = Menu()

        # everything related to the houses
        self.house_csv = import_csv("levels/overworld/overworld_houses.csv")
        self.house_imgs = import_sprite_sheet("assets/overworld/house.png", (16, 16), (32, 32))
        self.house_sprites = self.create_group("house")

        # limits -> where and where can't the user go
        self.limit_csv = import_csv("levels/overworld/overworld_contraints.csv")
        self.limit_sprites = self.create_group("limit")

        # creating groups for all the levels
        self.lvl1_sprites = self.create_group("lvl1")
        self.lvl2_sprites = self.create_group("lvl2")
        self.lvl3_sprites = self.create_group("lvl3")
        self.lvl4_sprites = self.create_group("lvl4")
        self.lvl5_sprites = self.create_group("lvl5")
        self.lvl6_sprites = self.create_group("lvl6")

        # bundle all the lvls into 1 big list so that you can just loop over it later rather than check them all individually
        self.lvl_sprites = [self.lvl1_sprites, self.lvl2_sprites, self.lvl3_sprites, self.lvl4_sprites, self.lvl5_sprites, self.lvl6_sprites]

        # everything related to the water
        self.water_csv = import_csv("levels/overworld/overworld_water.csv")
        self.water_imgs = import_sprite_sheet("assets/overworld/water.png", (16, 16), (32, 32))
        self.water_sprites = self.create_group("water")

        # water details i.e. boat
        self.water_details_csv = import_csv("levels/overworld/overworld_water_details.csv")
        self.water_details_sprites = self.create_group("water_details")

        # everything related to nature -> trees bushes
        self.nature_csv = import_csv("levels/overworld/overworld_nature.csv")
        self.nature_imgs = import_sprite_sheet("assets/overworld/nature.png", (16, 16), (32, 32))
        self.nature_sprites = self.create_group("nature")

        # the terrain are the tiles underneath the houses
        self.terrain_csv = import_csv("levels/overworld/overworld_terrain.csv")
        self.terrain_imgs = import_sprite_sheet("assets/overworld/terrain.png", (16, 16), (32, 32))
        self.terrain_sprites = self.create_group("terrain")

        # the floor is everything where the player can walk
        self.floor_csv = import_csv("levels/overworld/overworld_floor.csv")
        self.floor_imgs = import_sprite_sheet("assets/overworld/floor.png", (16, 16), (32, 32))
        self.floor_sprites = self.create_group("floor")

        # contains where the player starts and ends
        self.player_csv = import_csv("levels/overworld/overworld_floor.csv")
        self.player_sprites = self.create_group("player")

    # creating the tiles for terrains and lvls
    def create_group(self, type):
        group = pygame.sprite.Group()

        for x, row in enumerate(self.house_csv):
            for y, val in enumerate(row):
                posX = y * TILESIZE
                posY = x * TILESIZE

                if type == "terrain":
                    sprite = Terrain(posX, posY, self.terrain_imgs, int(self.terrain_csv[x][y]))
                    group.add(sprite)
                
                elif type == "nature":
                    sprite = Terrain(posX, posY, self.nature_imgs, int(self.nature_csv[x][y]))
                    group.add(sprite)
                
                elif type == "floor":
                    sprite = Terrain(posX, posY, self.floor_imgs, int(self.floor_csv[x][y]))
                    group.add(sprite)
                
                elif type == "house":
                    sprite = Terrain(posX, posY, self.house_imgs, int(self.house_csv[x][y]))
                    group.add(sprite)
                
                elif type == "water":
                    sprite = Terrain(posX, posY, self.water_imgs, int(self.water_csv[x][y]))
                    group.add(sprite)
                
                elif type == "water_details":
                    sprite = Terrain(posX, posY, self.water_imgs, int(self.water_details_csv[x][y]))
                    group.add(sprite)
                
                elif type == "player" and self.player_csv[x][y] == "1":
                    group = pygame.sprite.GroupSingle()
                    self.start_pos = (posX, posY)
                    sprite = Player((posX, posY), self.screen, self.limit_sprites, self.lvl_sprites)
                    group.add(sprite)
                    return group

                elif type == "limit":
                    if self.limit_csv[x][y] == "-1":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl1":
                    if self.limit_csv[x][y] == "104":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)

                elif type == "lvl2":
                    if self.limit_csv[x][y] == "105":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl3":
                    if self.limit_csv[x][y] == "106":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)

                elif type == "lvl4":
                    if self.limit_csv[x][y] == "146":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl5":
                    if self.limit_csv[x][y] == "542":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
                elif type == "lvl6":
                    if self.limit_csv[x][y] == "558":
                        sprite = Terrain(posX, posY, self.house_imgs, 5)
                        group.add(sprite)
                
        
        return group

    # if the player was changed in the menu
    def check_name_changed(self):
        if config.overworld_player != self.player:
            self.player = config.overworld_player
            self.player_sprites.sprite.get_imgs(self.player)

    # reset the overworld so the player resets to the start
    def reset(self):
        self.__init__(self.screen)

    # toggling the menu
    def toggle(self):
        self.game_paused = not self.game_paused

    # this method will be called by the main function, all the stuff that will be going in the while loop will be called here
    def run(self):
        self.check_name_changed()

        self.terrain_sprites.draw(self.screen)
        self.terrain_sprites.update()

        self.water_sprites.draw(self.screen)
        self.water_sprites.update()

        self.water_details_sprites.draw(self.screen)
        self.water_details_sprites.update()

        self.nature_sprites.draw(self.screen)
        self.nature_sprites.update()

        self.floor_sprites.draw(self.screen)
        self.floor_sprites.update()

        self.player_sprites.draw(self.screen)
    
        self.house_sprites.draw(self.screen)
        self.house_sprites.update()

        
        if not self.game_paused:
            
            self.player_sprites.update()

        else:
            self.menu.display()


        
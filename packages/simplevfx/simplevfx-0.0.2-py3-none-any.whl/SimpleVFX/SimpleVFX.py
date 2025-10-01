import pygame
from enum import Enum
from os import listdir
from os.path import isfile, isdir, join
from typing import Any


# This class defines a set of enumerated values to specify the direction of VisualEffect images.
class ImageDirection(Enum):
    RIGHT = 0
    LEFT = 1
    TOP = 2
    BOTTOM = 3


# This class handles spawning and rendering the actual VisualEffect.
class VisualEffect:
    # @purpose:
    # instantiate the VisualEffect class
    # @scope:
    # private
    # @params:
    # source: a game object spawning the effect, which needs a rect (pygame.Rect or pygame.rect.Rect) attribute
    # image_master: a dictionary of images from the VisualEffectsManager class
    # image_name: a string, the name of the image_master key containing the image (case-insensitive, converted to uppercase)
    # direction (sometimes optional): an ImageDirection (enum defined in his file), defining both the image facing to load
    #           (if image mirrors were generated, in which case this parameter is required) and the alignment direction to lock
    #           the VisualEffects rect to the source's rect
    # rotation (optional): a float, the rotation degree at which to turn the image
    # alpha (optional): a float, the alpha opacity value at which to set the image
    # offset (optional): a tuple of 2 floats, the X (index 0) and Y (index 1) offset from the source rect at which the image should be spawned
    # scale (optional): a tuple of 2 floats, the width (index 0) and height (index 1) factor to which the image should be scaled
    # linked_to_source (optional): a boolean, specify whether to lock the image's location to its spawn point, or to move it with the source object
    # @returns:
    # none
    # @exceptions:
    # AttributeError, raised if the effect's source does not have a rect (pygame.Rect or pygame.rect.Rect) attribute
    def __init__(self, source: Any, image_master: dict[str, pygame.Surface] | dict[str, dict[ImageDirection, pygame.Surface]], image_name: str,
                 direction: ImageDirection | list[ImageDirection] | tuple[ImageDirection] | None=None, rotation: float=0, alpha: int=255,
                 offset: tuple[float, float]=(0.0, 0.0), scale: tuple[float, float]=(1.0, 1.0), linked_to_source: bool=False) -> None:
        if not hasattr(source, "rect"):
            raise AttributeError(f"Linked source of type {type(source)} must be of have a rect property.")
        else:
            self.source: Any = source

        self.image: pygame.Surface = image_master[image_name.upper()]
        if isinstance(self.image, dict):
            if isinstance(direction, ImageDirection) and direction in [ImageDirection.LEFT, ImageDirection.RIGHT]:
                self.image = self.image[direction]
            elif isinstance(direction, (list, tuple)):
                for valid_direction in direction:
                    if valid_direction in [ImageDirection.LEFT, ImageDirection.RIGHT]:
                        self.image = self.image[valid_direction]
                        break
            else:
                self.image = self.image[ImageDirection.RIGHT]

        if isinstance(direction, ImageDirection) or direction is None:
            self.direction: list[ImageDirection] = [direction]
        else:
            self.direction: list[ImageDirection] = direction

        self.offset: tuple[float, float] = offset

        if scale != (1, 1):
            self.image = pygame.transform.smoothscale(self.image, scale)
        if alpha != 255:
            self.image.set_alpha(alpha)
        if rotation != 0:
            self.image = pygame.transform.rotate(self.image, rotation)
        self.rect: pygame.Rect = self.image.get_rect()

        self.is_linked_to_source: bool = linked_to_source
        if not self.is_linked_to_source:
            self.__align__()

    # @purpose:
    # align the VisualEffect image to the source's location
    # @scope:
    # private
    # @params:
    # none, runs off instantiated values
    # @returns:
    # none
    # @exceptions:
    # none
    def __align__(self):
        if ImageDirection.LEFT in self.direction:
            self.rect.left = self.source.rect.left + self.offset[0]
        elif ImageDirection.RIGHT in self.direction:
            self.rect.right = self.source.rect.right - self.offset[0]
        else:
            self.rect.centerx = self.source.rect.centerx

        if ImageDirection.BOTTOM in self.direction:
            self.rect.bottom = self.source.rect.bottom - self.offset[1]
        elif ImageDirection.TOP in self.direction:
            self.rect.top = self.source.rect.top + self.offset[1]
        else:
            self.rect.centery = self.source.rect.centery

    # @purpose:
    # blit the VisualEffect's image to the screen
    # @scope:
    # public
    # @params:
    # screen: the pygame surface on which to blit the image
    # screen_offset (optional): a tuple of 2 floats, the X (index 0) and Y (index 1) offsets at which the image should be drawn on the screen
    #           the practical purpose of this is to render to the screen based on display coordinates (e.g. top left corner of your
    #           monitor is X=0, Y=0) while tracking game objects at coordinates based on the level, map, or other world abstraction
    #           (e.g. top left corner of the level, map, or world is X=0, Y=0)
    # @returns:
    # none
    # @exceptions:
    # none
    def draw(self, screen: pygame.Surface, screen_offset: tuple[float, float]=(0.0, 0.0)) -> None:
        if self.is_linked_to_source:
            self.__align__()
        screen.blit(self.image, (self.rect.x - screen_offset[0], self.rect.y - screen_offset[1]))


# This class handles loading all VisualEffect images into a single place, rather than loading separately for each generated effect,
# to optimize memory usage and performance.
class VisualEffectsManager:
    # @purpose:
    # instantiate the VisualEffectsManager class
    # @scope:
    # private
    # @params:
    # path: a string, the file path to the directory containing your VFX images
    # ext (optional): a string, list of strings, or tuple of strings, the valid file extensions to load
    # generate_mirrors (optional): a boolean, specify whether to generate mirrored left- and right-facing versions of the loaded
    # default_time (optional): a float, the default amount of time in which spawned VisualEffects should be kept alive
    # @returns:
    # none
    # @exceptions:
    # none
    def __init__(self, path: str, ext: str | list[str] | tuple[str] | None=None,
                 generate_mirrors: bool=True, default_time: float | None=None) -> None:
        if generate_mirrors:
            self.image_master: dict[str, dict[str, pygame.Surface]] | None = VisualEffectsManager.__generate_mirrors__(VisualEffectsManager.__load_images__(path, ext))
        else:
            self.image_master: dict[str, pygame.Surface] | None = VisualEffectsManager.__load_images__(path, ext)
        self.active_effects: dict[VisualEffect, float] = {}
        self.default_time: float | None = default_time

    # @purpose:
    # load images from a directory
    # @scope:
    # private
    # @params:
    # path: a string, the file path to the directory containing your VFX images
    # ext (optional): a string, list of strings, or tuple of strings, the valid file extensions to load
    # @returns:
    # a dictionary of loaded images, with keys = the uppercase file name minus any file extensions (splits at first period)
    # @exceptions:
    # FileNotFoundError, raised if no valid files are found at the specified directory
    # NotADirectoryError, raised if the specified path is not a directory
    @staticmethod
    def __load_images__(path: str, ext: str | list[str] | tuple[str] | None = None) -> dict[str, pygame.Surface] | None:
        if isdir(path):
            img_files: list[str] = [f for f in listdir(path) if isfile(join(path, f))]
            if isinstance(ext, str):
                img_files = [f for f in img_files if f.endswith(ext)]
            elif isinstance(ext, (list, tuple)):
                img_files = [f for f in img_files if any(f.endswith(e) for e in ext)]

            images: dict[str, pygame.Surface] = {}
            for f in img_files:
                images[f.split(".")[0].upper()] = pygame.image.load(join(path, f)).convert_alpha()

            if len(images.keys()) > 0:
                return images
            else:
                raise FileNotFoundError(f"No valid files found at location {path}.")
        else:
            raise NotADirectoryError(f"{path} is not a valid directory.")

    # @purpose
    # flip images on the X-axis to generate both left- and right-facing images
    # @scope:
    # private
    # @params:
    # images: a dictionary, the loaded images in a single direction
    # @returns:
    # a two-level dictionary of left (flipped on X-axis) and right (loaded) images, with the first level keys = the uppercase loaded file names
    #           and the second level keys = an ImageDirection directional value
    # @exceptions:
    # none
    @staticmethod
    def __generate_mirrors__(images: dict[str, pygame.Surface]) -> dict[str, dict[ImageDirection, pygame.Surface]] | None:
        mirrored_images: dict[str, dict[ImageDirection, pygame.Surface]] = {}
        for key, value in images.items():
            mirrored_images[key] = {ImageDirection.LEFT: pygame.transform.flip(value, True, False),
                                    ImageDirection.RIGHT: value}
        return mirrored_images

    # @purpose:
    # spawn a VisualEffect on a timer
    # @scope:
    # public
    # @params:
    # effect: a VisualEffect to spawn (requires all the parameters in the VisualEffect __init__ function)
    # time (sometimes optional): a float, the time in which the VisualEffect should be kept alive, optional if default_time was specified in __init__
    # @returns:
    # none
    # @exceptions:
    # ValueError, raised if neither time nor default time are specified and > 0.0
    def spawn(self, effect: VisualEffect, time: float | None=None) -> None:
        if time is None:
            if self.default_time is not None and self.default_time > 0.0:
                time = self.default_time
            else:
                raise ValueError("VisualEffects must have an alive time or default alive time specified and greater than 0.")
        self.active_effects[effect] = time

    # @purpose:
    # manage active VisualEffects
    # @scope:
    # public
    # @params:
    # dtime: a float, the amount of time that has passed in your game loop between instances of effects being drawn
    # @returns:
    # none
    # @exceptions:
    # none
    def manage(self, dtime: float):
        to_kill: list[VisualEffect] = []
        for key, value in self.active_effects.items():
            self.active_effects[key] -= dtime
            if self.active_effects[key] < 0.0:
                to_kill.append(key)
        for key in to_kill:
            del self.active_effects[key]

    # @purpose:
    # draw all active VisualEffects
    # @scope:
    # public
    # @params:
    # screen: the pygame surface on which to blit the images
    # screen_offset (optional): a tuple of 2 floats, the X (index 0) and Y (index 1) offsets at which the images should be drawn on the screen
    #           the practical purpose of this is to render to the screen based on display coordinates (e.g. top left corner of your
    #           monitor is X=0, Y=0) while tracking game objects at coordinates based on the level, map, or other world abstraction
    #           (e.g. top left corner of the level, map, or world is X=0, Y=0)
    # @returns:
    # none
    # @exceptions:
    # none
    def draw(self, screen: pygame.Surface, screen_offset: tuple[float, float] = (0.0, 0.0)) -> None:
        for effect in self.active_effects.keys():
            effect.draw(screen, screen_offset)

    # @purpose:
    # a simple loop to manage and draw all active VisualEffects
    # this may not fit your game engine's architecture, so you may want to call the manage and draw functions separately
    # @scope:
    # public
    # @params:
    # dtime: a float, the amount of time that has passed in your game loop between instances of effects being drawn
    # screen: the pygame surface on which to blit the images
    # screen_offset (optional): a tuple of 2 floats, the X (index 0) and Y (index 1) offsets at which the images should be drawn on the screen
    #           the practical purpose of this is to render to the screen based on display coordinates (e.g. top left corner of your
    #           monitor is X=0, Y=0) while tracking game objects at coordinates based on the level, map, or other world abstraction
    #           (e.g. top left corner of the level, map, or world is X=0, Y=0)
    # @returns:
    # none
    # @exceptions:
    # none
    def loop(self, dtime: float, screen: pygame.Surface, screen_offset: tuple[float, float] = (0.0, 0.0)) -> None:
        self.manage(dtime)
        self.draw(screen, screen_offset)

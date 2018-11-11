#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: seedjyh@gmail.com
# Create date: 2018/11/8


class Colour:
    def __init__(self, *args, **kwargs):
        """
        create object of Colour by:
            Colour(66051)
            or Colour("010203")
            or Colour(red=3, green=2, blue=1)
        :param kwargs: color=66051, color="010203", or red=3, green=2, blue = 1
        """
        self.red = 0
        self.green = 0
        self.blue = 0
        for value in args:
            if type(value) == int:
                self.red = value & 0xFF
                self.green = (value >> 8) & 0xFF
                self.blue = (value >> 16) & 0xFF
            elif type(value) == str:
                value_int = int(value, 16)
                self.red = value_int & 0xFF
                self.green = (value_int >> 8) & 0xFF
                self.blue = (value_int >> 16) & 0xFF
        for key, value in kwargs.items():
            if key == "colour":
                if type(value) == int:
                    self.red = value & 0xFF
                    self.green = (value >> 8) & 0xFF
                    self.blue = (value >> 16) & 0xFF
                elif type(value) == str:
                    value_int = int(value, 16)
                    self.red = value_int & 0xFF
                    self.green = (value_int >> 8) & 0xFF
                    self.blue = (value_int >> 16) & 0xFF
            else:
                setattr(self, key, value)

    def __str__(self):
        return "red=%d,green=%d,blue=%d" % (self.red, self.green, self.blue)

    def similar_to(self, colour, diff=0):
        if type(colour) == str:
            colour = Colour(colour)
        if abs(self.red - colour.red) > diff:
            return False
        if abs(self.green - colour.green) > diff:
            return False
        if abs(self.blue - colour.blue) > diff:
            return False
        return True


if __name__ == "__main__":
    pass

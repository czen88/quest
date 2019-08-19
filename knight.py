#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:07:39 2019

@author: igor
"""

# ASSUMPTIONS
# Python 3 is installed
# Board size is 8 x 8
# Invalid input will result in error message
# Lowercase input is converted to uppercase
# Enter exit to stop execution

from functools import reduce
import re
      
class Board:
    """
    A class used to represent Chess Board


    Attributes
    ----------
    size : int
        Size of the board. Currently fixed to 8
    xmap : str
        The list of letters used to represent x axis of the board
    visited : []
        Two dimensional boolean array representing visited cells of the board

    Methods
    -------
    is_inside(x, y)
        Returns True if coordinates are inside the board and False otherwise
    get_pos(x, y)
        Returns cell position based on coordinates. For example B2 is returned for x=2, y=2
    """
    def __init__(self):
        self.size = 8
        self.xmap = 'ABCDEFGH'
        # Make all cells unvisited  
        self.visited = [[False for i in range(self.size + 1)] for j in range(self.size + 1)] 

    # Checks whether cell is inside the board 
    def is_inside(self, x, y): 
        """Returns True if coordinates are inside the board and False otherwise.

        Parameters
        ----------
        x : int
            X coordinate of the board
        y : int
            Y coordinate of the board
        """
        return (x >= 1 and x <= self.size and y >= 1 and y <= self.size)    

    def get_pos(self, x, y):
        """Returns cell position based on coordinates. For example B2 is returned for x=2, y=2
        Returns empty string if cell is outside the board

        Parameters
        ----------
        x : int
            X coordinate of the board
        y : int
            Y coordinate of the board
        """
        if self.is_inside(x, y): return self.xmap[x-1]+str(y)
        return ''
    
    def set_visited(self, x, y):
        self.visited[x][y] = True
        
    def is_visited(self, x, y):
        return self.visited[x][y]
    
class Cell: 
    def __init__(self, board, x, y, path = None):
        self.board = board
        self.x = x 
        self.y = y
        if path is None: path = []
        self.path = path.copy()
        self.path.append((x,y))

    def get_pos(self):
        return self.board.get_pos(self.x, self.y)

    def get_path_str(self):
        return reduce(lambda a, b: a+' '+b, map(lambda x: self.board.get_pos(x[0], x[1]), self.path))

class Knight:
    def __init__(self, board):
        # All possible movements for the Knight: [dx,dy] 
        self.steps = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]
        self.board = board

    def get_steps(self, cell):
        res = []         
        for s in self.steps:
            c = Cell(self.board, cell.x + s[0], cell.y + s[1], cell.path)
            if(self.board.is_inside(c.x, c.y) and not self.board.is_visited(c.x, c.y)): 
                res.append(c)
        return res

class Navigator:
    def __init__(self, board, piece):
        self.board = board
        self.piece = piece
    
    def validate_input(self, arg):
        mask = '['+self.board.xmap+'][1-'+str(self.board.size)+']$'
        if re.findall(mask, arg.upper()) == []: 
            print("Incorrect argument: "+arg)
            return False
        return True
    
    # Method returns shortest path for Knight to reach target position
    def get_best_path(self, start, finish):
        if not self.validate_input(start) or not self.validate_input(finish): return ""
        start = start.upper()
        finish = finish.upper()
     
        # We do not need to move Knight
        if start == finish: return start
 
        # Init starting position of Knight with 0 distance 
        x = int(self.board.xmap.index(start[0])) + 1
        y = int(start[1])
        c = Cell(self.board, x, y)

        # Visit starting state
        self.board.set_visited(c.x, c.y)
        
        queue = []                
        queue.append(c)
                   
        # Loop until queue is not empty  
        while(len(queue) > 0):           
            t = queue.pop(0) 
              
            # Iterate for all reachable cells  
            for c in self.piece.get_steps(t):
                # if current cell is equal to target cell - we have found the path!  
                if(c.get_pos() == finish): return c.get_path_str()
                  
                self.board.set_visited(c.x, c.y)
                queue.append(c)
        # In case if no path found return empty string
        return ""
  
if __name__=='__main__':
    while True:
        instr = ''
        try:
            instr = input()
        except EOFError:
            break

        if instr == 'EXIT': break
        args = instr.split()        
        if len(args) != 2:
            print("Incorrect number of arguments provided: "+str(len(args)))
        else:
            b = Board()
            n = Navigator(b, Knight(b))
            print(n.get_best_path(args[0], args[1]))
            
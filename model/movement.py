from model.map import Region, Tile
from typing import List, Tuple, Dict
from queue import Queue

def bFS(moveDistance: int, grid: List[List[Tile]], start: Tuple[int, int], end: Tuple[int, int]):
    queue: Queue[Tuple[Tuple, int]] = Queue()
    queue.put(start)
    visited: Dict[Tuple[int, int], bool] = {}
    depth: int = 0
    prev: Dict[Tuple[int, int], Tuple[int, int]] = {}
    path: List[Tuple[int, int]] = []

    while not queue.empty():
        curPos, depth = queue.get()
        if curPos == end:
            return constructPath(prev, path, end)
        if depth > moveDistance:
            return []
        addNeighbors(grid, visited, curPos, queue, depth, prev)
    return []

def addNeighbors(grid: List[List[Tile]], visited: Dict[Tuple], pos: Tuple, q: Queue, depth: int, prev: Dict[Tuple, Tuple]):
    for (x,y) in [(x, y) for x in range(-1, 2) for y in range(-1, 2)]:
        x_new = x + pos[0]
        y_new = y + pos[1]

        # Out of Bounds check 
        if (x_new < 0 or y_new < 0) or (x_new > grid.len() or y_new > grid.len()):
            continue

        # isPassable() check
        if not grid[x_new][y_new].isPassable():
            continue

        # Visited check & add neighbor to queue
        if not (x_new, y_new) in visited:
            visited[(x_new, y_new)] = True
            q.put((x_new, y_new), depth + 1)
            prev[(x_new, y_new)] = pos
    return

def constructPath(prev: Dict[Tuple, Tuple], path: List[Tuple], end: Tuple):
    cur: Tuple = end

    while cur in prev:
        path.insert(cur, 0)
        cur = prev[cur]

    return
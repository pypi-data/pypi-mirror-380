import numpy as np
import numba
import heapq

import calsipro.util
import calsipro.separate



def calculate_mask_reach(data):
    assert len(data.shape) == 2
    data = data.copy()
    reach = reachability(data)
    th = calsipro.separate.calculate_threshold(reach)
    mask = calsipro.util.calculate_mask(reach, th=th, raw=True)
    return mask


def reachability(data):
    data = calsipro.util.normalize(data)
    reach = np.ones(shape=data.shape, dtype=data.dtype)
    visited = np.zeros(shape=data.shape, dtype=np.bool_)
    level = np.zeros(shape=data.shape, dtype=data.dtype)
    _reachability(data, reach, visited, level)
    return reach


@numba.njit(cache=True)
def _reach_init_point(x, y, next, reach, visited, data, level):
    heapq.heappush(next, (0.0, x, y))
    reach[x, y] = 0.0
    level[x, y] = data[x, y]


@numba.njit(cache=True)
def _reach_init(xdim, ydim, next, reach, visited, data, level):

    for y in range(10):
        _reach_init_point(0, y, next, reach, visited, data, level)
        _reach_init_point(0, ydim-y-1, next, reach, visited, data, level)
        _reach_init_point(xdim-1, y, next, reach, visited, data, level)
        _reach_init_point(xdim-1, ydim-y-1, next, reach, visited, data, level)

    for x in range(10):
        _reach_init_point(x, 0, next, reach, visited, data, level)
        _reach_init_point(xdim-x-1, 0, next, reach, visited, data, level)
        _reach_init_point(x, ydim-1, next, reach, visited, data, level)
        _reach_init_point(xdim-x-1, ydim-1, next, reach, visited, data, level)


@numba.njit(cache=True)
def _reach_check(ox, oy, x, y, xdim, ydim, next, reach, data, visited, level):
    W1 = 100
    W2 = 1
    WT = W1+W2
    if 0 <= x < xdim and 0 <= y < ydim:
        r = abs(data[x,y] - level[ox, oy])
        r = max(r, reach[ox, oy])
        reach[x, y] = min(reach[x, y], r)
        level[x, y] = (W1*level[ox, oy] + W2*data[x, y]) / WT
        heapq.heappush(next, (r, x, y))


@numba.njit(cache=True)
def _reach_visit(ox, oy, xdim, ydim, next, reach, data, visited, level):
    if visited[ox, oy]:
        return
    visited[ox, oy] = True

    _reach_check(ox, oy, ox+1, oy, xdim, ydim, next, reach, data, visited, level)
    _reach_check(ox, oy, ox-1, oy, xdim, ydim, next, reach, data, visited, level)
    _reach_check(ox, oy, ox, oy+1, xdim, ydim, next, reach, data, visited, level)
    _reach_check(ox, oy, ox, oy-1, xdim, ydim, next, reach, data, visited, level)


@numba.njit(cache=True)
def _reachability(data, reach, visited, level):
    next = [(np.float64(0.0), 1, 1) for x in range(0)]
    xdim, ydim = data.shape
    _reach_init(xdim, ydim, next, reach, visited, data, level)

    while (len(next) != 0):
        r, x, y = heapq.heappop(next)
        _reach_visit(x, y, xdim, ydim, next, reach, data, visited, level)

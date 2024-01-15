#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random as rnd
import matplotlib.pyplot as plt


def plot_segments(point, s):
    plt.xlabel('Координаты')
    plt.title("Графическое представление")
    for i in s:
        d = [0, 0]
        plt.plot(i, d, color="blue", linewidth=40, solid_capstyle='butt')
    plt.plot(point, [0 for _ in range(len(point))], linestyle='None',
             marker='|', markersize=60, color="red")
    ax = plt.gca()
    ax.set_yticks([])
    plt.show()

def pointscover1(s):
    segment = []
    while (len(s) > 0):
        xm = min(s)
        segment.append([xm, xm+1])
        i = 0
        while i < len(s):
            if segment[-1][0] <= s[i] <= segment[-1][1]:
                s.pop(i)
            else:
                i += 1
    return segment

def pointscover2(s):
    segment = []
    s.sort()
    i = 0
    while i < len(s):
        xm = s[i]
        segment.append([xm, xm+1])
        i += 1
        while i < len(s) and s[i] <= xm+1:
            i += 1
    return segment

if __name__ == '__main__':
    s = [rnd.randint(0, 100)/10 for i in range(20)]
    s2 = s.copy()
    print("Множество точек:", s)
    seg = pointscover1(s)
    print("Множество отрезков 1:", seg)
    s = s2
    seg = pointscover2(s)
    print("Множество отрезков 2:", seg)
    print("Минимальное количество отрезков, \
    которыми можно покрыть данное множество точек = ", len(seg))
    plot_segments(s2, seg)
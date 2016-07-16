__author__ = 'zhangxa'

from numpy import *

def file2matrix(filename):
    file = open(filename)
    lines = file.readlines()
    numLines = len(lines)
    matrix = zeros((numLines,1))
    targetVector = []
    row = 0
    for line in lines:
        dataSplit = line.strip().split('\t')
        matrix[row,:] = dataSplit[0:3]
        targetVector.append(int(dataSplit[-1]))
        row+=1
    return matrix,targetVector




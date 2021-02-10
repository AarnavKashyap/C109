import pandas as pd
import statistics
import csv

df = pd.read_csv("height-weight.csv")
heightlist = df["Height(Inches)"].to_list()
weightlist = df["Weight(Pounds)"].to_list()

heightmean = statistics.mean(heightlist)
heightmedian = statistics.median(heightlist)
heightmode = statistics.mode(heightlist)
heightstdev = statistics.stdev(heightlist)

print(heightmean)
print(heightmedian)
print(heightmode)
print(heightstdev)

firststart = heightmean - heightstdev
firstend = heightmean + heightstdev

secondstart = heightmean - 2*heightstdev
secondend = heightmean + 2*heightstdev

thirdstart = heightmean - 3*heightstdev
thirdend = heightmean + 3*heightstdev

first = [result for result in heightlist if result > firststart and result < firstend]
second = [result for result in heightlist if result > secondstart and result < secondend]
third = [result for result in heightlist if result > thirdstart and result < thirdend]

firstpercentage = len(first)* 100 / len(heightlist)
secondpercentage = len(second)* 100 / len(heightlist)
thirdpercentage = len(third)* 100 / len(heightlist)

print(firstpercentage)
print(secondpercentage)
print(thirdpercentage)




#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for i in range(0, len(dir(hidden_4))):
        if dir(hidden_4)[i][0] != '_':
            print("{}".format(dir(hidden_4)[i]))

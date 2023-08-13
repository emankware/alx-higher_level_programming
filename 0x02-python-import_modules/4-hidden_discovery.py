#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    name = dir
    for i in range(0, len(name)):
        if name[i][0:2] != "__":
            print("{}".format(name[i]))

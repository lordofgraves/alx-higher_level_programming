#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for a in names:
        if a[:2] != "__":
            print(a)

def friend(x):
    myfriend = []
    for name in x:
        if len(name) == 4:
            myfriend.append(name)
    return myfriend
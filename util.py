import math
def lerp(t, b, c, d):
    # t /= durasi/2
    # if(t<1):
    #     return (c/2)*t*t+b
    # else:
    #     t -= 1
    #     return -(c/2) * (t*(t-2) - 1) + b
    t /= d/2
    if (t < 1):
        return c/2*t*t*t*t + b
    t -= 2
    return -c/2 * (t*t*t*t - 2) + b
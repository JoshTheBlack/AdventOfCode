from comm import timed

@timed
def day17A(data):
    return sum(range(abs(data[2])))

@timed
def day17B(data):
    def search(xmin, xmax, ymin, ymax, v0xmin):
        total = 0

        for v0x in range(v0xmin, xmax + 1):
            for v0y in range(ymin, -ymin):
                x, y   = 0, 0
                vx, vy = v0x, v0y

                while x <= xmax and y >= ymin:
                    if x >= xmin and y <= ymax:
                        total += 1
                        break

                    x, y = (x + vx, y + vy)
                    vy -= 1

                    if vx > 0:
                        vx -= 1
        return total
    
    xmin, xmax, ymin, ymax = data
    v0xmin = int((xmin*2)**0.5)
    total = 0

    for v0x in range(v0xmin, xmax + 1):
        for v0y in range(ymin, -ymin):
            x,y = 0,0
            vx,vy = v0x,v0y
            while x <= xmax and y >= ymin:
                if x >= xmin and y <= ymax:
                    total += 1
                    break
                x,y = (x+vx, y+vy)
                vy -= 1
                vx = max(0,vx-1)

    # total = search(xmin, xmax, ymin, ymax, v0xmin)

    return total











if __name__ == "__main__":
    data = [253,280,-73,-46]
    print(f"Day 17 A: {day17A(data)}") # 
    print(f"Day 17 B: {day17B(data)}") # 
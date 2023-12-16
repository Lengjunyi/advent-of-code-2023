lines = open("quest16.in").read().split("\n")

M = len(lines)
N = len(lines[0])


total_met = set()

maxi = 0
for ii in range(len(lines)):
    for jj in range(len(lines[0])):
        if ii!=0 and jj!=0 and ii!=M-1 and jj != N-1:
            continue
# for ii in [0]:
#     for jj in [0]:
        for (dxx, dyy) in [(1,0),(0,1),(-1,0),(0,-1)]:
            if (ii,jj,dxx,dyy) in total_met:
                continue
            met = set()
            queue = [(ii,jj,dxx,dyy)]
            while queue:
                now = queue[0]
                queue = queue[1:]
                if now in met:
                    continue
                x,y,dx,dy = now
                if x<0 or y<0 or x>=M or y >= N:
                    continue
                met.add(now)
                # print(123)
                c = lines[x][y]
                # print(lines[x])
                if c == ".":
                    queue.append((x+dx,y+dy,dx,dy))
                elif c == "\\":
                    queue.append((x+dy,y+dx,dy,dx))
                elif c == "/":
                    queue.append((x-dy,y-dx,-dy,-dx))
                elif (c == "|" and dy == 0) or (c == "-" and dx == 0):
                    queue.append((x+dx,y+dy,dx,dy))
                else:
                    if dx == 0:
                        queue.append((x+1, y, 1, 0))
                        queue.append((x-1, y, -1, 0))
                    if dy == 0:
                        queue.append((x, y+1, 0, 1))
                        queue.append((x, y-1, 0, -1))
                # print(now)

            points = set()
            for (x,y,dx,dy) in met:
                points.add((x,y))
            # print(len(points))

            ans = 0
            # for i in range(len(lines)):
            #     for j in range(len(lines[0])):
            #         if (i,j) in points:
            #             print("#", end="")
            #             ans += 1
            #         else:
            #             print(".", end="")
            #     print()
            total_met.update(met)
            print(len(points),ii,jj,dxx,dyy)
            ans = len(points)
            maxi = max(ans, maxi)

print(maxi)

# i was expecting a much higher computing complexity...
# but it turns out it's just bash bash bash
# so no need for optimization

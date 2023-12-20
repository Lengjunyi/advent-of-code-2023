s = open("quest20.in").read()


wires = {}
vs = []
for l in s.split("\n"):
    left,right = l.split(" -> ")
    right = list(right.split(", "))
    if left == "broadcaster":
        vs = [(left, v, False) for v in right]
    else:
        wires[left[1:]] = {"to" : [], "from" : [], "cache": {}}
        if left[0] == "%":
            wires[left[1:]]["cache"][left[1:]] = False
        for r in right:
            if r not in wires:
                wires[r] = {"to" : [], "from" : [], "cache": {}}

for l in s.split("\n"):
    left,right = l.split(" -> ")
    right = list(right.split(", "))

    if left == "broadcaster":
        continue

    wires[left[1:]]["type"] = left[0]
    for r in right:
        wires[left[1:]]["to"].append(r)
        # wires[r]["from"].append(left[1:])
        wires[r]["cache"][left[1:]] = False

    # wires.append((left[0], left[1:], False, right))

vs1 = vs
print(wires)


anss = {}

keys = wires.keys()
c1, c2 = 0,0
for ii in range(10000):
    c2 += 1
    vs = [v for v in vs1]
    while vs:
        fro, to, v = vs[0]
        # print(fro, v, to)
        if v:
            c1 += 1
        else:
            if to in {"st", "tn", "hh", "dt"} and to not in anss:
                anss[to] = ii+1
        # print(c1, c2)
        vs = vs[1:]
        if "type" not in wires[to]:
            continue
        if wires[to]["type"] == "&":
            wires[to]["cache"][fro] = v
            # print(wires[to]["cache"])
            vnext = True
            for vv in wires[to]["cache"].values():
                vnext = vnext and vv
            #     print(to, vnext, vv, "here")
            # print(vnext)
            for next in wires[to]["to"]:
                vs.append((to, next, not vnext))
        else:
            if not v:
                # print("taken", v, fro, to)
                wires[to]["cache"][to] = not wires[to]["cache"][to]
                for next in wires[to]["to"]:
                    vs.append((to, next, wires[to]["cache"][to]))
    all = {}
    for k in wires:
        for j in wires[k]["cache"]:
            all[j] = wires[k]["cache"][j]
            # print(wires[k]["cache"])
    # print(ii, "th run",c1, c2,)
print(c1 * c2)
        # for obs in wires[n][""]

print(anss)

import math
print(math.lcm(*anss.values()))

# c1, c2 = 0,0
# for ii in range(2):
#     c2 += 1
#     vs = [vvv for vvv in vs1]
#     while vs:
#         n, v = vs[0]
#         print(n,v)
#         vs = vs[1:]
#         if v:
#             c1+=1
#         else:
#             c2+=1
#         # print(c1,c2)
#         for i, (a,b,c,d) in enumerate(wires):
#             if b == n:
#                 if a == "&":
#                     c = v
#                     for nn in d:
#                         vs.append((nn, not c))
#                 if a == "%":
#                     if not v:
#                         c = not c
#                         for nn in d:
#                             vs.append((nn, c))
#                 wires[i] = (a,b,c,d)


# def nneeded(node):
#     if 

caches = {}

def find(node):
    if node in caches:
        return caches[node]
    if node == "broadcast":
        return 1
    print(wires[node]["cache"])
    if "type" in wires[node] and wires[node]["type"] == "&" and len(wires[node]["cache"]) == 1:
        for next in wires[node]["cache"]:
            return 2 * find(next)
    else:
        ans = 1000000000000
        for r in wires[node]["cache"]:
            ans = min(ans, find(r))
        return ans
        
# print(find("rx"))

print(c1, c2)

# not very happy today.
# cheated by looking into the solution on reddit.
# spent tons of time looking for a universal solution
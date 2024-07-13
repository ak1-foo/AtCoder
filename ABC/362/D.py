# Time UP!!

top_num, line_num = map(int, input().split())
top_weight = list(map(int, input().split()))

line_weight = [list(map(int, input().split())) for _ in range(line_num)]

print(line_weight)
go_weight = [{'from': line_weight[line][0], 'to': line_weight[line][1], 'weight': line_weight[line][2]+top_weight[line_weight[line][1]-1]} for line in range(line_num)]

def find_min_costs():
    costs = [float('inf')] * top_num
    costs[0] = top_weight[0]
    for i in range(top_num):
        for j in range(line_num):
            weight = go_weight[j]
            if (costs[weight['to']] > costs[weight['from']] + weight['weight']):
                costs[weight['to']] = costs[weight['from']] + weight['weight']
                if (i == top_num -1):
                    return costs

def get_route(start_idx, goal_idx):
    visited_top = []
    route_list = [[]]

def calc_weight(route_list):
    best_weight = float('inf')
    for route in route_list:
        weight = 0
        for i, line in enumerate(route):
            if (i==0):
                weight += top_weight[line[0]] # 左の頂点の重みを足す
            weight += top_weight[line[1]] + line[2] # 右の頂点の重みと辺の重みを足す
        if (best_weight == -1 or best_weight > weight):
            best_weight = weight

print(find_min_costs())

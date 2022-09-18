import collections

def mergeInStockDays(stockInfos):
    stockMap = collections.defaultdict(list)
    # N -> len(stockInfos)
    # O(N)
    for stock in stockInfos:
        element = stock[0]
        day = stock[1]
        inStock = stock[2]
        stockMap[element].append((day, inStock))

    # k -> elements
    # v -> len(value)
    # V -> total len(value) -> N

    # O(k vlogv)
    for value in stockMap.values():
        value.sort()
    
    mergedStockInfos = collections.defaultdict(list)

    # O(kv) -> O(n)
    # k
    for element, stockInfos in stockMap.items():
        #  v
        for i in range(len(stockInfos)):
            day = stockInfos[i][0]
            inStock = stockInfos[i][1]
            if i == 0 or mergedStockInfos[element][-1][2] != inStock:
                mergedStockInfos[element].append([day, day, inStock])
            else:
                mergedStockInfos[element][-1][1] = day
    
    print(mergedStockInfos)

mergeInStockDays([['A1', 1, 0], ['A2', 1, 1], ['A1', 3, 1], ['A2', 2, 0], ['A2', 3, 1], ['A1', 2, 1], ['A1', 4, 1], ['A1', 5, 1]])
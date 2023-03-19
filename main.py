# python3
import heapq


def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs

    threads = [(i, 0) for i in range(n)]

    heap = [(0, i) for i in range(n)]
    heapq.heapify(heap)

    for i in range(m):

        fin, index = heapq.heappop(heap)
        output.append((index, fin))
        fin+= data[i]


        threads[index] = (index, fin)
        heapq.heappush(heap, (fin, index))

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    n,m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    for i in result:
        print(i[0], i[1])
    
    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()

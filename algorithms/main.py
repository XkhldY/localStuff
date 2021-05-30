from typing import List


def turnstile(time, direction):
    en, ex = [], []
    res = [0] * len(time)
    for i, t in enumerate(time):
        if direction[i] == 1:
            ex.append([time[i], i])
        else:
            en.append([time[i], i])

    timeCounter, lastTurn = 0, -1  # time is 0 at the beginning and -1
    # indicates nothing happened at prior time
    while ex or en:
        # Process the exit queue if and only if following conditions are satisfied
        # If exit queue is not empty and the person at the front of the queue can go out based on his time stamp
        # and ( Nothing happened at last time stamp i.e. nobody moved in or out so lastTurn will be -1 in this case
        # or, somebody moved out at last time stamp, in this case lastTurn will be 1
        # or, nobody is there in the entrance queue
        # or, at last time stamp somebody got in but the person at the front of the queue can't go in due to their timestamp
        if ex and ex[0][0] <= timeCounter and \
                (lastTurn == -1 or lastTurn == 1 or not en or (lastTurn == 0 and en[0][0] > timeCounter)):
            res[ex[0][1]] = timeCounter
            lastTurn = 1
            ex.pop(0)
        elif en and en[0][0] <= timeCounter:
            res[en[0][1]] = timeCounter
            lastTurn = 0
            en.pop(0)
        else:
            lastTurn = -1

        timeCounter += 1

    return res


def get_times(num_customers: int, arr_time: List[int], direction: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    if num_customers == 1:
        return arr_time
    ret = []
    l = 0
    r = 1
    last = 1
    while r < len(arr_time) and l < len(arr_time):
        if arr_time[l] < arr_time[r]:
            ret.append(arr_time[l])
            l = r
            r += 1
            last = direction[l]

        elif arr_time[l] == arr_time[r]:
            if direction[l] == direction[r] or (direction[l] == 1 and (not last or last == 1)) or (
                direction[l] == 0 and last == 0
            ):
                ret.append(arr_time[l])
                arr_time[r] += 1
                l = r
                r += 1
                last = direction[l]

            elif direction[r] == 1 and (not last or last == 1) or (direction[r] == 0 and last == 0):
                ret.append(arr_time[r])
                arr_time[l] += 1
                r += 1
                last = direction[r]
    return ret





    return ret


if __name__ == "__main__":
    testcases = [
        [[0, 0, 1, 5], [0, 1, 1, 0], [2, 0, 1, 5]], \
        [[1, 2, 4], [0, 1, 1], [1, 2, 4]], \
        [[1, 1], [1, 1], [1, 2]], \
        [[1, 1, 3, 3, 4, 5, 6, 7, 7], [1, 1, 0, 0, 0, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    ]

    passedCounter = 0
    for i, test in enumerate(testcases):
        # time, direction, expected = test[0], test[1], test[2]
        # result = turnstile(time, direction)

        # if result == expected:
        #     passedCounter += 1
        # else:
        #     print(" %d Test case failed " % (i + 1))
        #     print("Expected: ", expected)
        #     print("Got: ", result)

        time, direction, expected = test[0], test[1], test[2]
        result = get_times(len(time), time, direction)
        if result == expected:
            passedCounter += 1
        else:
            print(" %d Test case failed " % (i + 1))
            print("Expected: ", expected)
            print("Got: ", result)

    print("%d/%d Test Cased Passed" % (passedCounter, len(testcases)))

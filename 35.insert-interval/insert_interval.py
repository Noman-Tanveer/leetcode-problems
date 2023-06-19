class Solution:
    def insert(self, intervals, newInterval):

        START, END = 0, 1
        s, e = newInterval[START], newInterval[END]
        left, right = [], []
        for cur_interval in intervals:
            if cur_interval[END] < s:
                left += [ cur_interval ]

            elif cur_interval[START] > e:
                right += [ cur_interval ]

            else:
                s = min(s, cur_interval[START])
                e = max(e, cur_interval[END])

        return left + [ [s, e] ] + right

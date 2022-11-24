import csv
import statistics

def estimate(params, x):
    (t0,t1) = params
    return (t0 + t1 * x)

def get_new_params(params, data):
    (t0, t1) = params
    (x, y) = data
    tmp0 = 0
    tmp1 = 0
    for i in range(len(x)) :
        tmp0 += estimate(params, x[i]) - y[i]
        tmp1 += (estimate(params, x[i]) - y[i]) * x[i]
    tmp0 *= 1 / len(x)
    tmp1 *= 1 / len(x)
    return (tmp0, tmp1)

def get_params(data):
    t0 = 0
    t1 = 0
    t0_n = 1
    t1_n = 1
    while (abs(t0_n) > 0.001 or abs(t1_n) > 0.001):
        (t0_n, t1_n) = get_new_params((t0, t1), data)
        t0 -= 0.0001 * t0_n
        t1 -= 0.0001 * t1_n
    return ((t0,t1))
def normalize(d):
    mean = statistics.mean(d)
    sd = statistics.stdev(d)
    d_res = []
    for i in d :
        d_res.append((i - mean) / sd)
    return (d_res, mean, sd)
if __name__ == "__main__":
    x = []
    y = []
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            x.append(int(row['km']))
            y.append(int(row['price']))
    (x_n, x_mean, x_sd) = normalize(x) 
    (y_n, y_mean, y_sd) = normalize(y) 
    (t0, t1) = get_params((x_n, y_n))
    print(estimate((t0, t1) , (84000- statistics.mean(x)) / statistics.stdev(x)) * statistics.stdev(y) + statistics.mean(y))


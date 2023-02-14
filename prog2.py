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
def load_data():
    x = []
    y = []
    with open('data.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            x.append(int(row['km']))
            y.append(int(row['price']))
    return (x, y)
def prog2():
    (x, y) = load_data()
    (x_n, x_mean, x_sd) = normalize(x) 
    (y_n, y_mean, y_sd) = normalize(y) 
    (t0, t1) = get_params((x_n, y_n))
    #(t0 + t1 * ((x - m(x)) / stdev(x))) * stdev(y) + m(y) 
    #(t0 + t1 * (x / stdev(x) - m(x) / stdev(x))) * stdev(y) + m(y)
    #(t0 + (x * t1)/stdev(x) - (t1 * m(x)) /stdev(x)) * stdev(y) + m(y)
    # t0*stdev(y) + m(y) - t1 * m(x) * stdev(y) / stdev(x) + x * t1 * stdev(y) / stdev(x)
    (t0_2, t1_2) = (t0 * statistics.stdev(y) + statistics.mean(y) - t1 * statistics.mean(x) * statistics.stdev(y) /  statistics.stdev(x), \
t1 * statistics.stdev(y) / statistics.stdev(x))
    return (t0_2, t1_2)
    print(t0_2, t1_2)
    print(estimate((t0, t1) , (84000- statistics.mean(x)) / statistics.stdev(x)) * statistics.stdev(y) + statistics.mean(y))
    print(t0_2 + t1_2 * 84000)
if __name__ == "__main__":
    (t0, t1) = prog2()
    f = open("params.txt", "w")
    f.write(str(t0) + "\n")
    f.write(str(t1))
    f.close()    
    print ("Params saves")

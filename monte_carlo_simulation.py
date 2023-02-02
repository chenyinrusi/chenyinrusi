import random
import pandas
import statistics

def lm_simulation(ppl_no=100, simu_no=100, cutoff_no=37):
    initial_base = []

    for i in range(0, ppl_no):
        initial_base.append(i)
    simu_base = []
    simu_base_string = []

    for j in range(0, simu_no):
        bench_base = initial_base.copy()
        result_base = []
        for i in range(0, ppl_no):
            ind = random.randint(0, len(bench_base) - 1)
            result_base.append(bench_base[ind])
            bench_base.remove(bench_base[ind])
        simu_base.append((result_base))
        simu_base_string.append(str(result_base))

    next_pick_no = []
    next_pick_result = []
    succ_pick = []
    succ_result = []

    for i in simu_base:
        sample_max = max(i[:cutoff_no])
        exist_flag = 0
        for j in range(cutoff_no, ppl_no):
            if i[j] > sample_max:
                next_pick_no.append(j + 1)
                succ_pick.append(j + 1)
                next_pick_result.append(i[j])
                succ_result.append(i[j])
                exist_flag = 1
                break
            else:
                pass
        if exist_flag == 0:
            next_pick_no.append('')
            next_pick_result.append('')
        else:
            pass 
            

    stats_no_one = (simu_no - len(succ_pick)) / simu_no
    stats_avg_result = statistics.mean(succ_result)
    stats_avg_pick = statistics.mean(succ_pick)
    stats_stdev_result = statistics.stdev(succ_result)
    stats_stdev_pick = statistics.stdev(succ_pick)

    consolidated_data = pandas.DataFrame(simu_base_string, columns=['Sample Data'])
    consolidated_data['NEXT_PICK'] = next_pick_no
    consolidated_data['NEXT_RESULT'] = next_pick_result

    return consolidated_data, stats_no_one, stats_avg_pick, stats_stdev_pick, stats_avg_result, stats_stdev_result

for i in [10,37,60]:
    simu_data = lm_simulation(ppl_no= 100, simu_no= 1000000, cutoff_no= i)
    print(i)
    print(simu_data[1])
    print(simu_data[2])
    print(simu_data[4])

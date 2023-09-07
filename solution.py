def minimum_flips(initial_str, target_str):
    flips = 0
    for i in range(len(target_str)):
        if initial_str[i] != target_str[i]:
            flips += 1
            for j in range(i, len(initial_str)):
                if initial_str[j] == '0':
                    initial_str = initial_str[:j] + '1' + initial_str[j+1:]
                else:
                    initial_str = initial_str[:j] + '0' + initial_str[j+1:]
    return flips

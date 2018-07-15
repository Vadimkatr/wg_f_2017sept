import time
start_time = time.time()

for test_name in ['test_A', 'test_B', 'test_C', 'test_D']:
    with open(f'Wargaming Forge Task/task_1_data/{test_name}/players.txt', 'r') as players_file, \
        open(f'Wargaming Forge Task/task_1_data/{test_name}/teams.txt', 'r') as teams_file, \
        open(f'Vadim_Lisay_task_1_team_pairs/{test_name}_pairs.txt', 'w') as pairs_file:
        players = []
        teams = dict()
        #
        for line in players_file.readlines():
            players.append(int(line.split(' ')[1]))
        for line in teams_file.readlines():
            tm = [int(i) for i in line.split(' ')]
            teams[tm[0]] = sum([players[i] for i in tm[1:]])
        sorted_teams = sorted(teams.items(), key=lambda key:key[1])
        # or:
        # from operator import itemgetter
        # sorted_teams = sorted(teams.items(), key=itemgetter(1))
        #
        for i in range(len(sorted_teams)):
            pairs_file.write(str(sorted_teams[i][0]))
            if i % 2 != 0:
                pairs_file.write('\n')
            else:
                pairs_file.write(' ')    

print("--- %s seconds ---" % (time.time() - start_time))

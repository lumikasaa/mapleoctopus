

success_r = {
    1: [ 1,     0,     0    ],
    2: [ 0.7,   0.3,   0    ],
    3: [ 0.55,  0.45,  0    ],
    4: [ 0.4,   0.6,   0    ],
    5: [ 0.307, 0.693, 0    ],
    6: [ 0.205, 0.765, 0.03 ],
    7: [ 0.153, 0.817, 0.03 ],
    8: [ 0.1,   0.87,  0.03 ]
}

rewards = {
    1: 0,
    2: 1,
    3: 3,
    4: 6,
    5: 10,
    6: 20,
    7: 50,
    8: 150,
    9: 300
}

r_t = {
    100: rewards
}

# Just some random enum type of thing for readability idk, that's probably a lost
# cause at this point but who even cares.
SUCCESS = 0
FAILURE = 1
RESET = 2

results = []

def recursive_weighted(round):

    if round == 1:
        return

    round_w_rewards = {}
    row = '{: <4}'.format(f'r{round}') + ': '

    for c_lvl in range(2,9):

        c = 0 if c_lvl == 2 else 1

        w_reward = r_t[round][c_lvl+1] * success_r[c_lvl][SUCCESS] \
                 + r_t[round][c_lvl-c] * success_r[c_lvl][FAILURE] \
                 + r_t[round][2]       * success_r[c_lvl][RESET]
        
        if w_reward > rewards[c_lvl]:
            round_w_rewards[c_lvl] = w_reward
            row = row + "\U0001f7e9"

        else:
            round_w_rewards[c_lvl] = rewards[c_lvl]
            row = row + "\U0001f7e5"

    results.insert(0,row)

    round_w_rewards[1] = rewards[1]
    round_w_rewards[9] = rewards[9]
    r_t[round-1] = round_w_rewards

    recursive_weighted(round-1)
        

recursive_weighted(100)

print("      2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣")

for i in range(len(results)):
    print(results[i])
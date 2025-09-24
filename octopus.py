

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

# Just some random enum type of thing for readability idk, that's probably a lost
# cause at this point but who even cares.
SUCCESS = 0
FAILURE = 1
RESET = 2

rewards = {
    0: {
        1: 0,
        2: 1,
        3: 3,
        4: 6,
        5: 10,
        6: 20,
        7: 50,
        8: 150,
        9: 300
    },
    1: {
        1: 0,
        2: 40,
        3: 120,
        4: 240,
        5: 400,
        6: 600,
        7: 1000,
        8: 4000,
        9: 8000
    },
    2: {
        1: 0,
        2: 20,
        3: 60,
        4: 120,
        5: 200,
        6: 300,
        7: 600,
        8: 2000,
        9: 6000
    }
}

# MORE "ENUMS" YAY
# FRAGS = 0
# ERDA = 1
# VOUCHERS = 2


def recursive_weighted(round, r_t, results, mode=0):

    if round == 1:
        return

    round_w_rewards = {}
    row = '{: <4}'.format(f'r{round}') + ': '

    for c_lvl in range(2,9):

        c = 0 if c_lvl == 2 else 1

        w_reward = r_t[round][c_lvl+1] * success_r[c_lvl][SUCCESS] \
                 + r_t[round][c_lvl-c] * success_r[c_lvl][FAILURE] \
                 + r_t[round][2]       * success_r[c_lvl][RESET]
        
        if w_reward > rewards[mode][c_lvl]:
            round_w_rewards[c_lvl] = w_reward
            row = row + "\U0001f7e9"

        else:
            round_w_rewards[c_lvl] = rewards[mode][c_lvl]
            row = row + "\U0001f7e5"

    results.insert(0,row)

    round_w_rewards[1] = rewards[mode][1]
    round_w_rewards[9] = rewards[mode][9]
    r_t[round-1] = round_w_rewards

    recursive_weighted(round-1, r_t, results, mode)
        


def main():

    results = []

    mode_input = int(input("Select mode: [1] Sol Erda Fragments [2] Sol Erda [3] EXP Vouchers:\n"))

    r_t = {
        100: rewards[mode_input-1]
    }

    print(r_t)
    recursive_weighted(100, r_t, results, mode_input-1)

    print("      2️⃣ 3️⃣ 4️⃣ 5️⃣ 6️⃣ 7️⃣ 8️⃣")

    for i in range(len(results)):
        print(results[i])


if __name__ == "__main__":
    main()
from fire import Fire
from tqdm import tqdm
from prisoner_riddle.simulation import simulate
from prisoner_riddle.strategy import open_boxes_random, open_boxes_strategically


def loop(run_count:int = 1, prisoners_count:int = 100, strategize: bool = False):
    free_count = 0
    executed_count = 0
    strategy = open_boxes_strategically if strategize else open_boxes_random

    for i in tqdm(range(1, run_count + 1)):
        free = simulate(prisoners_count, strategy)

        if free: free_count += 1
        else: executed_count += 1

        # print(f'loop #{i} -- results : {"free!" if free else "executed!"}')
    
    print(f'\nfinal results: {(free_count / run_count)}% time freed')
        


if __name__ == '__main__':
    Fire({'run': loop})
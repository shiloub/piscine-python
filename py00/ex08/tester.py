from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(5000)):
    sleep(0.003)
print()
for elem in tqdm(range(5000)):
    sleep(0.003)
print()
def tower_of_hanoi(n , from_rod, to_rod, using_rod):
    if n == 0:
        return
    tower_of_hanoi(n-1, from_rod, using_rod, to_rod)
    print("Move disk ",n," from ",from_rod,"to ",to_rod)
    tower_of_hanoi(n-1, using_rod, to_rod, from_rod)
         
n = 3
from_rod, using_rod, to_rod = 'A', 'B', 'C'

tower_of_hanoi(n, from_rod, to_rod, using_rod)
def display_toh_moves(self, s, d, disk):
    print('Move disk', disk, 'from', s, 'to', d)

def move_disks(self, source, dest, s, d):
    first_popped_element, source = source.pop(source)
    second_popped_element, dest = dest.pop(dest)
    if first_popped_element == -1:
        source = source.push(source, second_popped_element)
        source.display_toh_moves(d, s, second_popped_element)
    elif second_popped_element == -1:
        dest = dest.push(dest, first_popped_element)
        dest.display_toh_moves(s, d, first_popped_element)
    elif first_popped_element > second_popped_element:
        source = source.push(source, first_popped_element)
        source = source.push(source, second_popped_element)
        source.display_toh_moves(d, s, second_popped_element)
    else:
        dest = dest.push(dest, second_popped_element)
        dest = dest.push(dest, first_popped_element)
        dest.display_toh_moves(s, d, first_popped_element)
    
    return source, dest

def tower_of_hanoi(self, no_of_disks, source, aux, dest):
    print('\n\n')
    s = 'S'
    a = 'A'
    d = 'D'
    if no_of_disks % 2 == 0:
        a, d = d, a
    no_of_moves = pow(2, no_of_disks) - 1
    for i in range(no_of_disks, 0, -1):
        source = source.push(source, i)
        
    for i in range(no_of_moves):
        if i % 3 == 0:
            source, dest = source.move_disks(source, dest, s, d)
        elif i % 3 == 1:
            source, aux = source.move_disks(source, aux, s, a)
        elif i % 3 == 2:
            aux, dest = source.move_disks(aux, dest, a, d)
    print('\n\n')


























def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)


















- Power Function
- Factorial Function

Iteration + Recursion



int x, int y -> x^y

x = 2, y = 3; Output = 8



n = 4

factorial(4) -> 4 * 3 * 2 * 1
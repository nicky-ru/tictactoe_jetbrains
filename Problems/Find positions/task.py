sequence = input().split()
number = input()
positions = [indx for indx in range(len(sequence)) if sequence[indx] == number]
if not positions:
    print('not found')
else:
    positions.sort()
    positions = [str(positions[indx]) for indx in range(len(positions))]
    print(" ".join(positions))

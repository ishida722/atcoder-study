N, X = map(int, input().split())
A = [i for i in map(int, input().split()) if i != X]

print(' '.join([str(i) for i in A]))


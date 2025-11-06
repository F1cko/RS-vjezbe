import heapq

def dijkstra(graf, pocetak):
    udaljenosti = {cvor: float('inf') for cvor in graf}
    udaljenosti[pocetak] = 0

    red = [(0, pocetak)]

    while red:
        trenutna_udaljenost, cvor = heapq.heappop(red)

        if trenutna_udaljenost > udaljenosti[cvor]:
            continue
        for susjed, tezina in graf[cvor]:
            nova_udaljenost = trenutna_udaljenost + tezina
            if nova_udaljenost < udaljenosti[susjed]:
                udaljenosti[susjed] = nova_udaljenost
                heapq.heappush(red, (nova_udaljenost, susjed))

    return udaljenosti
graf = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

print(dijkstra(graf, 'A'))

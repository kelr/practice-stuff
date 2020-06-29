# Incomplete, need to update to find the hamiltonian path
# for the graph.
def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        history = {}
        for ticket in tickets:
            if ticket[0] not in history:
                history[ticket[0]] = [ticket[1]]
            else:
                history[ticket[0]].append(ticket[1])
                history[ticket[0]].sort()
        print(history)
        
        curr = "JFK"
        out = []
        for num in range(len(tickets)):
            out.append(curr)
            for i,d in enumerate(history[curr]):
                print(d)
                if d in history or num == len(tickets) - 1:
                    dest = d
                    history[curr].pop(i)
            curr = dest
        out.append(curr)
        return out
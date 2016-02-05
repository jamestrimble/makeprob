import sys

class KidneyError(Exception):
    pass

class Vertex(object):
    def __init__(self, id):
        self.id = id
        self.edges_out = []
        self.edges_in = []

class Edge(object):
    def __init__(self, src, tgt, wt):
        self.src = src
        self.tgt = tgt
        self.wt = wt

def add_edge(src, tgt, wt):
    """Adds and edge from Vertex src to Vertex tgt"""
    edge = Edge(src, tgt, wt)
    src.edges_out.append(edge)
    tgt.edges_in.append(edge)

def print_instance(vv):
    print "{}\t{}".format(len(vv), sum(len(v.edges_out) for v in vv))
    for v in vv:
        for e in v.edges_out:
            print "{}\t{}\t{}".format(e.src.id, e.tgt.id, e.wt)
    print "-1\t-1\t-1"

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: python {} vertex_fail_prob edge_fail_prob\n".format(
                sys.argv[0]))
        exit(1)
    vprob = float(sys.argv[1])
    eprob = float(sys.argv[2])

    ascending = False

    lines = sys.stdin.readlines()
    n_vertices, m_edges = [int(x) for x in lines[0].split()]

    if not lines[m_edges+1].startswith("-1"):
        raise KidneyError("The number of edges in the input file appears to be incorrect")

    vv = [Vertex(id) for id in range(n_vertices)]

    for line in lines[1:m_edges+1]:
        tokens = line.split()
        src_id = int(tokens[0])
        tgt_id = int(tokens[1])
        wt = float(tokens[2])
        add_edge(vv[src_id], vv[tgt_id], wt)

    current_v = -1
    eprobs = []
    for i, v in enumerate(vv):
        for e in v.edges_out:
            if current_v != v.id:
                if eprobs:
                    print " ".join(map(str, eprobs))    
                    eprobs = []
                print vprob 
                current_v = v.id
            eprobs.append(eprob)
    if eprobs:
        print " ".join(map(str, eprobs))    


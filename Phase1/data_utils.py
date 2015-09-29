from graph import DirectedGraph, Node, Edge

def load_linqs_data(content_file, cites_file):
    graph_obj = DirectedGraph()
    class_labels = graph_nodes(graph_obj, content_file)
    graph_edges(graph_obj, cites_file)
    return graph_obj, class_labels

def graph_nodes(graph, content_file):
    content_file = open("D:\MCS\PGM\project\code\citeseer\citeseer.content", "r")
    file_content = []
    labels = []
    for con_line in content_file:
        line_array = con_line.split('\t')
        paper_content = {
            'paper_id': line_array[0],
            'class_label': line_array[-1].strip(),
            'word_attributes': line_array[1:-1],
        }
        class_label = line_array[-1].strip()
        if class_label not in labels:
            labels.append(class_label)
        file_content.append(paper_content)
    for paper in file_content:
        n = Node(paper['paper_id'], paper['word_attributes'], paper['class_label'])
        graph.add_node(n)
    return labels
def graph_edges(graph, cites_file):
    cites_file = open("D:\MCS\PGM\project\code\citeseer\citeseer.cites", "r")
    citations = dict()
    for con_line in cites_file:
        paper_array = con_line.split('\t')
        id_citing_paper = paper_array[1].strip()
        id_cited_paper = paper_array[0].strip()
        if id_citing_paper in citations:
            citations[id_citing_paper].append(id_cited_paper)
        else:
            citations[id_citing_paper] = [id_cited_paper]
    for id_citing_paper, id_cited_papers in citations.iteritems():
        for id_cited_paper in id_cited_papers:
            n = Edge(id_citing_paper, id_cited_paper)
            graph.add_edge(n)
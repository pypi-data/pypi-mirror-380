import json
import rdflib
from tinyrml import RR

def translate(map_spec, map_id, graph):
    for term_spec in map_spec:
        if "subject" in term_spec:
            translate_subject_map(term_spec, map_id, graph)
        elif "predicate" in term_spec and "object" in term_spec:
            translate_predicate_object_map(term_spec, map_id, graph)
        else:
            raise ValueError("Malformed term spec: {}".format(term_spec))
    return graph

def translate_subject_map(term_spec, map_id, graph):
    sm = rdflib.BNode()
    graph.add((map_id, RR.subjectMap, sm))
    graph.add((sm, RR.template, rdflib.Literal(term_spec["subject"])))
    if "class" in term_spec:
        graph.add((sm, RR["class"], rdflib.URIRef(term_spec["class"])))

def translate_predicate_object_map(term_spec, map_id, graph):
    pom = rdflib.BNode()
    om = rdflib.BNode()
    graph.add((map_id, RR.predicateObjectMap, pom))
    graph.add((pom, RR.predicate, rdflib.URIRef(term_spec["predicate"])))
    graph.add((pom, RR.objectMap, om))
    graph.add((om, RR.template, rdflib.Literal(term_spec["object"])))
    graph.add((om, RR.termTyoe, RR.Literal))
    if "datatype" in term_spec:
        graph.add((om, RR.datatype, rdflib.URIRef(term_spec["datatype"])))

EX = rdflib.Namespace("http://o.ra/")

if __name__ == "__main__":
    graph = rdflib.Graph()
    graph.bind("ex", EX)
    graph.bind("rr", RR)
    translate([
        {"subject": "http://o.ra/{id}"},
        {"predicate": "ex:boo", "object": "{boo}", "datatype": EX.dt}
    ], EX.foo, graph)
    print(graph.serialize())

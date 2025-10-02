from rdflib import DCTERMS, OWL, RDF, RDFS, SKOS, Namespace, URIRef

default_namespaces = [RDF, RDFS, OWL, DCTERMS, SKOS]
default_namespace_prefixes = ["rdf", "rdfs", "owl", "dcterms", "skos"]

RANK_PROPS = {RDF.type, RDFS.subClassOf}
FALLBACK_STRAT_TYPES = {
    OWL.bottomDataProperty,
    OWL.topDataProperty,
    OWL.AnnotationProperty,
    OWL.DeprecatedProperty,
    OWL.priorVersion,
    RDF.type,
    OWL.versionInfo,
    OWL.backwardCompatibleWith,
    RDFS.subClassOf,
    OWL.incompatibleWith,
    OWL.DatatypeProperty,
}


def get_default_namespace_prefixes() -> tuple[str, URIRef | Namespace]:
    return {
        prefix: ns
        for prefix, ns in zip(
            default_namespace_prefixes, default_namespaces, strict=True
        )
    }

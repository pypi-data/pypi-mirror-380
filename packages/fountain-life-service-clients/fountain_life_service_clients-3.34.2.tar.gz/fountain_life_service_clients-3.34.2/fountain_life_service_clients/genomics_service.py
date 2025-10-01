# This file was generated automatically. Do not edit it directly.
from typing import (
    List,
    Literal,
    NotRequired,
    Optional,
    TypedDict,
    Union,
    Unpack,
    cast,
)
from urllib.parse import quote

from fountain_life_service_clients._base_client import (
    AlphaConfig,
    AlphaResponse,
    BaseClient,
)


class Sample(TypedDict):
    sampleId: str
    patientId: NotRequired[str]


class GetVariantSetResponse(TypedDict):
    id: str
    datasetId: str
    patientId: NotRequired[str]
    samples: NotRequired[List[Sample]]


SearchVariantsRequest = TypedDict(
    "SearchVariantsRequest",
    {
        "variantSetIds": str,
        "include": NotRequired[str],
        "variantId": NotRequired[Union[str, List[str]]],
        "sequenceType": NotRequired[Union[Literal["somatic"], Literal["germline"]]],
        "gene": NotRequired[Union[str, List[str]]],
        "aminoAcidChange": NotRequired[Union[str, List[str]]],
        "drugAssociations": NotRequired[bool],
        "hasJaxKnowledge": NotRequired[bool],
        "transcript_in_jaxckb": NotRequired[bool],
        "cosmic_sample_count": NotRequired[float],
        "class": NotRequired[Union[str, List[str]]],
        "group": NotRequired[Union[str, List[str]]],
        "impact": NotRequired[Union[str, List[str]]],
        "biotype": NotRequired[Union[str, List[str]]],
        "rs_id": NotRequired[Union[str, List[str]]],
        "chromosome": NotRequired[Union[str, List[str]]],
        "clinvar_allele_id": NotRequired[Union[str, List[str]]],
        "clinvar_disease": NotRequired[Union[str, List[str]]],
        "clinvar_review": NotRequired[Union[str, List[str]]],
        "clinvar_significance": NotRequired[Union[str, List[str]]],
        "clinvar_submission": NotRequired[Union[str, List[str]]],
        "transcript_gene": NotRequired[Union[str, List[str]]],
        "transcript_gene_id": NotRequired[Union[str, List[str]]],
        "transcript_classification": NotRequired[Union[str, List[str]]],
        "transcript_group": NotRequired[Union[str, List[str]]],
        "transcript_impact": NotRequired[Union[str, List[str]]],
        "transcript_id": NotRequired[Union[str, List[str]]],
        "transcript_biotype": NotRequired[Union[str, List[str]]],
        "transcript_exon_intron_rank": NotRequired[Union[str, List[str]]],
        "transcript_hgvs_amino_acid_change": NotRequired[Union[str, List[str]]],
        "transcript_nucleotide_change": NotRequired[Union[str, List[str]]],
        "transcript_jax_protein_effect": NotRequired[Union[str, List[str]]],
        "transcript_jax_knowledge": NotRequired[Union[str, List[str]]],
        "cosmic_id": NotRequired[Union[str, List[str]]],
        "cosmic_mutation_status": NotRequired[Union[str, List[str]]],
        "cosmic_histology": NotRequired[Union[str, List[str]]],
        "cosmic_tumor_site": NotRequired[Union[str, List[str]]],
        "dbnsfp_fathmm_pred": NotRequired[Union[str, List[str]]],
        "dbnsfp_mutationtaster_pred": NotRequired[Union[str, List[str]]],
        "dbnsfp_sift_pred": NotRequired[Union[str, List[str]]],
        "sample_zygosity": NotRequired[Union[str, List[str]]],
        "sample_genotype": NotRequired[Union[str, List[str]]],
        "sample_filter": NotRequired[Union[str, List[str]]],
        "sample_vendsig": NotRequired[Union[str, List[str]]],
        "sequence_type": NotRequired[Union[str, List[str]]],
        "position": NotRequired[Union[str, List[str]]],
        "clinvar_near_variant": NotRequired[Union[str, List[str]]],
        "cosmic_near_variant": NotRequired[Union[str, List[str]]],
        "minimum_allele_frequency": NotRequired[Union[str, List[str]]],
        "maximum_allele_frequency": NotRequired[Union[str, List[str]]],
        "population_allele_frequency": NotRequired[Union[str, List[str]]],
        "exac_allele_frequency": NotRequired[Union[str, List[str]]],
        "exac_homozygous": NotRequired[Union[str, List[str]]],
        "dbnsfp_damaging_count": NotRequired[Union[str, List[str]]],
        "dbnsfp_damaging_predictor": NotRequired[Union[str, List[str]]],
        "dbnsfp_damaging_vote": NotRequired[Union[str, List[str]]],
        "dbnsfp_fathmm_rankscore": NotRequired[Union[str, List[str]]],
        "dbnsfp_mean_rankscore": NotRequired[Union[str, List[str]]],
        "dbnsfp_mean_rankscore_predictor": NotRequired[Union[str, List[str]]],
        "dbnsfp_mutationtaster_rankscore": NotRequired[Union[str, List[str]]],
        "dbnsfp_sift_rankscore": NotRequired[Union[str, List[str]]],
        "sample_allele_frequency": NotRequired[Union[str, List[str]]],
        "sample_quality": NotRequired[Union[str, List[str]]],
        "sample_read_depth": NotRequired[Union[str, List[str]]],
        "sample_alternate_read_depth": NotRequired[Union[str, List[str]]],
        "sample_reference_read_depth": NotRequired[Union[str, List[str]]],
        "nextPageToken": NotRequired[str],
        "pageSize": NotRequired[float],
    },
)


class Clinvar(TypedDict):
    alleleId: str
    disease: str
    review: str
    significance: str
    submission: str
    nearVariant: float


class Cosmic(TypedDict):
    sampleCount: float
    nearVariant: float
    tumorSite: NotRequired[str]
    histology: NotRequired[str]
    cosmicId: NotRequired[str]
    status: NotRequired[str]


EnsemblCanonItem = TypedDict(
    "EnsemblCanonItem",
    {
        "class": NotRequired[str],
        "impact": NotRequired[str],
        "gene": NotRequired[str],
        "geneId": NotRequired[str],
        "transcriptId": NotRequired[str],
        "biotype": NotRequired[str],
        "exonIntronRank": NotRequired[str],
        "nucleotideChange": NotRequired[str],
        "aminoAcidChange": NotRequired[str],
        "hgvsAminoAcidChange": NotRequired[str],
    },
)


class Dbnsfp(TypedDict):
    siftPred: List[Optional[str]]
    mutationTasterPred: List[Optional[str]]
    fathmmPred: List[Optional[str]]


EnsemblItem = TypedDict(
    "EnsemblItem",
    {
        "class": NotRequired[str],
        "impact": NotRequired[str],
        "gene": NotRequired[str],
        "geneId": NotRequired[str],
        "transcriptId": NotRequired[str],
        "biotype": NotRequired[str],
        "exonIntronRank": NotRequired[str],
        "nucleotideChange": NotRequired[str],
        "aminoAcidChange": NotRequired[str],
        "hgvsAminoAcidChange": NotRequired[str],
    },
)


class Vcf(TypedDict):
    quality: float
    filter: str
    variantAllelicFrequency: float
    coverage: str


class Item(TypedDict):
    id: str
    chromosome: str
    reference: str
    alternate: str
    position: float
    minimumAlleleFrequency: float
    maximumAlleleFrequency: float
    gnomadAlleleFrequency: float
    gnomadHomozygous: float
    rsid: str
    zygosity: str
    clinvar: Clinvar
    cosmic: Cosmic
    ensemblCanon: List[EnsemblCanonItem]
    dbnsfp: Dbnsfp
    ensembl: NotRequired[List[EnsemblItem]]
    vcf: NotRequired[Vcf]


class Links(TypedDict):
    self: str
    next: NotRequired[str]


class Invalid(TypedDict):
    variantSetIds: List[str]


class SearchVariantsResponse(TypedDict):
    items: NotRequired[List[Item]]
    links: Links
    sorted: NotRequired[bool]
    count: NotRequired[float]
    invalid: NotRequired[Invalid]


class GenomicsServiceClient(BaseClient):
    def __init__(self, **cfg: Unpack[AlphaConfig]):
        kwargs = {"target": "lambda://genomics-service:deployed", **(cfg or {})}
        super().__init__(**kwargs)

    async def get_variant_set(self, id: str):
        """Get a variant set by id"""
        res = await self.client.request(
            path=f"/v1/genomics/variantsets/{quote(id)}", method="GET"
        )
        return cast(AlphaResponse[GetVariantSetResponse], res)

    async def search_variants(self, body: SearchVariantsRequest):
        """Search for variants"""
        res = await self.client.request(
            path="/v1/genomics/variants/_search", method="POST", body=cast(dict, body)
        )
        return cast(AlphaResponse[SearchVariantsResponse], res)

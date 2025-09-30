"""
Module for parsing HGVS variant descriptions.
"""

import functools
import os

from lark import Lark, Token, Transformer, Tree
from lark.exceptions import UnexpectedCharacters, UnexpectedEOF

from .exceptions import UnexpectedCharacter, UnexpectedEnd
from .util import all_tree_children_equal, data_equals, get_child

AMBIGUITIES = [
    {
        "type": "insert_location | insert_length - length",
        # 10 ("inserted" start rule)
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "insert"
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [1, 0], "length")
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain_location_and_substitution | variant_certain_location",
        # R1:10
        # on the protein side
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 0], "location")
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 1], "substitution")
            and data_equals(children, [1, 0], "location")
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain_repeat | variant_certain_substitution - repeat",
        # PREF:p.Ala2[10]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == "variant_certain"
            and children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 1], "substitution")
            and data_equals(children, [1, 1, 0], "inserted")
            and data_equals(children, [1, 1, 0, 0], "insert")
            and len(get_child(children, [1, 1, 0, 0]).children) == 1
            and isinstance(get_child(children, [1, 1, 0, 0, 0]), Tree)
            and data_equals(children, [1, 1, 0, 0, 0], "length")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_repeat | variant_certain_substitution - repeat 2",
        # PREF:p.254AE[3]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == "variant_certain"
            and children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 1], "substitution")
            and data_equals(children, [1, 1, 0], "inserted")
            and data_equals(children, [1, 1, 0, 0], "insert")
            and len(get_child(children, [0, 1, 0, 0]).children) == 2
            and isinstance(get_child(children, [0, 1, 0, 0]), Tree)
            and data_equals(children, [1, 1, 0, 0, 1], "repeat_number")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_repeat | variant_certain_substitution - substitution 1",
        # PREF:p.Trp26Ter, LRG_199p1:p.Trp24Cys, PREF:p.Trp26*,
        # PREF:p.[Ser44Arg;Trp46Arg]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 1], "substitution")
            and data_equals(children, [1, 1, 0], "inserted")
            and data_equals(children, [1, 1, 0, 0], "insert")
            and len(get_child(children, [1, 1, 0, 0]).children) == 1
            and isinstance(get_child(children, [1, 1, 0, 0, 0]), Token)
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain_repeat | variant_certain_substitution - substitution 2",
        # for protein variants: 10R2:10_20
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 1], "substitution")
            and data_equals(children, [1, 1, 0], "inserted")
            and data_equals(children, [1, 1, 0, 0], "insert")
            and data_equals(children, [1, 1, 0, 0, 0], "description_protein")
        ),
        "selected": 1,
    },
    {
        "type": "insertion | repeat - insertion",
        # 10_11insNM_000001.1:c.100_200 ("variant" start rule)
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "insertion")
            and data_equals(children, [1, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "insertion | repeat | substitution - insertion",
        # R1:[1del;10_11insR2:2del]
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "insertion")
            and data_equals(children, [1, 1], "repeat")
            and data_equals(children, [2, 1], "substitution")
        ),
        "selected": 0,
    },
    {
        "type": "deletion | deletion_insertion | repeat - deletion_insertion",
        # 10_11insNM_000001.1:c.100_200 ("variant" start rule)
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data
            == children[1].data
            == children[2].data
            == "variant_certain"
            and data_equals(children, [0, 1], "deletion")
            and data_equals(children, [1, 1], "deletion_insertion")
            and data_equals(children, [2, 1], "repeat")
        ),
        "selected": 1,
    },
    {
        "type": "deletion | deletion_insertion | repeat | substitution - deletion_insertion",
        # R1:1delinsR2:2del
        "conditions": lambda children: (
            len(children) == 4
            and children[0].data == children[1].data == "variant_certain"
            and children[2].data == children[3].data == "variant_certain"
            and data_equals(children, [0, 1], "deletion")
            and data_equals(children, [1, 1], "deletion_insertion")
            and data_equals(children, [2, 1], "repeat")
            and data_equals(children, [3, 1], "substitution")
        ),
        "selected": 1,
    },
    {
        "type": "deletion | deletion_insertion | repeat | substitution - deletion_insertion",
        # R1:[1del;10_11insR2:2del]
        "conditions": lambda children: (
            len(children) == 4
            and children[0].data
            == children[1].data
            == children[2].data
            == children[3].data
            == "variant_certain"
            and data_equals(children, [0, 1], "deletion")
            and data_equals(children, [1, 1], "deletion_insertion")
            and data_equals(children, [2, 1], "repeat")
            and data_equals(children, [3, 1], "substitution")
        ),
        "selected": 1,
    },
    {
        "type": "inversion | repeat - inversion",
        # R1(t1):c.-5-3inv
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "inversion")
            and data_equals(children, [1, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "conversion | repeat - conversion",
        # R1:g.10_20conR2:40_50
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "conversion")
            and data_equals(children, [1, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "repeat | location - location",
        # REF:g.123?
        # REF:g.??
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == "variant_certain"
            and children[1].data == "variant_certain"
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 0], "location")
            and len(get_child(children, [1]).children) == 1
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain | variant_predicted - variant_predicted",
        # R1(R2(R3)):g.(10_15)
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant"
            and data_equals(children, [0, 0], "variant_certain")
            and data_equals(children, [1, 0], "variant_predicted")
            and len(get_child(children, [0, 0]).children) == 1
            and data_equals(children, [0, 0, 0], "location")
        ),
        "selected": 0,
    },
    {
        "type": "variants_certain_variant_predicted | variants_predicted_variant_certain - variants_predicted",
        # R1(R2(R3)):g.(10_15)
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variants"
            and data_equals(children, [0, 0], "variants_certain")
            and data_equals(children, [1, 0], "variants_predicted")
            and len(get_child(children, [1, 0]).children) == 1
            and data_equals(children, [0, 0, 0], "variant")
            and data_equals(children, [1, 0, 0], "variant")
            and data_equals(children, [0, 0, 0, 0], "variant_certain")
            and data_equals(children, [1, 0, 0, 0], "variant_certain")
        ),
        "selected": 0,
    },
    {
        "type": "variants_certain_variant_predicted | variants_predicted_variant_certain - variants_predicted",
        # NP_003997.1:p.(Trp24Cys)
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variants"
            and data_equals(children, [0, 0], "variants_certain")
            and data_equals(children, [1, 0], "variants_predicted")
            and len(get_child(children, [1, 0]).children) == 1
            and data_equals(children, [0, 0, 0], "variant")
            and data_equals(children, [1, 0, 0], "variant")
            and data_equals(children, [0, 0, 0, 0], "variant_predicted")
            and data_equals(children, [1, 0, 0, 0], "variant_certain")
        ),
        "selected": 1,
    },
    {
        "type": "description_dna | description_protein - description_dna",
        # R1:100insA
        # - we opt for "description_dna"
        # TODO: Leave it undefined and do the check based on
        #     the reference type?
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "description"
            and data_equals(children, [0, 0], "description_dna")
            and data_equals(children, [1, 0], "description_protein")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain-location_repeat|repeat - variant_certain-location",
        # NM_000492.4:c.1210-34_1210-6
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data
            == children[1].data
            == children[2].data
            == "variant_certain"
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [2]).children) == 1
            and data_equals(children, [2, 0], "location")
        ),
        "selected": 2,
    },
    {
        "type": "variant_certain-location_repeat|location_inversion - inversion",
        # NC_000015.9(NM_001012338.3):c.396-6644_1397-29766inv
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data
            == children[1].data
            == children[2].data
            == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "inversion")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [2]).children) == 2
            and data_equals(children, [2, 0], "location")
            and data_equals(children, [2, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_duplication | variant_certain_repeat - duplication",
        # R1:c.10-5_10-2dupR2:10
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "duplication")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_deletion | variant_certain_repeat - deletion",
        # R1:c.10-5_10-2delR2:10del
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "deletion")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [0, 1]).children) == 1
            and data_equals(children, [0, 1, 0], "inserted")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_delins | variant_certain_delins - one insert",
        # R1:c.10-5_10-2delinsTCTR2.2:c.10insT
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "deletion_insertion"
            and len(get_child(children, [1]).children) == 1
            and data_equals(children, [0, 0], "inserted")
        ),
        "selected": 1,
    },
    # TODO: revisit the next ones in the repeats context.
    {
        "type": "variant_certain_repeat | variant_certain_repeat_length - length 0",
        # R1:c.10-2[5]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [0, 1]).children) == 1
            and data_equals(children, [0, 1, 0], "inserted")
            and len(get_child(children, [0, 1, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0], "insert")
            and len(get_child(children, [0, 1, 0, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0, 0], "length")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_repeat | variant_certain_repeat_length - length 1",
        # R1:c.10-2[5]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [1, 1]).children) == 1
            and data_equals(children, [1, 1, 0], "inserted")
            and len(get_child(children, [1, 1, 0]).children) == 1
            and data_equals(children, [1, 1, 0, 0], "insert")
            and len(get_child(children, [1, 1, 0, 0]).children) == 1
            and data_equals(children, [1, 1, 0, 0, 0], "length")
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain_repeat | variant_certain_repeat_range_length - length 0",
        # R1:c.10-2_10-4[5]
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [2]).children) == 2
            and data_equals(children, [2, 0], "location")
            and data_equals(children, [2, 1], "repeat")
            and len(get_child(children, [0, 1]).children) == 1
            and data_equals(children, [0, 1, 0], "inserted")
            and len(get_child(children, [0, 1, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0], "insert")
            and len(get_child(children, [0, 1, 0, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0, 0], "length")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain_repeat | variant_certain_repeat_range_length - length 1",
        # R1:c.10-2_10-4[5]
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [2]).children) == 2
            and data_equals(children, [2, 0], "location")
            and data_equals(children, [2, 1], "repeat")
            and len(get_child(children, [1, 1]).children) == 1
            and data_equals(children, [1, 1, 0], "inserted")
            and len(get_child(children, [1, 1, 0]).children) == 1
            and data_equals(children, [1, 1, 0, 0], "insert")
            and len(get_child(children, [1, 1, 0, 0]).children) == 1
            and data_equals(children, [1, 1, 0, 0, 0], "length")
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain_repeat | variant_certain_repeat_range_length - length 2",
        # R1:c.10-2_10-4[5]
        "conditions": lambda children: (
            len(children) == 3
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
            and len(get_child(children, [2]).children) == 2
            and data_equals(children, [2, 0], "location")
            and data_equals(children, [2, 1], "repeat")
            and len(get_child(children, [2, 1]).children) == 1
            and data_equals(children, [2, 1, 0], "inserted")
            and len(get_child(children, [2, 1, 0]).children) == 1
            and data_equals(children, [2, 1, 0, 0], "insert")
            and len(get_child(children, [2, 1, 0, 0]).children) == 1
            and data_equals(children, [2, 1, 0, 0, 0], "length")
        ),
        "selected": 2,
    },
    {
        "type": "variant_certain_repeat | variant_certain_substitution - 2",
        # for protein descriptions
        # STR:D5S818
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and isinstance(get_child(children, [0, 0, 0]), Tree)
            and data_equals(children, [0, 0, 0], "point")
            and len(get_child(children, [0, 0, 0]).children) == 2
            and isinstance(get_child(children, [0, 0, 0, 0]), Token)
            and isinstance(get_child(children, [0, 0, 0, 1]), Token)
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and isinstance(get_child(children, [1, 0, 0]), Tree)
            and data_equals(children, [1, 0, 0], "point")
            and len(get_child(children, [1, 0, 0]).children) == 2
            and isinstance(get_child(children, [1, 0, 0, 0]), Token)
            and isinstance(get_child(children, [1, 0, 0, 1]), Token)
            and data_equals(children, [1, 1], "substitution")
        ),
        "selected": 1,
    },
    {
        "type": "deletion_insertion | deletion_insertion | ... nested - 0",
        # REF_1:10del REF_2:20insA REF_3:30insT
        "conditions": lambda children: (
            len(children) >= 2
            and children[0].data == children[1].data == "deletion_insertion"
            and len(get_child(children, [0]).children) == 2
            and len(get_child(children, [1]).children) == 2
            and isinstance(get_child(children, [1, 0]), Tree)
            and len(get_child(children, [1, 0]).children) == 1
            and isinstance(get_child(children, [1, 1]), Tree)
            and len(get_child(children, [1, 1]).children) == 1
            and data_equals(children, [1, 0, 0], "insert")
            and len(get_child(children, [1, 0, 0]).children) == 1
            and (
                data_equals(children, [1, 0, 0, 0], "description_dna")
                or data_equals(children, [1, 0, 0, 0], "description_protein")
            )
        ),
        "selected": 1,
    },
    {
        "type": "inserted | inserted ",
        # in the inserted rule
        # NG_000001.1(NM_000002.3):c.(170_?)_420+60[19]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "inserted"
            and len(get_child(children, [0]).children) == 1
            and data_equals(children, [0, 0], "insert")
            and len(get_child(children, [0, 0]).children) == 1
            and data_equals(children, [0, 0, 0], "description_dna")
            and len(get_child(children, [1]).children) == 1
            and data_equals(children, [1, 0], "insert")
            and len(get_child(children, [1, 0]).children) == 2
            and data_equals(children, [1, 0, 0], "description_dna")
            and data_equals(children, [1, 0, 1], "repeat_number")
        ),
        "selected": 1,
    },
    {
        "type": "inserted insert repeat_mixed - 0 ",
        # in the variant rule
        # 123_191delins[CAG[19];CAA[4]]
        "conditions": lambda children: (
            all_tree_children_equal(children, "inserted")
            and all_tree_children_equal(children[0].children, "insert")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain repeat | variant_certain substitution - 0 ",
        # for proteins
        # R1:p.Ala1207_Asp1208Thr1207_Asn1208
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [0, 1]).children) == 1
            and data_equals(children, [0, 1, 0], "inserted")
            and len(get_child(children, [0, 1, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0], "insert")
            and len(get_child(children, [0, 1, 0, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0, 0], "repeat_mixed")
            and len(get_child(children, [0, 1, 0, 0, 0]).children) == 2
            and data_equals(children, [0, 1, 0, 0, 0, 1], "repeat_number")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "substitution")
        ),
        "selected": 0,
    },
    {
        "type": "variant_certain repeat | variant_certain substitution - 1 ",
        # for proteins
        # R1:p.Ala1207_Asp1208Thr1207_Asn1208[10]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [0, 1]).children) == 1
            and data_equals(children, [0, 1, 0], "inserted")
            and len(get_child(children, [0, 1, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0], "insert")
            and len(get_child(children, [0, 1, 0, 0]).children) == 1
            and data_equals(children, [0, 1, 0, 0, 0], "location")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "substitution")
        ),
        "selected": 1,
    },
    {
        "type": "variant_certain repeat | variant_certain substitution - 1 ",
        # for proteins
        # R1:54_149Ala[23]Ter[1]
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "substitution")
            and get_child(children, [0, 1, 0]) == get_child(children, [1, 1, 0])
        ),
        "selected": 0,
    },
    {
        "type": "repeat | repeat - 0 ",
        # NG_007524:28578-181-182
        "conditions": lambda children: (
            len(children) == 2
            and children[0].data == children[1].data == "variant_certain"
            and len(get_child(children, [0]).children) == 2
            and data_equals(children, [0, 0], "location")
            and data_equals(children, [0, 1], "repeat")
            and len(get_child(children, [1]).children) == 2
            and data_equals(children, [1, 0], "location")
            and data_equals(children, [1, 1], "repeat")
        ),
        "selected": 0,
    },
    {
        "type": "insert description_dna repeat_number | insert description_dna - 0 ",
        # inserted
        # NG_000001.1(NM_000002.3):c.(170_?)_420+60[19]
        "conditions": lambda children: (
                len(children) == 2
                and children[0].data == children[1].data == "insert"
                and len(get_child(children, [0]).children) == 2
                and data_equals(children, [0, 0], "description_dna")
                and data_equals(children, [0, 1], "repeat_number")
                and len(get_child(children, [1]).children) == 1
                and data_equals(children, [1, 0], "description_dna")
        ),
        "selected": 0,
    },
    {
        "type": "insert location repeat_number | insert repeat_mixed - 0 ",
        # test_variant_to_model 123_191[CAG[19];CAA[4];10_15[6]
        "conditions": lambda children: (
                len(children) == 2
                and children[0].data == children[1].data == "insert"
                and len(get_child(children, [0]).children) in [2, 3]
                and data_equals(children, [0, 1], "repeat_number")
                and len(get_child(children, [1]).children) == 1
                and data_equals(children, [1, 0], "repeat_mixed")
        ),
        "selected": 0,
    },
    {
        "type": "insert location repeat_number | insert repeat_mixed - 0 ",
        # test_variant_to_model 123_191[CAG[19];CAA[4];10_15[6]
        "conditions": lambda children: (
                len(children) == 2
                and children[0].data == children[1].data == "insert"
                and len(get_child(children, [0]).children) == 2
                and data_equals(children, [0, 0], "location")
                and data_equals(children, [0, 1], "repeat_number")
                and len(get_child(children, [1]).children) == 1
                and data_equals(children, [1, 0], "repeat_mixed")
        ),
        "selected": 0,
    },
    {
        "type": "insert description_dna inv | insert description_dna - 1 ",
        "conditions": lambda children: (
                len(children) == 2
                and children[0].data == children[1].data == "insert"
                and len(get_child(children, [0]).children) == 2
                and data_equals(children, [0, 0], "description_dna")
                and isinstance(get_child(children, [0, 1]), Token)
                and len(get_child(children, [1]).children) == 1
                and data_equals(children, [1, 0], "description_dna")
        ),
        "selected": 1,
    },
]


class AmbigTransformer(Transformer):
    def _ambig(self, children):
        # from lark.tree import pydot__tree_to_png
        # pydot__tree_to_png(Tree("ambig", children), "ambig.png")
        for ambig in AMBIGUITIES:
            if ambig["conditions"](children):
                # from lark.tree import pydot__tree_to_png
                # pydot__tree_to_png(Tree("ambig", children), "ambig_2.png")
                return children[ambig["selected"]]
        raise Exception("Ambiguity not solved.")


class ProteinTransformer(Transformer):
    def p_variants(self, children):
        return Tree("variants", children)

    def p_variants_certain(self, children):
        return Tree("variants_certain", children)

    def p_variants_predicted(self, children):
        return Tree("variants_predicted", children)

    def p_variant(self, children):
        return Tree("variant", children)

    def p_variant_certain(self, children):
        return Tree("variant_certain", children)

    def p_variant_predicted(self, children):
        return Tree("variant_predicted", children)

    def p_location(self, children):
        return Tree("location", children)

    def p_range(self, children):
        return Tree("range", children)

    def p_length(self, children):
        return Tree("length", children)

    def p_point(self, children):
        return Tree("point", children)

    def p_deletion(self, children):
        return Tree("deletion", children)

    def p_deletion_insertion(self, children):
        return Tree("deletion_insertion", children)

    def p_duplication(self, children):
        return Tree("duplication", children)

    def p_equal(self, children):
        return Tree("equal", children)

    def extension(self, children):
        return Tree("extension", children)

    def extension_n(self, children):
        point = Tree(
            "point", [Token("NUMBER", children[0].value), Token("OUTSIDE_CDS", "-")]
        )
        location = [Tree("location", [point])]
        return Tree("inserted", [Tree("insert", location)])

    def extension_c(self, children):
        new_children = []
        for child in children:
            if isinstance(child, Token):
                new_children.append(Tree("insert", [Token("P_SEQUENCE", child.value)]))
            else:
                new_children.append(Tree("insert", [child]))
        if new_children:
            return Tree("extension", [Tree("inserted", new_children)])
        else:
            return Tree("extension", [])

    def frame_shift(self, children):
        new_children = []
        for child in children:
            if isinstance(child, Token):
                new_children.append(Tree("insert", [Token("P_SEQUENCE", child.value)]))
            else:
                new_children.append(Tree("insert", [child]))
        if new_children:
            return Tree("frame_shift", [Tree("inserted", new_children)])
        else:
            return Tree("frame_shift", [])

    def p_insertion(self, children):
        return Tree("insertion", children)

    def p_repeat(self, children):
        return Tree("repeat", children)

    def p_substitution(self, children):
        return Tree("substitution", children)

    def p_inserted(self, children):
        return Tree("inserted", children)

    def p_insert(self, children):
        return Tree("insert", children)

    def p_repeat_number(self, children):
        return Tree("repeat_number", children)

    def p_repeat_mixed(self, children):
        return Tree("repeat_mixed", children)

    def P_COORDINATE_SYSTEM(self, name):
        return Token("COORDINATE_SYSTEM", name.value)


class FinalTransformer(Transformer):
    def variants(self, children):
        if children[0].data == "variants_certain":
            return Tree("variants", children[0].children)
        if children[0].data == "variants_predicted":
            return Tree("variants_predicted", children[0].children)
        return Tree("variants", children)

    def variant_predicted(self, children):
        return Tree("variant_predicted", children[0].children)

    def variant(self, children):
        if children[0].data == "variant_certain":
            return Tree("variant", children[0].children)
        elif children[0].data == "variant_predicted":
            return Tree("variant_predicted", children[0].children)


def _read_grammar_file(file_name):
    grammar_path = os.path.join(os.path.dirname(__file__), f"ebnf/{file_name}")
    with open(grammar_path) as grammar_file:
        return grammar_file.read()


def _replace_annon_terminals(grammar):
    updated_grammar = grammar
    terminals = {
        "PREDICTED_EQUAL": "(=)",
        "LPAR_LSQB": "([",
        "LSQB_LPAR": "[(",
        "RSQB_RPAR": "])",
        "RPAR_RSQB": ")]",
    }
    for name in terminals:
        updated_grammar = updated_grammar.replace('"terminals[name]"', name)
        updated_grammar += f'\n\n{name}: "{terminals[name]}"'
    return updated_grammar


class HgvsParser:
    """
    HGVS parser object.
    """

    def __init__(self, grammar_path=None, start_rule=None, ignore_white_spaces=True):
        """
        :arg str grammar_path: Path to a different EBNF grammar file.
        :arg str start_rule: Alternative start rule for the grammar.
        :arg bool ignore_white_spaces: Ignore or not white spaces in the description.
        """
        self._grammar_path = grammar_path
        self._start_rule = start_rule
        self._ignore_whitespaces = ignore_white_spaces
        self._create_parser()

    def _create_parser(self):
        if self._grammar_path:
            with open(self._grammar_path) as grammar_file:
                grammar = grammar_file.read()
        else:
            grammar = _read_grammar_file("top.g")
            grammar += _read_grammar_file("dna.g")
            grammar += _read_grammar_file("protein.g")
            grammar += _read_grammar_file("reference.g")
            grammar += _read_grammar_file("common.g")
            grammar = _replace_annon_terminals(grammar)

        start_rule = self._start_rule if self._start_rule else "description"

        if self._ignore_whitespaces:
            grammar += "\n%import common.WS\n%ignore WS"

        self._parser = Lark(
            grammar, parser="earley", start=start_rule, ambiguity="explicit"
        )

    def parse(self, description):
        """
        Parse the provided description.

        :arg str description: An HGVS description.
        :returns: A parse tree.
        :rtype: lark.Tree
        """
        try:
            parse_tree = self._parser.parse(description)
        except UnexpectedCharacters as e:
            raise UnexpectedCharacter(e, description)
        except UnexpectedEOF as e:
            raise UnexpectedEnd(e, description)
        return parse_tree

    def status(self):
        """
        Print parser's status information.
        """
        print("Parser type: %s" % self._parser_type)
        if self._parser_type == "lark":
            print(" Employed grammar path: %s" % self._grammar_path)
            print(" Options:")
            print("  Parser class: %s" % self._parser.parser_class)
            print("  Parser: %s" % self._parser.options.parser)
            print("  Lexer: %s" % self._parser.options.lexer)
            print("  Ambiguity: %s" % self._parser.options.ambiguity)
            print("  Start: %s" % self._parser.options.start)
            print("  Tree class: %s" % self._parser.options.tree_class)
            print(
                "  Propagate positions: %s" % self._parser.options.propagate_positions
            )


@functools.lru_cache
def get_parser(grammar_path=None, start_rule=None):
    return HgvsParser(grammar_path, start_rule)


def parse(description, grammar_path=None, start_rule=None):
    """
    Parse the provided HGVS `description`, or the description part,
    e.g., a location, a variants list, etc., if an appropriate alternative
    `start_rule` is provided.

    :arg str description: Description (or description part) to be parsed.
    :arg str grammar_path: Path towards a different grammar file.
    :arg str start_rule: Alternative start rule for the grammar.
    :returns: Parse tree.
    :rtype: lark.Tree
    """
    parser = get_parser(grammar_path, start_rule)

    # from lark.tree import pydot__tree_to_png
    # pydot__tree_to_png(parser.parse(description), "tree.png")

    return FinalTransformer().transform(
        AmbigTransformer().transform(
            ProteinTransformer().transform(parser.parse(description))
        )
    )

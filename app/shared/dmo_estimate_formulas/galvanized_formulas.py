from math import ceil
from typing import List

from app.decking_quote.decking_quote_model import Layout
from app.shared.dmo_estimate_formulas.frame_formulas import estimate_frame_material
from app.shared.material_order_model import MaterialOrderSpecItem


def get_qty_by_reference(dmo_materials: List[MaterialOrderSpecItem] | None, reference: str) -> float:
    if dmo_materials:
        for material in dmo_materials:
            if material.reference_snapshot == reference:
                return getattr(material, "estimated_qty", 0.0)

    return 0.0


def estimate_galvanized_stringer(layout: Layout | None) -> int:
    if layout and layout.stairs:
        return sum(ceil(stair.width + 1) for stair in layout.stairs if stair.width)

    return 0


def estimate_galvanized_dtt1z(layout: Layout | None) -> int:
    if layout and layout.dtt1z:
        return layout.dtt1z

    return 0


def estimate_galvanized_dtt2z(layout: Layout | None) -> int:
    if layout and layout.dtt2z:
        return layout.dtt2z

    return 0


def estimate_galvanized_postbase(layout: Layout | None, size: str = "") -> int:
    if layout:
        posts: float = 0

        for area in layout.main_areas if layout.main_areas else []:
            if area.support_post_grade and area.support_post_grade.size == size and area.support_post_grade.qty:
                posts += area.support_post_grade.qty

        for area in layout.lading_areas if layout.lading_areas else []:
            if area.support_post_grade and area.support_post_grade.size == size and area.support_post_grade.qty:
                posts += area.support_post_grade.qty

        return int(posts)

    return 0


def estimate_galvanized_facemount_langle(layout: Layout | None, size: List[str] = []) -> int:
    if layout and layout.main_areas:
        # Sempre colocar 4 se houver algum Deck Area correspondenta ao deck grade size
        exists = any(area.deck_grade in size for area in layout.main_areas)

        return 4 if exists else 0

    return 0


def estimate_galvanized_anchors(layout: Layout) -> float:
    total: float = 0.0

    for area in layout.main_areas if layout.main_areas else []:
        total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty and area.ledger_attaches_to == "concrete" else 0

    for area in layout.lading_areas if layout.lading_areas else []:
        total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty and area.ledger_attaches_to == "concrete" else 0

    return total * 1.333 / 10


def estimate_galvanized_fastener(layout: Layout | None) -> float:
    if layout:
        total: float = 0.0

        for area in layout.main_areas if layout.main_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty and area.ledger_attaches_to == "wood" else 0

        for area in layout.lading_areas if layout.lading_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty and area.ledger_attaches_to == "wood" else 0

        WOOD_RAILLING_POSTS = 0
        return (total * 1.333 + WOOD_RAILLING_POSTS * 4) / 50

    return 0.0


def estimate_galvanized_dripedge(layout: Layout | None) -> float:
    if layout:
        total: float = 0.0

        for area in layout.main_areas if layout.main_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty else 0

        for area in layout.lading_areas if layout.lading_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty else 0

        return total / 25

    return 0.0


def estimate_galvanized_flashingtape(layout: Layout | None) -> float:
    if layout:
        total: float = 0.0

        for area in layout.main_areas if layout.main_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty else 0

        for area in layout.lading_areas if layout.lading_areas else []:
            total += area.ledger_board.qty if area.ledger_board and area.ledger_board.qty else 0

        return total / 75

    return 0.0


def estimate_galvanized_nailbox(layout: Layout | None) -> int:
    if layout:
        if layout.main_areas or layout.lading_areas or layout.stairs:
            return 1

    return 0


def estimate_galvanized_butyltape(layout: Layout | None) -> float:
    if layout:
        total: float = 0.0

        total += estimate_frame_material(layout, '2x6')
        total += estimate_frame_material(layout, '2x8')
        total += estimate_frame_material(layout, '2x10')
        total += estimate_frame_material(layout, '2x12')

        return total / 50

    return 0.0


def estimate_galvanized_joists(layout: Layout | None, dmo_materials: List[MaterialOrderSpecItem] | None, size: str = "") -> float:
    if layout:

        width: float = 0.0

        if layout.main_areas:
            for area in layout.main_areas:
                width += area.width if area.width and area.deck_grade == size else 0.0

        if layout.lading_areas:
            for landing in layout.lading_areas:
                width += landing.width if landing.width and landing.deck_grade == size else 0.0

        facemount_langle: float = 0
        if size == "2x6":
            facemount_langle = get_qty_by_reference(dmo_materials, "LUS26-2Z")

        if size == "2x8":
            facemount_langle = get_qty_by_reference(dmo_materials, "LUS28-2Z")

        if size == "2x10":
            facemount_langle = get_qty_by_reference(dmo_materials, "LUS210-2Z")

        if size == "2x12":
            facemount_langle = get_qty_by_reference(dmo_materials, "HU212-2")

        return (width * 0.75 * 2) - facemount_langle

    return 0


def estimate_galvanized_hurricane(dmo_materials: List[MaterialOrderSpecItem] | None) -> float:
    if dmo_materials:
        sum: float = 0.0

        for material in dmo_materials:
            sum += material.estimated_qty if material.reference_snapshot == "LUS26Z" else 0
            sum += material.estimated_qty if material.reference_snapshot == "LUS28Z" else 0
            sum += material.estimated_qty if material.reference_snapshot == "LUS210Z" else 0
            sum += material.estimated_qty if material.reference_snapshot == "HU212" else 0

        return sum / 2

    return 0.0


def estimate_galvanized_connectornail12(dmo_materials: List[MaterialOrderSpecItem] | None) -> float:
    if dmo_materials:
        E = get_qty_by_reference(dmo_materials, "461938")
        F = get_qty_by_reference(dmo_materials, "LSCZ")

        return (E * 7) + (F * 24)

    return 0.0


def estimate_galvanized_connectornail3(dmo_materials: List[MaterialOrderSpecItem] | None) -> float:
    if dmo_materials:
        A = get_qty_by_reference(dmo_materials, "LUS26Z")
        B = get_qty_by_reference(dmo_materials, "LUS28Z")
        C = get_qty_by_reference(dmo_materials, "LUS210Z")
        D = get_qty_by_reference(dmo_materials, "HU212")
        N = get_qty_by_reference(dmo_materials, "LUS26-2Z")
        O = get_qty_by_reference(dmo_materials, "LUS28-2Z")
        P = get_qty_by_reference(dmo_materials, "LUS210-2Z")
        Q = get_qty_by_reference(dmo_materials, "HU212-2")
        R = get_qty_by_reference(dmo_materials, "L50Z")
        S = get_qty_by_reference(dmo_materials, "L70Z")
        T = get_qty_by_reference(dmo_materials, "L90Z")

        return (A * 8) + (B * 10) + (C * 12) + (D * 16) + (R * 6) + (S * 8) + (T * 10) + (N * 8) + (O * 10) + (P * 12) + (Q * 16)

    return 0.0


def estimate_galvanized_connectorscrew(dmo_materials: List[MaterialOrderSpecItem] | None) -> float:
    if dmo_materials:
        I = get_qty_by_reference(dmo_materials, "ABA66Z")
        J = get_qty_by_reference(dmo_materials, "ABW44Z")
        L = get_qty_by_reference(dmo_materials, "BCS2-2/4Z")
        M = get_qty_by_reference(dmo_materials, "BCS2-3/6Z")

        return ((I * 8) + (J * 8) + (L * 12) + (M * 16)) / 100

    return 0.0

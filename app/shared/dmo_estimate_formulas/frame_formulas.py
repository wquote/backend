import math
from typing import List

from app.decking_quote.decking_quote_model import Area, Layout, QtySize, Stair


def estimate_frame_material(layout: Layout | None, size: str = "") -> float:
    main_areas: float = 0.0
    landing_areas: float = 0.0
    stair: float = 0.0

    if layout:
        main_areas = estimate_areas(layout.main_areas, size)
        landing_areas = estimate_areas(layout.lading_areas, size)
        stair = estimate_stair(layout.stairs, size)

    return main_areas + landing_areas + stair


def estimate_areas(areas: List[Area] | None, size: str = "") -> float:
    if not areas:
        return 0.0

    joist: float = 0.0
    beam_grade: float = 0.0
    wphi: float = 0.0
    support_post: float = 0.0

    for area in areas:
        joist += estimate_joist(area.ledger_board, size)  # joist
        beam_grade += estimate_beam(area.beam_grade, size)
        wphi += estimate_deck_grade(area.width, area.deck_grade, size) * phi(area.depth)
        support_post += estimate_support_post(area.height, area.support_post_grade, size)

    return joist + beam_grade + wphi + support_post


def estimate_stair(stairs: List[Stair] | None, size: str = "") -> float:
    if not stairs:
        return 0.0

    beam_grade: float = 0.0
    stringer: float = 0.0
    support_post_grade: float = 0.0

    for stair in stairs:
        beam_grade += estimate_beam(stair.beam_grade, size)
        stringer += estimate_stair_stringer(stair, size)
        support_post_grade += estimate_stair_support_post_grade(stair, size)

    return beam_grade + stringer + support_post_grade


def estimate_joist(ledger_board: QtySize | None, size: str = "") -> float:
    if ledger_board is None or ledger_board.qty is None or ledger_board.size != size:
        return 0.0

    return ledger_board.qty


def estimate_beam(beam_grade: QtySize | None, size: str = "") -> float:
    if not beam_grade or not beam_grade.qty or not beam_grade.size or not size in beam_grade.size:
        return 0.0

    factor: int = 0
    if "double" in beam_grade.size:
        factor = 2

    if "triple" in beam_grade.size:
        factor = 3

    return factor * beam_grade.qty


def estimate_deck_grade(width: float | None, deck_grade: str | None, size: str = "") -> float:
    if not width or not deck_grade or deck_grade != size:
        return 0.0

    return math.ceil(width * 0.75 + 5)


def phi(value: float | None) -> float:
    if not value:
        return 0

    if value > 24:
        return value
    elif value > 18:
        return 24
    elif value > 16:
        return 20
    elif value > 14:
        return 16
    elif value > 12:
        return 14
    elif value > 10:
        return 12
    elif value > 8:
        return 10
    elif value > 6:
        return 8
    elif value > 5:
        return 6
    elif value > 4:
        return 5
    else:
        return 4


def estimate_support_post(height: float | None, support_post_grade: QtySize | None, size: str = "") -> float:
    if not height or not support_post_grade or not support_post_grade.qty or support_post_grade.size != size:
        return 0.0

    return height * support_post_grade.qty


def estimate_stair_stringer(stair: Stair | None, size: str = "") -> float:
    if not stair or not stair.riser or not stair.width or not size or size != "2x12":
        return 0.0

    total_riser = stair.riser
    riser = math.ceil(total_riser * 12 / 7.5)
    treads = riser - 1

    stringer_length = math.ceil(((treads * 10 / 12) ** 2 + (total_riser) ** 2) ** 0.5)
    stringer_length_phi = phi(stringer_length)
    return stringer_length_phi * math.ceil(stair.width + 1)
    # return math.ceil(stair.riser * 12 / 7 - 1) * math.ceil(stair.width + 1)


def estimate_stair_support_post_grade(stair: Stair | None, size: str = "") -> float:
    if not stair or not stair.riser or not stair.beam_grade or stair.beam_grade.size != size:
        return 0.0

    return stair.riser

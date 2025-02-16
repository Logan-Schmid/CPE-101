
def poly_add2(poly1: list[float], poly2: list[float]) -> list[float]:
    """
    Takes in two polynomials of degree two and returns the polynomial sum
    :param poly1:
    :param poly2:
    :return:
    """
    poly_sum: list[float] = []

    for i in range(len(poly1) if len(poly1) >= len(poly2) else len(poly2)):
        if len(poly1) >= (i + 1) and len(poly2) >= (i + 1):
            poly_sum.append(poly1[i] + poly2[i])
        elif len(poly1) >= (i + 1) and not len(poly2) >= (i + 1):
            poly_sum.append(poly1[i])
        elif not len(poly1) >= (i + 1) and len(poly2) >= (i + 1):
            poly_sum.append(poly2[i])

    return poly_sum


def poly_mult2(poly1: list[float], poly2: list[float]) -> list[float]:
    poly_mult: list[float] = []

    highest_order: int = (len(poly1)-1) + (len(poly2)-1)
    for i in range(highest_order+1):
        poly_mult.append(0)

    for poly1_exp, poly1_coeff in enumerate(poly1):
        for poly2_exp, poly2_coeff in enumerate(poly2):
            combined_order: int = poly1_exp + poly2_exp
            poly_mult[combined_order] += poly1_coeff * poly2_coeff

    return poly_mult
def top_three(scores):
    return sorted(scores)[:3]


def any_expensive(products):
    for product in products:
        if product["price"] > 100:
            return True
        else:
            return False

def bestiary_page(creatures, first_letter):
    return [cr for cr in creatures if cr.lower().startswith(first_letter.lower())]

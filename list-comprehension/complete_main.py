def bestiary_page(creatures, first_letter):
    lower_initial = first_letter.lower()
    filtered_creatures = [ cr for cr in creatures if cr.lower().startswith(lower_initial) ]
    return filtered_creatures

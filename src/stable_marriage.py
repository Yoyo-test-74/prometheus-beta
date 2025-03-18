def stable_marriage(men_preferences, women_preferences):
    """
    Implement the Gale-Shapley algorithm for the Stable Marriage Problem.
    
    Args:
    men_preferences (list of list): A list where each inner list represents 
        the preferences of a man, ordered from most to least preferred.
    women_preferences (list of list): A list where each inner list represents 
        the preferences of a woman, ordered from most to least preferred.
    
    Returns:
    dict: A stable matching where keys are men and values are their matched women.
    
    Raises:
    ValueError: If the input lists are not of equal length or preferences are invalid.
    """
    # Input validation
    if not men_preferences or not women_preferences:
        raise ValueError("Preferences lists cannot be empty")
    
    n = len(men_preferences)
    if len(women_preferences) != n:
        raise ValueError("Men and women preference lists must be of equal length")
    
    # Validate preference lists (adjusted to be more flexible)
    for prefs in men_preferences + women_preferences:
        if len(set(prefs)) != len(prefs) or \
           any(not (0 <= p < n) for p in prefs):
            raise ValueError("Invalid preference list: must contain unique integers from 0 to n-1")
    
    # Initialize data structures
    women_partners = [None] * n  # Current partner for each woman
    men_partners = [None] * n  # Current partner for each man
    men_next_proposal = [0] * n  # Next woman to propose to for each man
    
    # Rank of each woman for each man (to quickly check preference)
    women_rank = [None] * n
    for m in range(n):
        women_rank[m] = {w: rank for rank, w in enumerate(men_preferences[m])}
    
    # Rank of each man for each woman (to quickly check preference)
    men_rank = [None] * n
    for w in range(n):
        men_rank[w] = {m: rank for rank, m in enumerate(women_preferences[w])}
    
    # Matching algorithm
    while None in men_partners:
        # Find a free man
        free_man = men_partners.index(None)
        
        # Get the next woman he wants to propose to
        woman = men_preferences[free_man][men_next_proposal[free_man]]
        men_next_proposal[free_man] += 1
        
        # If woman is free, match her with the man
        if women_partners[woman] is None:
            women_partners[woman] = free_man
            men_partners[free_man] = woman
        else:
            # Woman is already matched, check if she prefers new man
            current_partner = women_partners[woman]
            
            # Compare preferences
            if men_rank[woman][free_man] < men_rank[woman][current_partner]:
                # Woman prefers new man
                men_partners[current_partner] = None
                women_partners[woman] = free_man
                men_partners[free_man] = woman
    
    # Convert to dictionary for return
    return {m: women_partners[m] for m in range(n)}
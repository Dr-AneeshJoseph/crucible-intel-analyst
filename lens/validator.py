import math
from datetime import datetime

class EvidenceValidator:
    """
    Implements Loop 1.5: Weighted Evidence + Time Decay.
    """
    
    # Base Weights
    TIER_WEIGHTS = {
        "T1": 1.0,  # Physical Law / Peer Review
        "T2": 0.8,  # Standards
        "T3": 0.5,  # Single Study
        "T4": 0.2   # Opinion
    }

    def calculate_score(self, tier: str, year: int):
        """
        Score = Base_Weight * Decay_Factor
        Decay: Loses 5% value per year (Exponential).
        """
        current_year = datetime.now().year
        age = max(0, current_year - year)
        
        base = self.TIER_WEIGHTS.get(tier, 0.1)
        
        # Exponential Decay formula: N(t) = N0 * e^(-lambda*t)
        # Lambda = 0.05 (5% decay per year)
        decay_factor = math.exp(-0.05 * age)
        
        final_score = base * decay_factor
        return round(final_score, 3)

    def annihilate_weak_claims(self, claims: list):
        """
        The Annihilation Loop: Filters out low-quality claims.
        """
        scored_claims = []
        for c in claims:
            score = self.calculate_score(c['source_type'], c['year'])
            c['truth_score'] = score
            scored_claims.append(c)

        # Sort by score (Highest first)
        scored_claims.sort(key=lambda x: x['truth_score'], reverse=True)

        if not scored_claims:
            return []

        # ANNIHILATION THRESHOLD:
        # If the best claim has score 0.9, ignore anything below 0.2 (Gap > 4x)
        top_score = scored_claims[0]['truth_score']
        threshold = top_score * 0.25 # Keep claims within 25% relative strength
        
        # Strict Filter
        survivors = [c for c in scored_claims if c['truth_score'] >= threshold]
        
        return survivors
      

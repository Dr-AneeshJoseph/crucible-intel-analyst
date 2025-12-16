import os
import json
from .lens.validator import EvidenceValidator

class CrucibleAnalyst:
    def __init__(self):
        self.validator = EvidenceValidator()
        
        # Load Prompt
        # (Using safe path joining as discussed)
        prompt_path = os.path.join(os.path.dirname(__file__), 'prompts', 'evidence_kernel.md')
        with open(prompt_path, 'r') as f:
            self.system_prompt = f.read()

    def process_intel(self, raw_llm_json_string: str):
        """
        Takes the LLM's raw JSON extraction, validates it, and returns the Truth.
        """
        try:
            # 1. Parse LLM Output
            # In a real app, you'd use a regex or strict json parser here
            claims = json.loads(raw_llm_json_string)
            
            # 2. Run The Crucible (Math)
            survivors = self.validator.annihilate_weak_claims(claims)
            
            return {
                "status": "ANALYZED",
                "total_claims": len(claims),
                "surviving_claims": len(survivors),
                "report": survivors
            }
        except Exception as e:
            return {"status": "ERROR", "msg": str(e)}

    def construct_prompt(self, user_text: str):
        return f"{self.system_prompt}\n\nINPUT_TEXT:\n{user_text}"
      

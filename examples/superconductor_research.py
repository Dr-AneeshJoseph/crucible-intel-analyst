from crucible.analyst import CrucibleAnalyst

# Scenario: The LK-99 Superconductor debate (Scientific Claim Verification)
mock_llm_output = """
[
  {
    "claim": "Material exhibits zero resistance at room temperature.",
    "source_type": "T3", 
    "year": 2023,
    "content": "Pre-print paper by original authors (Not peer reviewed yet)."
  },
  {
    "claim": "Material is likely a ferromagnet, not a superconductor.",
    "source_type": "T1",
    "year": 2024,
    "content": "Nature Magazine Peer-Reviewed Replication Study."
  },
  {
    "claim": "I made a floating rock in my garage!",
    "source_type": "T4",
    "year": 2023,
    "content": "Viral video on social media."
  }
]
"""

analyst = CrucibleAnalyst()
result = analyst.process_intel(mock_llm_output)

# The T1 Peer-Review (2024) should annihilate the T3 Pre-print (2023) and T4 Video.
print(f"--- TRUTH ENGINE REPORT ---")
for item in result['report']:
    print(f"[{item['truth_score']}] {item['claim']}")
  

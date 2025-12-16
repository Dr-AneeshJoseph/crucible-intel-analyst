from crucible.analyst import CrucibleAnalyst

# MOCK DATA: Represents what the LLM *extracted* from a messy internet search
# Imagine the LLM read a blog and a medical journal.
mock_llm_output = """
[
  {
    "claim": "Vaccine X causes magnetism.",
    "source_type": "T4",
    "year": 2021,
    "content": "Blog post by User123."
  },
  {
    "claim": "Vaccine X is safe and effective.",
    "source_type": "T1",
    "year": 2024,
    "content": "CDC Meta-Analysis of 10 million patients."
  },
  {
    "claim": "Vaccine X has mild side effects.",
    "source_type": "T3",
    "year": 2015,
    "content": "Single study on 50 people."
  }
]
"""

analyst = CrucibleAnalyst()

# Run the Crucible
result = analyst.process_intel(mock_llm_output)

print(f"--- CRUCIBLE REPORT ---")
print(f"Input Claims: {result['total_claims']}")
print(f"Survivors: {result['surviving_claims']}")
print("\n[SURVIVING FACTS]")
for item in result['report']:
    print(f"[{item['truth_score']}] {item['claim']} (Source: {item['source_type']})")

# EXPECTED OUTPUT:
# T1 (Score ~1.0) survives.
# T3 (Score ~0.3 due to age decay) might survive depending on threshold.
# T4 (Score ~0.2) is ANNIHILATED because it is too weak compared to T1.


#!/usr/bin/env python3
"""
Basic usage example for Callosum Personality DSL
"""

from callosum_dsl import Callosum, PersonalityAI, PERSONALITY_TEMPLATES


def main():
    print("🎯 Callosum DSL - Basic Usage Example")
    print("=" * 40)
    
    # Create a compiler instance
    callosum = Callosum()
    
    # Example 1: Use a ready-made template
    print("\n1️⃣ Using a Ready-Made Template")
    dsl = PERSONALITY_TEMPLATES["helpful_assistant"]
    personality = callosum.to_json(dsl)
    
    print(f"Name: {personality['name']}")
    print(f"Traits: {len(personality['traits'])}")
    for trait in personality['traits']:
        print(f"  • {trait['name']}: {trait['strength']:.2f}")
    
    # Example 2: Create a custom personality
    print("\n2️⃣ Creating a Custom Personality")
    custom_dsl = '''personality "Python Expert" {
  traits {
    technical_knowledge: 0.95;
    helpfulness: 0.90;
    patience: 0.85;
    creativity: 0.75;
  }
  
  knowledge {
    domain("python") {
      language_features: expert;
      libraries: advanced;
      debugging: expert;
    }
    
    domain("teaching") {
      explanation: advanced;
      mentoring: intermediate;
    }
  }
  
  behaviors {
    when technical_knowledge > 0.9 -> prefer("code_examples");
    when helpfulness > 0.8 -> seek("complete_solutions");
  }
  
  evolution {
    if learns("user_style") then trait("patience") += 0.05;
  }
}'''
    
    custom_personality = callosum.to_json(custom_dsl)
    print(f"Created: {custom_personality['name']}")
    print(f"Knowledge domains: {[d['name'] for d in custom_personality['knowledge']]}")
    
    # Example 3: Generate system prompt for AI
    print("\n3️⃣ Generating System Prompt")
    system_prompt = callosum.to_prompt(custom_dsl)
    print("System prompt preview:")
    print(system_prompt[:200] + "..." if len(system_prompt) > 200 else system_prompt)
    
    # Example 4: All compilation targets
    print("\n4️⃣ All Compilation Targets")
    formats = ["json", "prompt", "lua", "sql", "cypher"]
    
    for fmt in formats:
        output = callosum.compile(custom_dsl, fmt)
        print(f"✅ {fmt.upper()}: {len(output)} characters")
    
    # Example 5: AI Integration (commented out - requires API key)
    print("\n5️⃣ AI Integration Example (commented out)")
    print("""
# Uncomment and add your API key to try AI integration:

# ai = PersonalityAI(
#     personality_dsl=custom_dsl,
#     api_key="your-openai-key-here",
#     provider="openai"
# )
# 
# response = ai.chat("Help me understand Python decorators")
# print(f"AI Response: {response}")
# 
# info = ai.get_personality_summary()
# print(f"Dominant trait: {info['dominant_trait']}")
""")
    
    print("\n🎉 Basic usage example complete!")
    print("\n💡 Next steps:")
    print("   • Try modifying the personality DSL")
    print("   • Add your AI API key for chat integration")
    print("   • Check out README_PYTHON.md for more examples")


if __name__ == "__main__":
    main()

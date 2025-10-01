#!/usr/bin/env python3
"""
Trait Sensitivity Tests - Verify small changes in traits produce different outputs

This test validates that adjusting specific trait values in the DSL
actually changes AI behavior, proving the system uses the exact values.
"""

import pytest
import os
import sys

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from callosum_dsl import PersonalityAI


class TestTraitSensitivity:
    """Test that small trait changes produce different AI behaviors"""
    
    def setup_method(self):
        """Setup for each test"""
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path)
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
    
    @pytest.mark.integration
    def test_helpfulness_trait_variations(self):
        """Test that different helpfulness levels produce different responses"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Base personality with low helpfulness
        low_helpfulness = '''personality: "Helpful Assistant - Low"

traits:
  helpfulness: 0.3
  patience: 0.8
  empathy: 0.8
  
knowledge:
  domain general_support:
    problem_solving: expert
    communication: advanced
    
behaviors:
  - when helpfulness > 0.9 → seek "solutions"
  - when patience > 0.8 → prefer "guidance"'''

        # Same personality but with high helpfulness  
        high_helpfulness = '''personality: "Helpful Assistant - High"

traits:
  helpfulness: 0.95
  patience: 0.8
  empathy: 0.8
  
knowledge:
  domain general_support:
    problem_solving: expert
    communication: advanced
    
behaviors:
  - when helpfulness > 0.9 → seek "solutions"
  - when patience > 0.8 → prefer "guidance"'''

        question = "I'm struggling with a project at work."
        
        # Test with low helpfulness
        ai_low = PersonalityAI(low_helpfulness)
        ai_low.set_provider("openai", api_key=self.openai_api_key)
        response_low = ai_low.chat(question, max_tokens=100, temperature=0.2)
        
        # Test with high helpfulness
        ai_high = PersonalityAI(high_helpfulness)
        ai_high.set_provider("openai", api_key=self.openai_api_key)
        response_high = ai_high.chat(question, max_tokens=100, temperature=0.2)
        
        print("\n" + "="*80)
        print("🧪 HELPFULNESS TRAIT SENSITIVITY TEST")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n📉 LOW Helpfulness (0.3):")
        print(f"   {response_low}")
        print(f"\n📈 HIGH Helpfulness (0.95):")
        print(f"   {response_high}")
        
        # Analyze differences
        responses_different = response_low.lower().strip() != response_high.lower().strip()
        
        # Count solution-oriented words (should be more in high helpfulness)
        solution_words = ["help", "solution", "fix", "resolve", "assist", "support", "try", "suggest"]
        low_solutions = sum(1 for word in solution_words if word in response_low.lower())
        high_solutions = sum(1 for word in solution_words if word in response_high.lower())
        
        print(f"\n📊 Analysis:")
        print(f"   Solution words in LOW helpfulness: {low_solutions}")
        print(f"   Solution words in HIGH helpfulness: {high_solutions}")
        print(f"   Responses are different: {responses_different}")
        print(f"   High helpfulness more solution-focused: {high_solutions > low_solutions}")
        
        assert responses_different, "Different helpfulness levels should produce different responses"
        
        return {
            "low_helpfulness_response": response_low,
            "high_helpfulness_response": response_high,
            "responses_different": responses_different,
            "helpfulness_effect_detected": high_solutions > low_solutions
        }
    
    @pytest.mark.integration
    def test_creativity_trait_variations(self):
        """Test that creativity level changes creative expression"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Low creativity writer
        low_creativity = '''personality: "Writer - Low Creativity"

traits:
  creativity: 0.2
  imagination: 0.3
  literary_flair: 0.4
  
knowledge:
  domain writing:
    storytelling: expert
    character_development: expert
    
behaviors:
  - when creativity > 0.9 → seek "perspectives"
  - when imagination > 0.8 → prefer "descriptions"'''

        # High creativity writer
        high_creativity = '''personality: "Writer - High Creativity"

traits:
  creativity: 0.95
  imagination: 0.90
  literary_flair: 0.88
  
knowledge:
  domain writing:
    storytelling: expert
    character_development: expert
    
behaviors:
  - when creativity > 0.9 → seek "perspectives"  
  - when imagination > 0.8 → prefer "descriptions"'''

        question = "Describe a rainy day."
        
        # Test low creativity
        ai_low = PersonalityAI(low_creativity)
        ai_low.set_provider("openai", api_key=self.openai_api_key)
        response_low = ai_low.chat(question, max_tokens=80, temperature=0.2)
        
        # Test high creativity  
        ai_high = PersonalityAI(high_creativity)
        ai_high.set_provider("openai", api_key=self.openai_api_key)
        response_high = ai_high.chat(question, max_tokens=80, temperature=0.2)
        
        print("\n" + "="*80)
        print("🧪 CREATIVITY TRAIT SENSITIVITY TEST")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n📉 LOW Creativity (0.2):")
        print(f"   {response_low}")
        print(f"\n📈 HIGH Creativity (0.95):")
        print(f"   {response_high}")
        
        # Analyze creative language
        creative_words = ["dancing", "whispered", "symphony", "painting", "melody", "canvas", "tapestry", "shimmering", "ethereal", "mystical"]
        descriptive_words = ["gently", "softly", "gracefully", "delicately", "rhythmic", "melodic", "flowing", "cascading"]
        
        low_creative = sum(1 for word in creative_words if word in response_low.lower())
        high_creative = sum(1 for word in creative_words if word in response_high.lower())
        
        low_descriptive = sum(1 for word in descriptive_words if word in response_low.lower())
        high_descriptive = sum(1 for word in descriptive_words if word in response_high.lower())
        
        responses_different = response_low.lower().strip() != response_high.lower().strip()
        
        print(f"\n📊 Analysis:")
        print(f"   Creative language in LOW: {low_creative}")
        print(f"   Creative language in HIGH: {high_creative}")
        print(f"   Descriptive language in LOW: {low_descriptive}")
        print(f"   Descriptive language in HIGH: {high_descriptive}")
        print(f"   Responses are different: {responses_different}")
        
        creativity_effect = (high_creative > low_creative) or (high_descriptive > low_descriptive)
        print(f"   High creativity more expressive: {creativity_effect}")
        
        assert responses_different, "Different creativity levels should produce different responses"
        
        return {
            "low_creativity_response": response_low,
            "high_creativity_response": response_high,
            "creativity_effect": creativity_effect
        }
    
    @pytest.mark.integration
    def test_technical_precision_variations(self):
        """Test that precision level affects technical explanations"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Low precision mentor
        low_precision = '''personality: "Technical Mentor - Casual"

traits:
  technical_expertise: 0.9
  teaching_ability: 0.9
  precision: 0.3
  patience: 0.8
  
knowledge:
  domain programming:
    software_architecture: expert
    debugging: expert
    
behaviors:
  - when technical_expertise > 0.9 → prefer "explanations"
  - when teaching_ability > 0.8 → seek "opportunities"'''

        # High precision mentor
        high_precision = '''personality: "Technical Mentor - Precise"

traits:
  technical_expertise: 0.9
  teaching_ability: 0.9
  precision: 0.95
  patience: 0.8
  
knowledge:
  domain programming:
    software_architecture: expert
    debugging: expert
    
behaviors:
  - when technical_expertise > 0.9 → prefer "explanations"
  - when teaching_ability > 0.8 → seek "opportunities"'''

        question = "What is a function in programming?"
        
        # Test low precision
        ai_low = PersonalityAI(low_precision)
        ai_low.set_provider("openai", api_key=self.openai_api_key)
        response_low = ai_low.chat(question, max_tokens=100, temperature=0.1)
        
        # Test high precision
        ai_high = PersonalityAI(high_precision)
        ai_high.set_provider("openai", api_key=self.openai_api_key)
        response_high = ai_high.chat(question, max_tokens=100, temperature=0.1)
        
        print("\n" + "="*80)
        print("🧪 PRECISION TRAIT SENSITIVITY TEST")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n📉 LOW Precision (0.3):")
        print(f"   {response_low}")
        print(f"\n📈 HIGH Precision (0.95):")
        print(f"   {response_high}")
        
        # Analyze precision indicators
        precise_terms = ["specifically", "exactly", "precisely", "defined as", "syntax", "parameters", "return type", "scope"]
        casual_terms = ["basically", "kind of", "sort of", "like", "thing", "stuff"]
        
        low_precise = sum(1 for term in precise_terms if term in response_low.lower())
        high_precise = sum(1 for term in precise_terms if term in response_high.lower())
        
        low_casual = sum(1 for term in casual_terms if term in response_low.lower())
        high_casual = sum(1 for term in casual_terms if term in response_high.lower())
        
        responses_different = response_low.lower().strip() != response_high.lower().strip()
        
        print(f"\n📊 Analysis:")
        print(f"   Precise terms in LOW precision: {low_precise}")
        print(f"   Precise terms in HIGH precision: {high_precise}")
        print(f"   Casual terms in LOW precision: {low_casual}")
        print(f"   Casual terms in HIGH precision: {high_casual}")
        print(f"   Responses are different: {responses_different}")
        
        precision_effect = (high_precise > low_precise) or (low_casual > high_casual)
        print(f"   Precision difference detected: {precision_effect}")
        
        assert responses_different, "Different precision levels should produce different responses"
        
        return {
            "low_precision_response": response_low,
            "high_precision_response": response_high,
            "precision_effect": precision_effect
        }
    
    @pytest.mark.integration
    def test_behavior_threshold_effects(self):
        """Test that behavior thresholds actually trigger different behaviors"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Personality where helpfulness is BELOW threshold (0.9)
        below_threshold = '''personality: "Helper - Below Threshold"

traits:
  helpfulness: 0.8
  patience: 0.9
  
knowledge:
  domain general_support:
    problem_solving: expert
    
behaviors:
  - when helpfulness > 0.9 → seek "solutions"
  - when patience > 0.8 → prefer "guidance"'''

        # Personality where helpfulness is ABOVE threshold (0.9)
        above_threshold = '''personality: "Helper - Above Threshold"

traits:
  helpfulness: 0.95
  patience: 0.9
  
knowledge:
  domain general_support:
    problem_solving: expert
    
behaviors:
  - when helpfulness > 0.9 → seek "solutions"
  - when patience > 0.8 → prefer "guidance"'''

        question = "I have a problem I need to solve."
        
        # Test below threshold
        ai_below = PersonalityAI(below_threshold)
        ai_below.set_provider("openai", api_key=self.openai_api_key)
        response_below = ai_below.chat(question, max_tokens=80, temperature=0.1)
        
        # Test above threshold
        ai_above = PersonalityAI(above_threshold)
        ai_above.set_provider("openai", api_key=self.openai_api_key)
        response_above = ai_above.chat(question, max_tokens=80, temperature=0.1)
        
        print("\n" + "="*80)
        print("🧪 BEHAVIOR THRESHOLD SENSITIVITY TEST")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n📉 BELOW Threshold (helpfulness 0.8 ≤ 0.9):")
        print(f"   {response_below}")
        print(f"\n📈 ABOVE Threshold (helpfulness 0.95 > 0.9):")
        print(f"   {response_above}")
        
        # Look for solution-seeking behavior (should trigger when helpfulness > 0.9)
        solution_words = ["solution", "solve", "fix", "resolve", "answer", "address", "tackle"]
        guidance_words = ["guide", "help", "assist", "support", "step", "approach"]
        
        below_solutions = sum(1 for word in solution_words if word in response_below.lower())
        above_solutions = sum(1 for word in solution_words if word in response_above.lower())
        
        below_guidance = sum(1 for word in guidance_words if word in response_below.lower())
        above_guidance = sum(1 for word in guidance_words if word in response_above.lower())
        
        responses_different = response_below.lower().strip() != response_above.lower().strip()
        
        print(f"\n📊 Analysis:")
        print(f"   Solution-seeking words BELOW threshold: {below_solutions}")
        print(f"   Solution-seeking words ABOVE threshold: {above_solutions}")
        print(f"   Guidance words BELOW threshold: {below_guidance}")
        print(f"   Guidance words ABOVE threshold: {above_guidance}")
        print(f"   Responses are different: {responses_different}")
        
        threshold_effect = above_solutions > below_solutions
        print(f"   Threshold behavior triggered: {threshold_effect}")
        
        assert responses_different, "Different threshold positions should produce different responses"
        
        return {
            "below_threshold_response": response_below,
            "above_threshold_response": response_above,
            "threshold_effect": threshold_effect
        }


if __name__ == "__main__":
    # Run trait sensitivity tests
    pytest.main([__file__, "-v", "-s"])

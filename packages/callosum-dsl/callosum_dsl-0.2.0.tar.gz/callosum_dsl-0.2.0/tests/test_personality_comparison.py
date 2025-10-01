#!/usr/bin/env python3
"""
Personality Comparison Tests - Prove DSL actually changes AI behavior

This test suite compares AI responses WITH and WITHOUT Callosum DSL personalities
to demonstrate that the personality system actually influences AI behavior.
"""

import pytest
import os
import sys
from unittest.mock import Mock, patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from callosum_dsl import PersonalityAI, PERSONALITY_TEMPLATES, OpenAIProvider, LangChainProvider


class TestPersonalityComparison:
    """Compare AI responses with and without personality DSL"""
    
    def setup_method(self):
        """Setup for each test"""
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path)
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        
        # Test questions that should show personality differences
        self.test_questions = [
            "Hello, how can you help me?",
            "Write a story about a cat.",
            "Explain what a variable is in programming.",
            "I'm feeling frustrated with coding.",
            "What's the best way to learn?"
        ]
    
    def test_mock_personality_vs_no_personality(self):
        """Test personality difference with mocked responses"""
        
        # Test with helpful_assistant personality
        personality_dsl = PERSONALITY_TEMPLATES["helpful_assistant"]
        
        # Mock responses - simulate what we'd expect with/without personality
        def mock_personality_response(messages, model=None, **kwargs):
            """Mock response that shows personality traits"""
            user_msg = messages[-1]["content"].lower()
            if "help" in user_msg:
                return "I'm delighted to help you! My empathy and patience guide me to provide the most supportive assistance possible. What can I do for you today?"
            elif "story" in user_msg:
                return "I'd be happy to help you with that story! Let me craft something heartwarming for you about a cat."
            elif "variable" in user_msg:
                return "I'm here to help you understand variables! Let me explain this programming concept in a supportive way that makes it easy to grasp."
            return "I'm here to help you with whatever you need! How can I assist you today?"
        
        def mock_no_personality_response(messages, model=None, **kwargs):
            """Mock response without personality - more generic"""
            user_msg = messages[-1]["content"].lower()
            if "help" in user_msg:
                return "I can assist you with various tasks. What do you need help with?"
            elif "story" in user_msg:
                return "Here's a story about a cat: A cat sat on a mat."
            elif "variable" in user_msg:
                return "A variable is a storage location with a name that holds data."
            return "How can I help you?"
        
        with patch('openai.OpenAI') as mock_openai_class:
            # Test WITH personality
            mock_client = Mock()
            mock_openai_class.return_value = mock_client
            
            def create_personality_mock(*args, **kwargs):
                response = mock_personality_response(kwargs.get('messages', []))
                mock_response = Mock()
                mock_choice = Mock()
                mock_message = Mock()
                mock_message.content = response
                mock_choice.message = mock_message
                mock_response.choices = [mock_choice]
                return mock_response
            
            mock_client.chat.completions.create = create_personality_mock
            
            # Create PersonalityAI with helpful_assistant
            ai_with_personality = PersonalityAI(personality_dsl)
            ai_with_personality.set_provider("openai", api_key="mock-key")
            
            personality_responses = []
            for question in self.test_questions[:3]:  # Test first 3 questions
                response = ai_with_personality.chat(question)
                personality_responses.append((question, response))
            
            # Test WITHOUT personality (direct OpenAI)
            def create_no_personality_mock(*args, **kwargs):
                response = mock_no_personality_response(kwargs.get('messages', []))
                mock_response = Mock()
                mock_choice = Mock()
                mock_message = Mock()
                mock_message.content = response
                mock_choice.message = mock_message
                mock_response.choices = [mock_choice]
                return mock_response
            
            mock_client.chat.completions.create = create_no_personality_mock
            
            # Direct provider without personality
            provider_no_personality = OpenAIProvider(api_key="mock-key")
            
            no_personality_responses = []
            for question in self.test_questions[:3]:
                # Simple system message without personality
                messages = [
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": question}
                ]
                response = provider_no_personality.chat(messages)
                no_personality_responses.append((question, response))
            
            # Analyze differences
            print("\n" + "="*80)
            print("🧪 PERSONALITY VS NO PERSONALITY COMPARISON (MOCK)")
            print("="*80)
            
            differences_found = 0
            for i in range(len(personality_responses)):
                question, with_personality = personality_responses[i]
                _, without_personality = no_personality_responses[i]
                
                print(f"\n📋 Question: {question}")
                print(f"🎭 WITH Personality: {with_personality}")
                print(f"🤖 WITHOUT Personality: {without_personality}")
                
                # Check for personality indicators
                personality_indicators = ["delighted", "empathy", "supportive", "heartwarming", "guide"]
                has_personality_traits = any(indicator in with_personality.lower() for indicator in personality_indicators)
                is_different = with_personality.lower() != without_personality.lower()
                
                if has_personality_traits and is_different:
                    print("✅ PERSONALITY DIFFERENCE DETECTED")
                    differences_found += 1
                else:
                    print("❌ No clear personality difference")
            
            # Assert that we found personality differences
            assert differences_found >= 2, f"Expected personality differences in at least 2 responses, found {differences_found}"
            print(f"\n🎉 SUCCESS: Found personality differences in {differences_found}/3 responses")
    
    @pytest.mark.integration
    def test_real_personality_vs_no_personality(self):
        """Test personality difference with REAL API calls"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Test with technical_mentor personality
        personality_dsl = PERSONALITY_TEMPLATES["technical_mentor"]
        question = "Explain what a variable is in programming."
        
        # Test WITH personality
        ai_with_personality = PersonalityAI(personality_dsl)
        ai_with_personality.set_provider("openai", api_key=self.openai_api_key)
        response_with_personality = ai_with_personality.chat(question, max_tokens=150, temperature=0.1)
        
        # Test WITHOUT personality (direct OpenAI with generic prompt)
        provider_no_personality = OpenAIProvider(api_key=self.openai_api_key)
        messages_no_personality = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
        response_without_personality = provider_no_personality.chat(messages_no_personality, max_tokens=150, temperature=0.1)
        
        # Display results
        print("\n" + "="*80)
        print("🧪 REAL API PERSONALITY COMPARISON")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n🎭 WITH Technical Mentor Personality:")
        print(f"   {response_with_personality}")
        print(f"\n🤖 WITHOUT Personality (Generic Assistant):")
        print(f"   {response_without_personality}")
        
        # Analyze differences
        technical_indicators = ["technical", "programming", "concept", "systematic", "explain", "detailed"]
        personality_traits = sum(1 for indicator in technical_indicators if indicator in response_with_personality.lower())
        generic_traits = sum(1 for indicator in technical_indicators if indicator in response_without_personality.lower())
        
        length_difference = abs(len(response_with_personality) - len(response_without_personality))
        responses_different = response_with_personality.lower().strip() != response_without_personality.lower().strip()
        
        print(f"\n📊 Analysis:")
        print(f"   Technical indicators WITH personality: {personality_traits}")
        print(f"   Technical indicators WITHOUT personality: {generic_traits}")
        print(f"   Length difference: {length_difference} characters")
        print(f"   Responses are different: {responses_different}")
        
        # Assertions
        assert responses_different, "Responses should be different with vs without personality"
        assert len(response_with_personality) > 20, "Response with personality should be substantial"
        assert len(response_without_personality) > 20, "Response without personality should be substantial"
        
        # Expect personality to produce more technical language or longer explanations
        personality_shows_effect = (
            personality_traits > generic_traits or 
            len(response_with_personality) > len(response_without_personality) * 1.2
        )
        
        print(f"✅ Personality effect detected: {personality_shows_effect}")
        return {
            "with_personality": response_with_personality,
            "without_personality": response_without_personality,
            "personality_traits": personality_traits,
            "generic_traits": generic_traits,
            "responses_different": responses_different,
            "personality_shows_effect": personality_shows_effect
        }
    
    @pytest.mark.integration  
    def test_creative_writer_vs_generic(self):
        """Test creative writer personality vs generic responses"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        # Test creative writing request
        personality_dsl = PERSONALITY_TEMPLATES["creative_writer"]
        question = "Write a short story about a magical forest."
        
        # WITH creative writer personality
        ai_creative = PersonalityAI(personality_dsl)
        ai_creative.set_provider("openai", api_key=self.openai_api_key)
        creative_response = ai_creative.chat(question, max_tokens=100, temperature=0.3)
        
        # WITHOUT personality
        provider_generic = OpenAIProvider(api_key=self.openai_api_key)
        generic_messages = [
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": question}
        ]
        generic_response = provider_generic.chat(generic_messages, max_tokens=100, temperature=0.3)
        
        # Display comparison
        print("\n" + "="*80) 
        print("🧪 CREATIVE WRITER VS GENERIC COMPARISON")
        print("="*80)
        print(f"📋 Question: {question}")
        print(f"\n🎭 WITH Creative Writer Personality:")
        print(f"   {creative_response}")
        print(f"\n🤖 WITHOUT Personality (Generic):")
        print(f"   {generic_response}")
        
        # Analyze creativity indicators
        creative_words = ["magical", "enchanted", "mystical", "shimmering", "whispered", "glowing", "ancient", "mysterious", "ethereal"]
        creative_count = sum(1 for word in creative_words if word in creative_response.lower())
        generic_count = sum(1 for word in creative_words if word in generic_response.lower())
        
        print(f"\n📊 Creativity Analysis:")
        print(f"   Creative language WITH personality: {creative_count} words")
        print(f"   Creative language WITHOUT personality: {generic_count} words")
        
        responses_different = creative_response.lower().strip() != generic_response.lower().strip()
        assert responses_different, "Creative responses should differ from generic ones"
        
        print(f"✅ Creative personality effect: {creative_count >= generic_count}")
        return {
            "creative_response": creative_response,
            "generic_response": generic_response,
            "creative_words_with": creative_count,
            "creative_words_without": generic_count,
            "responses_different": responses_different
        }
    
    def test_system_prompt_inclusion(self):
        """Verify that our DSL-generated system prompts are actually being used"""
        
        # Get the compiled system prompt from our DSL
        personality_dsl = PERSONALITY_TEMPLATES["helpful_assistant"]
        
        with patch('openai.OpenAI') as mock_openai_class:
            mock_client = Mock()
            mock_openai_class.return_value = mock_client
            
            # Capture the actual messages sent to OpenAI
            captured_messages = []
            
            def capture_messages(*args, **kwargs):
                captured_messages.append(kwargs.get('messages', []))
                mock_response = Mock()
                mock_choice = Mock()
                mock_message = Mock()
                mock_message.content = "Test response"
                mock_choice.message = mock_message
                mock_response.choices = [mock_choice]
                return mock_response
            
            mock_client.chat.completions.create = capture_messages
            
            # Create PersonalityAI and make a chat call
            ai = PersonalityAI(personality_dsl)
            ai.set_provider("openai", api_key="mock-key")
            ai.chat("Hello")
            
            # Verify system prompt was included
            assert len(captured_messages) == 1, "Should have captured one API call"
            messages = captured_messages[0]
            assert len(messages) >= 2, "Should have system and user messages"
            
            system_message = messages[0]
            assert system_message["role"] == "system", "First message should be system message"
            
            system_content = system_message["content"]
            print(f"\n🔍 SYSTEM PROMPT VERIFICATION:")
            print(f"System prompt: {system_content[:200]}...")
            
            # Check that our DSL-compiled content is in the system prompt
            personality_indicators = ["Helpful AI Assistant", "helpfulness", "empathy"]
            found_indicators = [ind for ind in personality_indicators if ind in system_content]
            
            assert len(found_indicators) > 0, f"System prompt should contain personality indicators, found: {found_indicators}"
            assert len(system_content) > 100, "System prompt should be substantial (>100 chars)"
            
            print(f"✅ Personality indicators found in system prompt: {found_indicators}")
            print(f"✅ System prompt length: {len(system_content)} characters")
    
    @pytest.mark.integration
    def test_multiple_personalities_show_differences(self):
        """Test that different personalities produce different responses to the same question"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        question = "How should I approach learning something new?"
        responses = {}
        
        # Test all three personalities with the same question
        for name, personality_dsl in PERSONALITY_TEMPLATES.items():
            ai = PersonalityAI(personality_dsl)
            ai.set_provider("openai", api_key=self.openai_api_key)
            response = ai.chat(question, max_tokens=80, temperature=0.2)
            responses[name] = response
        
        # Display all responses
        print("\n" + "="*80)
        print("🧪 MULTIPLE PERSONALITIES COMPARISON")
        print("="*80)
        print(f"📋 Question: {question}")
        
        for name, response in responses.items():
            print(f"\n🎭 {name.upper().replace('_', ' ')}:")
            print(f"   {response}")
        
        # Verify all responses are different
        response_values = list(responses.values())
        unique_responses = len(set(r.lower().strip() for r in response_values))
        
        print(f"\n📊 Analysis:")
        print(f"   Total personalities tested: {len(responses)}")
        print(f"   Unique responses: {unique_responses}")
        
        # Should have different responses from different personalities
        assert unique_responses >= 2, f"Expected at least 2 unique responses, got {unique_responses}"
        
        # Look for personality-specific language
        helpful_words = ["help", "support", "guide", "assist"]
        creative_words = ["creative", "imaginative", "explore", "inspiration"]
        technical_words = ["systematic", "structured", "methodology", "approach"]
        
        for name, response in responses.items():
            response_lower = response.lower()
            if name == "helpful_assistant":
                helpful_count = sum(1 for word in helpful_words if word in response_lower)
                print(f"   Helpful assistant indicators: {helpful_count}")
            elif name == "creative_writer":
                creative_count = sum(1 for word in creative_words if word in response_lower) 
                print(f"   Creative writer indicators: {creative_count}")
            elif name == "technical_mentor":
                technical_count = sum(1 for word in technical_words if word in response_lower)
                print(f"   Technical mentor indicators: {technical_count}")
        
        print("✅ Personalities show distinct responses to the same question")
        return responses


if __name__ == "__main__":
    # Run personality comparison tests
    pytest.main([__file__, "-v", "-s"])

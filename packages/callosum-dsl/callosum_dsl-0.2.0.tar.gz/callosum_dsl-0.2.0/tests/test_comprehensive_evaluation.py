#!/usr/bin/env python3
"""
Comprehensive Evaluation Tests for Callosum DSL
Tests the package with real questions across different personalities and evaluates responses

This test suite actually uses the callosum_dsl package to run real queries against 
various personalities and domains, then evaluates the responses for quality and consistency.
"""

import pytest
import os
import sys
import json
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from unittest.mock import Mock, patch

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from callosum_dsl import PersonalityAI, PERSONALITY_TEMPLATES, CallosumError


class ResponseEvaluator:
    """Helper class to evaluate AI responses for quality and personality consistency"""
    
    @staticmethod
    def evaluate_response_quality(response: str, question: str, min_length: int = 10) -> Dict[str, Any]:
        """Evaluate basic response quality metrics"""
        if not isinstance(response, str):
            return {"valid": False, "error": "Response is not a string"}
        
        response = response.strip()
        if len(response) < min_length:
            return {"valid": False, "error": f"Response too short ({len(response)} chars)"}
        
        # Check for actual error patterns that indicate system failures
        error_patterns = [
            r"\bexception.*occurred\b", # exception occurred
            r"\bapi.*key.*invalid\b", # API key invalid
            r"\brate.*limit.*exceeded\b", # rate limit exceeded 
            r"\btimeout.*error\b", # timeout error
            r"\bconnection.*failed\b", # connection failed
            r"\binternal.*server.*error\b" # internal server error
        ]
        
        for pattern in error_patterns:
            if re.search(pattern, response.lower()):
                return {"valid": False, "error": f"Response contains error pattern: {pattern}"}
        
        return {
            "valid": True,
            "length": len(response),
            "word_count": len(response.split()),
            "has_punctuation": any(p in response for p in '.!?'),
            "is_complete_sentence": response.strip().endswith(('.', '!', '?'))
        }
    
    @staticmethod
    def evaluate_personality_consistency(response: str, personality_name: str, 
                                       expected_traits: List[str]) -> Dict[str, Any]:
        """Evaluate if response matches expected personality traits"""
        response_lower = response.lower()
        
        trait_indicators = {
            "helpful_assistant": [
                "help", "assist", "support", "guide", "service", "glad", "happy",
                "pleasure", "welcome", "here for you", "ready", "available"
            ],
            "creative_writer": [
                "imagine", "story", "creative", "artistic", "vision", "inspiration",
                "character", "narrative", "tale", "poetry", "literary", "brainstorm",
                "fantasy", "novel", "thrilled", "craft", "weave", "create", "world",
                "once upon a time", "exciting", "adventure", "magical"
            ],
            "technical_mentor": [
                "technical", "code", "programming", "software", "debug", "architecture",
                "best practice", "explain", "implement", "algorithm", "function",
                "concept", "specific", "designed", "block", "task", "language"
            ]
        }
        
        empathy_indicators = [
            "understand", "feel", "emotion", "concern", "care", "empathy",
            "patient", "gentle", "supportive"
        ]
        
        # Count trait indicators
        indicators = trait_indicators.get(personality_name, [])
        found_indicators = [ind for ind in indicators if ind in response_lower]
        
        # Check for empathy (common across personalities)
        found_empathy = [ind for ind in empathy_indicators if ind in response_lower]
        
        return {
            "personality_indicators_found": len(found_indicators),
            "total_personality_indicators": len(indicators),
            "personality_match_ratio": len(found_indicators) / max(len(indicators), 1),
            "empathy_indicators_found": len(found_empathy),
            "specific_indicators": found_indicators,
            "empathy_indicators": found_empathy
        }
    
    @staticmethod
    def evaluate_domain_relevance(response: str, expected_domain: str, question: str) -> Dict[str, Any]:
        """Evaluate if response is relevant to the expected knowledge domain"""
        response_lower = response.lower()
        question_lower = question.lower()
        
        domain_keywords = {
            "programming": ["code", "function", "variable", "class", "method", "algorithm", "debug"],
            "education": ["teach", "learn", "student", "lesson", "concept", "understand", "explain"],
            "writing": ["story", "character", "plot", "narrative", "write", "author", "book"],
            "general_support": ["help", "support", "assist", "solution", "answer", "problem"]
        }
        
        keywords = domain_keywords.get(expected_domain, [])
        found_keywords = [kw for kw in keywords if kw in response_lower or kw in question_lower]
        
        return {
            "domain": expected_domain,
            "relevant_keywords_found": len(found_keywords),
            "total_domain_keywords": len(keywords),
            "domain_relevance_ratio": len(found_keywords) / max(len(keywords), 1),
            "found_keywords": found_keywords
        }


class TestComprehensiveEvaluation:
    """Comprehensive evaluation tests for different personalities and providers"""
    
    def setup_method(self):
        """Setup for each test"""
        # Load environment variables from .env file in tests directory
        from dotenv import load_dotenv
        env_path = os.path.join(os.path.dirname(__file__), '.env')
        load_dotenv(env_path)
        
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.evaluator = ResponseEvaluator()
        
        # Find the DSL compiler path
        self.compiler_path = self._find_compiler_path()
        
        # Test questions designed to evaluate different aspects
        self.test_questions = {
            "general": [
                "Hello, how are you today?",
                "Can you help me with a problem?",
                "What's the weather like?",
                "Tell me about yourself in one sentence."
            ],
            "technical": [
                "Explain what a function is in programming.",
                "How do I debug a Python error?",
                "What are best practices for code review?",
                "What's the difference between a list and a dictionary?"
            ],
            "creative": [
                "Write a short story about a robot.",
                "Help me brainstorm ideas for a fantasy novel.",
                "Create a haiku about technology.",
                "Describe a magical forest in vivid detail."
            ],
            "educational": [
                "How do I learn a new programming language?",
                "What's the best way to study effectively?",
                "Explain this concept simply: recursion.",
                "Help me understand why this is difficult."
            ]
        }
        
        # Expected personality characteristics
        self.personality_expectations = {
            "helpful_assistant": {
                "traits": ["helpfulness", "patience", "empathy"],
                "domain": "general_support",
                "tone": "supportive"
            },
            "creative_writer": {
                "traits": ["creativity", "imagination", "literary_flair"],
                "domain": "writing", 
                "tone": "imaginative"
            },
            "technical_mentor": {
                "traits": ["technical_expertise", "teaching_ability", "precision"],
                "domain": "programming",
                "tone": "instructional"
            }
        }
    
    def _find_compiler_path(self) -> Optional[str]:
        """Find the DSL compiler binary path"""
        import os
        from pathlib import Path
        
        # Get the project root directory
        test_dir = Path(__file__).parent
        project_root = test_dir.parent.parent
        
        # Search paths relative to project root
        search_paths = [
            project_root / "core" / "_build" / "default" / "bin" / "main.exe",
            project_root / "core" / "_build" / "install" / "default" / "bin" / "dsl-parser",
            project_root / "personality" / "dsl" / "_build" / "default" / "bin" / "main.exe",
            project_root / "_build" / "default" / "bin" / "main.exe"
        ]
        
        for path in search_paths:
            if path.exists() and os.access(str(path), os.X_OK):
                return str(path)
        
        return None
    
    def create_test_env_if_missing(self):
        """Create a sample .env file if it doesn't exist"""
        env_path = Path(__file__).parent / '.env'
        if not env_path.exists():
            env_content = """# Callosum DSL Test Environment Variables
# Add your real API keys here for integration tests
# These are optional - most tests work without them

OPENAI_API_KEY=your-openai-api-key-here
ANTHROPIC_API_KEY=your-anthropic-api-key-here

# For testing, you can leave these as placeholders
# Integration tests will skip automatically if keys are missing
"""
            env_path.write_text(env_content)
            print(f"📝 Created sample .env file at {env_path}")
    
    def test_create_sample_env_file(self):
        """Ensure .env file exists for other tests"""
        self.create_test_env_if_missing()
        env_path = Path(__file__).parent / '.env'
        assert env_path.exists(), "Should create .env file"
    
    # MOCK TESTS - These work without API keys
    
    def test_personality_consistency_mock_openai(self):
        """Test personality consistency across questions with mocked OpenAI"""
        with patch('openai.OpenAI') as mock_openai_class:
            mock_client = Mock()
            mock_openai_class.return_value = mock_client
            
            # Mock different responses based on personality
            def mock_create(*args, **kwargs):
                messages = kwargs.get('messages', [])
                system_msg = messages[0]['content'] if messages else ""
                user_msg = messages[-1]['content'] if len(messages) > 1 else ""
                
                # Generate personality-appropriate responses
                if "Helpful AI Assistant" in system_msg:
                    response = f"I'm here to help you with {user_msg.lower()}! Let me assist you with that."
                elif "Creative Writing" in system_msg:
                    response = f"What an imaginative question! Let me craft something creative about {user_msg.lower()}..."
                elif "Technical Programming" in system_msg:
                    response = f"From a technical perspective, {user_msg.lower()} involves programming concepts I can explain."
                else:
                    response = "Mock response for testing."
                
                mock_response = Mock()
                mock_choice = Mock()
                mock_message = Mock()
                mock_message.content = response
                mock_choice.message = mock_message
                mock_response.choices = [mock_choice]
                return mock_response
            
            mock_client.chat.completions.create = mock_create
            
            results = {}
            
            # Test each personality
            for personality_name, personality_dsl in PERSONALITY_TEMPLATES.items():
                try:
                    ai = PersonalityAI(personality_dsl, compiler_path=self.compiler_path)
                except CallosumError as e:
                    if "DSL compiler not found" in str(e):
                        pytest.skip(f"DSL compiler not available at {self.compiler_path}: {e}")
                    raise
                    
                ai.set_provider("openai", api_key="mock-key")
                
                personality_results = []
                
                # Test with different question types
                for question_type, questions in self.test_questions.items():
                    for question in questions:
                        response = ai.chat(question)
                        
                        # Evaluate response
                        quality = self.evaluator.evaluate_response_quality(response, question)
                        consistency = self.evaluator.evaluate_personality_consistency(
                            response, personality_name, 
                            self.personality_expectations[personality_name]["traits"]
                        )
                        
                        personality_results.append({
                            "question_type": question_type,
                            "question": question,
                            "response": response,
                            "quality": quality,
                            "consistency": consistency
                        })
                
                results[personality_name] = personality_results
            
            # Analyze results
            self._analyze_and_report_results(results, "Mock OpenAI")
            
            # Basic assertions
            for personality_name, personality_results in results.items():
                for result in personality_results:
                    assert result["quality"]["valid"], f"Invalid response for {personality_name}: {result['quality'].get('error')}"
                    assert result["response"] != "Mock response for testing.", f"Got default mock response for {personality_name}"
    
    def test_personality_consistency_mock_langchain(self):
        """Test personality consistency with mocked LangChain"""
        with patch('langchain_core.messages') as mock_messages:
            mock_messages.SystemMessage = Mock()
            mock_messages.HumanMessage = Mock()
            mock_messages.AIMessage = Mock()
            
            results = {}
            
            for personality_name, personality_dsl in PERSONALITY_TEMPLATES.items():
                # Create mock LLM with personality-specific responses
                mock_llm = Mock()
                
                def mock_invoke(messages, **kwargs):
                    # Extract user question from last message
                    user_msg = "test question" 
                    
                    if personality_name == "helpful_assistant":
                        content = f"I'm delighted to help you with {user_msg}! My empathy and patience guide me to provide supportive assistance."
                    elif personality_name == "creative_writer":
                        content = f"What a wonderful creative challenge! Let me weave some imaginative storytelling magic around {user_msg}..."
                    elif personality_name == "technical_mentor":
                        content = f"From a technical programming perspective, {user_msg} involves several key concepts I can explain systematically."
                    
                    return type('Response', (), {'content': content})()
                
                mock_llm.invoke = mock_invoke
                mock_llm.model_name = f"mock-{personality_name}-model"
                
                try:
                    ai = PersonalityAI(personality_dsl, compiler_path=self.compiler_path)
                except CallosumError as e:
                    if "DSL compiler not found" in str(e):
                        pytest.skip(f"DSL compiler not available at {self.compiler_path}: {e}")
                    raise
                    
                ai.set_provider("langchain", llm=mock_llm)
                
                personality_results = []
                
                # Test fewer questions for speed
                test_questions = self.test_questions["general"][:2] + self.test_questions["technical"][:1]
                
                for question in test_questions:
                    response = ai.chat(question)
                    
                    # Evaluate response
                    quality = self.evaluator.evaluate_response_quality(response, question)
                    consistency = self.evaluator.evaluate_personality_consistency(
                        response, personality_name,
                        self.personality_expectations[personality_name]["traits"]
                    )
                    
                    personality_results.append({
                        "question": question,
                        "response": response,
                        "quality": quality,
                        "consistency": consistency
                    })
                
                results[personality_name] = personality_results
            
            # Analyze results  
            self._analyze_and_report_results(results, "Mock LangChain")
            
            # Assertions
            for personality_name, personality_results in results.items():
                for result in personality_results:
                    assert result["quality"]["valid"], f"Invalid response for {personality_name}"
                    # Check for personality-specific indicators
                    consistency = result["consistency"]
                    assert consistency["personality_match_ratio"] > 0, f"No personality indicators found for {personality_name}"
    
    def test_complex_personality_evaluation_mock(self):
        """Test complex .colo personality files with mocked responses"""
        
        # Load complex personality from examples
        sample_personality_path = Path(__file__).parent.parent.parent / "core" / "examples" / "sample_personality.colo"
        
        if sample_personality_path.exists():
            with open(sample_personality_path, 'r') as f:
                complex_personality = f.read()
        else:
            # Fallback complex personality
            complex_personality = '''personality: "Advanced AI Tutor"

traits:
  empathy: 0.90
  patience: 0.85
  technical_expertise: 0.88
  adaptability: 0.75

knowledge:
  domain education:
    pedagogy: expert
    learning_psychology: advanced
    
  domain programming:
    software_architecture: expert
    debugging: advanced

behaviors:
  - when empathy > 0.8 → seek "understanding student emotions"
  - when technical_expertise > 0.8 → prefer "detailed explanations"'''
        
        with patch('openai.OpenAI') as mock_openai_class:
            mock_client = Mock()
            mock_openai_class.return_value = mock_client
            
            def mock_create(*args, **kwargs):
                # Generate response based on complex personality
                response = "As an empathetic AI tutor with strong technical expertise, I understand your learning needs and can provide detailed explanations with patience and adaptability."
                mock_response = Mock()
                mock_choice = Mock()
                mock_message = Mock()
                mock_message.content = response
                mock_choice.message = mock_message  
                mock_response.choices = [mock_choice]
                return mock_response
            
            mock_client.chat.completions.create = mock_create
            
            # Test complex personality
            try:
                ai = PersonalityAI(complex_personality, compiler_path=self.compiler_path)
            except CallosumError as e:
                if "DSL compiler not found" in str(e):
                    pytest.skip(f"DSL compiler not available at {self.compiler_path}: {e}")
                raise
                
            ai.set_provider("openai", api_key="mock-key")
            
            # Get personality info
            summary = ai.get_personality_summary()
            
            # Test various questions
            results = []
            for question in ["Help me learn programming", "I'm struggling with this concept", "Explain recursion"]:
                response = ai.chat(question)
                quality = self.evaluator.evaluate_response_quality(response, question)
                
                results.append({
                    "question": question,
                    "response": response,
                    "quality": quality
                })
            
            # Verify complex personality works
            assert summary["name"] is not None
            assert len(summary["traits"]) > 2
            for result in results:
                assert result["quality"]["valid"]
                
            print("✅ Complex personality evaluation completed successfully!")
    
    # INTEGRATION TESTS - These require real API keys
    
    @pytest.mark.integration
    def test_real_openai_personality_evaluation(self):
        """Test with real OpenAI API - comprehensive personality evaluation"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        results = {}
        
        # Test each personality with real OpenAI
        for personality_name, personality_dsl in PERSONALITY_TEMPLATES.items():
            try:
                ai = PersonalityAI(personality_dsl, compiler_path=self.compiler_path)
            except CallosumError as e:
                if "DSL compiler not found" in str(e):
                    pytest.skip(f"DSL compiler not available at {self.compiler_path}: {e}")
                raise
                
            ai.set_provider("openai", api_key=self.openai_api_key)
            
            personality_results = []
            expected = self.personality_expectations[personality_name]
            
            # Test with questions relevant to this personality
            if personality_name == "helpful_assistant":
                test_questions = self.test_questions["general"][:2]
            elif personality_name == "creative_writer":  
                test_questions = self.test_questions["creative"][:2]
            elif personality_name == "technical_mentor":
                test_questions = self.test_questions["technical"][:2]
            
            for question in test_questions:
                response = ai.chat(question, max_tokens=100, temperature=0.3)
                
                # Comprehensive evaluation
                quality = self.evaluator.evaluate_response_quality(response, question, min_length=20)
                consistency = self.evaluator.evaluate_personality_consistency(response, personality_name, expected["traits"])
                domain_relevance = self.evaluator.evaluate_domain_relevance(response, expected["domain"], question)
                
                personality_results.append({
                    "question": question,
                    "response": response,
                    "quality": quality,
                    "consistency": consistency,
                    "domain_relevance": domain_relevance
                })
            
            results[personality_name] = personality_results
        
        # Analyze and report results
        self._analyze_and_report_results(results, "Real OpenAI")
        
        # Critical assertions for real API
        for personality_name, personality_results in results.items():
            for result in personality_results:
                assert result["quality"]["valid"], f"OpenAI response invalid for {personality_name}: {result['quality'].get('error')}"
                assert result["quality"]["length"] > 20, f"OpenAI response too short for {personality_name}"
                
                # Personality consistency check
                consistency = result["consistency"]
                assert consistency["personality_match_ratio"] >= 0.05, f"No personality indicators for {personality_name} in response: {result['response'][:100]}"
    
    @pytest.mark.integration  
    def test_real_langchain_openai_personality_evaluation(self):
        """Test with real LangChain + OpenAI - personality evaluation"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        try:
            from langchain_openai import ChatOpenAI
        except ImportError:
            pytest.skip("langchain-openai not installed")
        
        results = {}
        
        for personality_name, personality_dsl in PERSONALITY_TEMPLATES.items():
            # Create real LangChain OpenAI model
            llm = ChatOpenAI(
                model="gpt-3.5-turbo",
                api_key=self.openai_api_key, 
                max_tokens=80,
                temperature=0.2
            )
            
            ai = PersonalityAI(personality_dsl, compiler_path=self.compiler_path)
            ai.set_provider("langchain", llm=llm)
            
            # Test one representative question per personality
            if personality_name == "helpful_assistant":
                question = "I need help solving a problem"
            elif personality_name == "creative_writer":
                question = "Write a creative story opening" 
            elif personality_name == "technical_mentor":
                question = "Explain programming concepts"
            
            response = ai.chat(question)
            
            # Evaluate
            quality = self.evaluator.evaluate_response_quality(response, question, min_length=15)
            consistency = self.evaluator.evaluate_personality_consistency(response, personality_name, 
                                                                        self.personality_expectations[personality_name]["traits"])
            
            results[personality_name] = [{
                "question": question,
                "response": response,
                "quality": quality,
                "consistency": consistency,
                "provider": "langchain-openai"
            }]
        
        # Report results
        self._analyze_and_report_results(results, "Real LangChain + OpenAI")
        
        # Assertions
        for personality_name, personality_results in results.items():
            result = personality_results[0]  # Single result per personality
            assert result["quality"]["valid"], f"LangChain response invalid for {personality_name}"
            assert result["quality"]["length"] > 15, f"LangChain response too short for {personality_name}"
    
    @pytest.mark.integration
    def test_cross_provider_personality_consistency(self):
        """Test same personality across different providers for consistency"""
        if not self.openai_api_key:
            pytest.skip("OPENAI_API_KEY environment variable not set")
        
        try:
            from langchain_openai import ChatOpenAI
        except ImportError:
            pytest.skip("langchain-openai not installed")
        
        # Use helpful_assistant personality
        personality_dsl = PERSONALITY_TEMPLATES["helpful_assistant"]
        question = "Hello, can you help me today?"
        
        # Test with OpenAI directly
        ai_openai = PersonalityAI(personality_dsl, compiler_path=self.compiler_path)
        ai_openai.set_provider("openai", api_key=self.openai_api_key)
        response_openai = ai_openai.chat(question, max_tokens=60, temperature=0.1)
        
        # Test with LangChain + OpenAI  
        llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=self.openai_api_key, max_tokens=60, temperature=0.1)
        ai_langchain = PersonalityAI(personality_dsl, compiler_path=self.compiler_path) 
        ai_langchain.set_provider("langchain", llm=llm)
        response_langchain = ai_langchain.chat(question)
        
        # Evaluate both responses
        quality_openai = self.evaluator.evaluate_response_quality(response_openai, question)
        quality_langchain = self.evaluator.evaluate_response_quality(response_langchain, question)
        
        consistency_openai = self.evaluator.evaluate_personality_consistency(response_openai, "helpful_assistant", ["helpfulness", "empathy"])
        consistency_langchain = self.evaluator.evaluate_personality_consistency(response_langchain, "helpful_assistant", ["helpfulness", "empathy"])
        
        # Both should be valid and show helpful personality traits
        assert quality_openai["valid"] and quality_langchain["valid"]
        assert consistency_openai["personality_match_ratio"] > 0
        assert consistency_langchain["personality_match_ratio"] > 0
        
        print(f"✅ OpenAI Direct: {response_openai}")
        print(f"✅ LangChain+OpenAI: {response_langchain}")
        print("✅ Cross-provider personality consistency verified!")
    
    def _analyze_and_report_results(self, results: Dict[str, List], provider_name: str):
        """Analyze and report comprehensive test results"""
        print(f"\n{'='*60}")
        print(f"🧪 COMPREHENSIVE EVALUATION RESULTS - {provider_name}")
        print(f"{'='*60}")
        
        total_tests = sum(len(personality_results) for personality_results in results.values())
        valid_responses = 0
        personality_matches = 0
        
        for personality_name, personality_results in results.items():
            print(f"\n🎭 {personality_name.upper().replace('_', ' ')}")
            print("-" * 40)
            
            personality_valid = 0
            personality_match_count = 0
            
            for i, result in enumerate(personality_results):
                quality = result["quality"]
                consistency = result.get("consistency", {})
                
                if quality["valid"]:
                    valid_responses += 1
                    personality_valid += 1
                    
                if consistency.get("personality_match_ratio", 0) > 0.1:
                    personality_matches += 1
                    personality_match_count += 1
                
                # Show sample result
                if i == 0:  # Show first result as example
                    print(f"Q: {result['question'][:50]}...")
                    print(f"A: {result['response'][:100]}...")
                    print(f"Quality: {'✅ Valid' if quality['valid'] else '❌ Invalid'} "
                          f"({quality.get('length', 0)} chars)")
                    print(f"Personality Match: {consistency.get('personality_match_ratio', 0):.2%}")
            
            print(f"Results: {personality_valid}/{len(personality_results)} valid, "
                  f"{personality_match_count}/{len(personality_results)} personality matches")
        
        # Overall statistics
        print(f"\n📊 OVERALL STATISTICS")
        print(f"{'─'*40}")
        print(f"Total Tests: {total_tests}")
        print(f"Valid Responses: {valid_responses}/{total_tests} ({valid_responses/total_tests:.1%})")
        print(f"Personality Matches: {personality_matches}/{total_tests} ({personality_matches/total_tests:.1%})")
        
        success_rate = valid_responses / total_tests if total_tests > 0 else 0
        if success_rate >= 0.9:
            print("🎉 EXCELLENT: 90%+ success rate!")
        elif success_rate >= 0.7:
            print("✅ GOOD: 70%+ success rate")
        elif success_rate >= 0.5:
            print("⚠️ FAIR: 50%+ success rate")
        else:
            print("❌ POOR: <50% success rate")
        
        print(f"\n✨ {provider_name} evaluation complete!\n")


if __name__ == "__main__":
    # Run comprehensive evaluation tests
    pytest.main([__file__, "-v", "-s"])

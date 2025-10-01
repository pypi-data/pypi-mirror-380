"""
Core classes and functions for Callosum Personality DSL Python integration
"""

import subprocess
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional, Union

# Handle resource loading with backwards compatibility
try:
    # Python 3.9+
    from importlib import resources
    def _get_resource_path(package: str, resource: str) -> str:
        # Handle subdirectories properly
        if '/' in resource:
            parts = resource.split('/')
            subpackage = '.'.join([package] + parts[:-1])
            filename = parts[-1]
            files = resources.files(subpackage)
            return str(files / filename)
        else:
            files = resources.files(package)
            return str(files / resource)
except ImportError:
    try:
        # Python 3.8 - try importlib_resources
        import importlib_resources as resources
        def _get_resource_path(package: str, resource: str) -> str:
            if '/' in resource:
                parts = resource.split('/')
                subpackage = '.'.join([package] + parts[:-1])
                filename = parts[-1]
                files = resources.files(subpackage)
                return str(files / filename)
            else:
                files = resources.files(package)
                return str(files / resource)
    except ImportError:
        # Fallback to pkg_resources (deprecated but available)
        import pkg_resources
        def _get_resource_path(package: str, resource: str) -> str:
            return pkg_resources.resource_filename(package, resource)


class CallosumError(Exception):
    """Base exception for Callosum DSL errors"""
    pass


class ParseError(CallosumError):
    """Raised when DSL parsing fails"""
    pass


class CompileError(CallosumError):
    """Raised when DSL compilation fails"""
    pass


class Callosum:
    """
    Python wrapper for Callosum Personality DSL
    
    Provides direct access to the DSL compiler with a clean Python API.
    """
    
    def __init__(self, compiler_path: Optional[str] = None):
        """
        Initialize the Callosum wrapper
        
        Args:
            compiler_path: Path to the dsl-parser binary. If None, will search
                          for it in the package or system PATH
        """
        self.compiler_path = self._find_compiler(compiler_path)
        if not self.compiler_path:
            raise CallosumError(
                "DSL compiler not found. The binary should be included with the package. "
                "If you built from source, ensure 'dune build' was run."
            )
    
    def _find_compiler(self, explicit_path: Optional[str]) -> Optional[str]:
        """Find the DSL compiler binary"""
        if explicit_path:
            return explicit_path if os.path.exists(explicit_path) else None
            
        # Search in package resources first
        try:
            binary_path = _get_resource_path('callosum_dsl', 'bin/dsl-parser')
            if os.path.exists(binary_path) and os.access(binary_path, os.X_OK):
                return binary_path
        except:
            pass
            
        # Search in common development locations
        search_paths = [
            # In the project (for development)
            "personality/dsl/_build/default/bin/main.exe",
            "_build/default/bin/main.exe",
            # Installed system-wide
            "dsl-parser"
        ]
        
        for path in search_paths:
            if os.path.exists(path):
                return os.path.abspath(path)
            
            # Check if it's in PATH
            if path == "dsl-parser":
                try:
                    result = subprocess.run(
                        ["which", "dsl-parser"], 
                        capture_output=True, text=True
                    )
                    if result.returncode == 0:
                        return result.stdout.strip()
                except (subprocess.SubprocessError, FileNotFoundError):
                    continue
        
        return None
    
    def compile(self, dsl_content: str, target: str = "json", 
                context: Optional[str] = None) -> str:
        """
        Compile DSL content to target format
        
        Args:
            dsl_content: The personality DSL as string
            target: Output format (json, prompt, lua, sql, cypher)
            context: Optional context hint for prompt generation
            
        Returns:
            Compiled output as string
            
        Raises:
            ParseError: If DSL parsing fails
            CompileError: If compilation fails
        """
        if not dsl_content.strip():
            raise ParseError("DSL content is empty")
        
        # Prepare command
        cmd = [self.compiler_path, "--output", target]
        
        if context:
            cmd.extend(["--context", context])
        
        # Use stdin for DSL content
        cmd.extend(["--input", "-"])
        
        try:
            result = subprocess.run(
                cmd,
                input=dsl_content,
                capture_output=True,
                text=True,
                timeout=30  # Reasonable timeout
            )
            
            if result.returncode != 0:
                error_msg = result.stderr.strip() if result.stderr else "Unknown compilation error"
                if "Parse errors:" in error_msg:
                    raise ParseError(error_msg)
                else:
                    raise CompileError(error_msg)
            
            # Filter out warnings from stdout (they start with "WARNING:")
            output_lines = result.stdout.split('\n')
            clean_output = '\n'.join(line for line in output_lines if not line.startswith('WARNING:'))
            
            return clean_output.strip()
            
        except subprocess.TimeoutExpired:
            raise CompileError("Compilation timed out")
        except FileNotFoundError:
            raise CallosumError(f"Compiler not found at: {self.compiler_path}")
    
    def to_json(self, dsl_content: str) -> Dict[str, Any]:
        """
        Compile DSL to JSON and return parsed data
        
        Args:
            dsl_content: The personality DSL as string
            
        Returns:
            Parsed personality data as dict
        """
        json_output = self.compile(dsl_content, "json")
        try:
            return json.loads(json_output)
        except json.JSONDecodeError as e:
            raise CompileError(f"Invalid JSON output: {e}")
    
    def to_prompt(self, dsl_content: str, context: Optional[str] = None) -> str:
        """
        Compile DSL to system prompt for LLMs
        
        Args:
            dsl_content: The personality DSL as string
            context: Optional context for prompt customization
            
        Returns:
            System prompt as string
        """
        return self.compile(dsl_content, "prompt", context)
    
    def to_lua(self, dsl_content: str) -> str:
        """
        Compile DSL to Lua script
        
        Args:
            dsl_content: The personality DSL as string
            
        Returns:
            Lua script as string
        """
        return self.compile(dsl_content, "lua")
    
    def to_sql(self, dsl_content: str) -> str:
        """
        Compile DSL to SQL schema and data
        
        Args:
            dsl_content: The personality DSL as string
            
        Returns:
            SQL statements as string
        """
        return self.compile(dsl_content, "sql")
    
    def to_cypher(self, dsl_content: str) -> str:
        """
        Compile DSL to Cypher queries for Neo4j
        
        Args:
            dsl_content: The personality DSL as string
            
        Returns:
            Cypher queries as string
        """
        return self.compile(dsl_content, "cypher")
    
    def load_file(self, filepath: Union[str, Path]) -> str:
        """
        Load DSL content from file
        
        Args:
            filepath: Path to .colo file
            
        Returns:
            DSL content as string
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return f.read()
        except IOError as e:
            raise CallosumError(f"Failed to read file {filepath}: {e}")
    
    def validate(self, dsl_content: str) -> bool:
        """
        Validate DSL content without compilation
        
        Args:
            dsl_content: The personality DSL as string
            
        Returns:
            True if valid, False otherwise
        """
        try:
            self.compile(dsl_content, "json")
            return True
        except (ParseError, CompileError):
            return False


class PersonalityAI:
    """
    AI assistant with Callosum personality
    
    Integrates with popular AI APIs like OpenAI, Anthropic, etc.
    """
    
    def __init__(self, personality_dsl: str, 
                 api_key: Optional[str] = None,
                 provider: str = "openai",
                 compiler_path: Optional[str] = None):
        """
        Initialize AI with personality
        
        Args:
            personality_dsl: DSL defining the personality
            api_key: API key for the AI provider
            provider: AI provider ("openai", "anthropic") 
            compiler_path: Path to DSL compiler
        """
        self.callosum = Callosum(compiler_path)
        self.personality_dsl = personality_dsl
        self.provider = provider.lower()
        
        # Compile personality
        try:
            self.personality_data = self.callosum.to_json(personality_dsl)
            self.system_prompt = self.callosum.to_prompt(personality_dsl)
        except (ParseError, CompileError) as e:
            raise CallosumError(f"Failed to compile personality: {e}")
        
        # Initialize AI client if API key provided
        self.client = None
        if api_key:
            self._init_ai_client(api_key)
    
    def _init_ai_client(self, api_key: str):
        """Initialize the AI client"""
        try:
            if self.provider == "openai":
                import openai
                self.client = openai.OpenAI(api_key=api_key)
            elif self.provider == "anthropic":
                import anthropic
                self.client = anthropic.Anthropic(api_key=api_key)
            else:
                raise ValueError(f"Unsupported provider: {self.provider}")
        except ImportError as e:
            raise CallosumError(
                f"Required package not installed for {self.provider}: {e}\n"
                f"Install with: pip install {self.provider}"
            )
    
    def chat(self, message: str, model: Optional[str] = None, **kwargs) -> str:
        """
        Chat with the AI using the personality
        
        Args:
            message: User message
            model: AI model to use (provider-specific)
            **kwargs: Additional parameters for the AI API
            
        Returns:
            AI response as string
        """
        if not self.client:
            raise CallosumError(
                "No AI client initialized. Provide api_key during initialization."
            )
        
        if self.provider == "openai":
            model = model or "gpt-4"
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {"role": "user", "content": message}
                ],
                **kwargs
            )
            return response.choices[0].message.content
        
        elif self.provider == "anthropic":
            model = model or "claude-3-sonnet-20240229"
            response = self.client.messages.create(
                model=model,
                max_tokens=kwargs.get('max_tokens', 1000),
                system=self.system_prompt,
                messages=[{"role": "user", "content": message}],
                **{k: v for k, v in kwargs.items() if k != 'max_tokens'}
            )
            return response.content[0].text
        
        else:
            raise CallosumError(f"Chat not implemented for provider: {self.provider}")
    
    def get_trait_strength(self, trait_name: str) -> Optional[float]:
        """Get the strength of a specific trait"""
        for trait in self.personality_data.get("traits", []):
            if trait["name"] == trait_name:
                return trait["strength"]
        return None
    
    def get_personality_summary(self) -> Dict[str, Any]:
        """Get a summary of the personality"""
        traits = {trait["name"]: trait["strength"] 
                 for trait in self.personality_data.get("traits", [])}
        
        return {
            "name": self.personality_data.get("name"),
            "traits": traits,
            "dominant_trait": max(traits.keys(), key=lambda k: traits[k]) if traits else None,
            "knowledge_domains": [domain["name"] for domain in self.personality_data.get("knowledge", [])],
            "system_prompt_length": len(self.system_prompt)
        }

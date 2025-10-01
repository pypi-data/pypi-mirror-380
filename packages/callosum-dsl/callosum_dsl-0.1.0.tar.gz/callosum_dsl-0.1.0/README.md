# Callosum AI Language Personality DSL

A powerful Domain Specific Language for defining rich, dynamic personalities for AI language models. Create sophisticated AI assistants with nuanced traits, evolving knowledge, context-aware behaviors, and adaptive learning patterns.

## Overview

The Callosum Personality DSL enables declarative definition of AI language model personalities that can evolve through interactions, featuring:

- **Dynamic Traits** with contextual modifiers, decay patterns, and amplification effects
- **Knowledge Domains** with expertise levels, inter-domain connections, and learning pathways  
- **Behavioral Rules** that trigger based on conversation context and internal state
- **Evolution Specifications** for personality growth through user interactions and learning

**Perfect for**: Creating unique AI assistants, chatbots, creative writing companions, educational tutors, and specialized AI agents with consistent, evolving personalities.

## Quick Start

### Installation

Navigate to the DSL directory and install dependencies:

```bash
cd personality/dsl

# Install OCaml dependencies
opam install . --deps-only

# Build the project
dune build

# Run tests
dune runtest
```

### Basic Usage

```ocaml
personality "Helpful AI Assistant" {
  traits {
    helpfulness: 0.9 with amplifies("problem_solving", 1.3);
    curiosity: 0.8 with decay(0.02/month), when("learning_opportunity");
    patience: 0.85 with unless("repetitive_questions");
    creativity: 0.7 with when("creative_tasks");
  }
  
  knowledge {
    domain("general_knowledge") {
      science: advanced;
      history: intermediate;
      arts: intermediate;
      "general_knowledge" connects_to "conversation" with 0.8;
    }
    
    domain("conversation") {
      active_listening: expert;
      empathy: advanced;
      explanation: expert;
    }
    
    domain("problem_solving") {
      analysis: advanced;
      creative_thinking: intermediate;
      "conversation" connects_to "problem_solving" with 0.9;
    }
  }
  
  behaviors {
    when helpfulness > 0.8 -> seek("ways to assist user");
    when curiosity > 0.7 -> ask("clarifying questions");
    when patience > 0.8 -> prefer("detailed explanations");
    when creativity > 0.6 -> seek("creative approaches");
    when "user_frustrated" -> prefer("calming, supportive tone");
  }
  
  evolution {
    if learns("user_preference") then trait("helpfulness") += 0.05;
    if interactions(100) then unlock_domain("specialized_knowledge");
    if learns("new_topic") then add_connection("general_knowledge", "conversation", 0.9);
    if learns("communication_style") then trait("empathy") += 0.1;
  }
}
```

## Architecture

```
lib/
├── types.ml       # Core type definitions
├── lexer.mll      # Lexical analysis
├── parser.mly     # Grammar parsing (Menhir)
├── ast.ml         # Abstract Syntax Tree utilities
├── semantic.ml    # Semantic analysis & validation
├── compiler.ml    # Multi-target compilation
└── optimize.ml    # Personality optimization
```

## Compilation Targets

The DSL compiles personalities to multiple formats for different AI language model integrations:

- **Prompt** - System prompts for OpenAI, Anthropic, and other LLM APIs
- **JSON** - Structured personality data for custom AI frameworks
- **Lua** - Runtime personality scripts for dynamic behavior systems
- **SQL** - Database storage for persistent personality evolution
- **Cypher** - Graph database for complex knowledge relationship modeling

```bash
# Generate system prompt for AI language models
dsl-parser --input examples/sample_personality.colo --output prompt

# Export as JSON for AI frameworks
dsl-parser --input examples/sample_personality.colo --output json

# Create Lua scripts for dynamic personality systems
dsl-parser --input examples/sample_personality.colo --output lua
```

## Features for AI Language Models

### Dynamic Trait System
- `decay(rate/time_unit)` - Traits naturally evolve over time (e.g., enthusiasm fades without engagement)
- `when(context)` - Contextual trait activation (e.g., "when teaching" -> increased patience)
- `unless(context)` - Contextual suppression (e.g., unless "user_frustrated" -> maintain formality)
- `amplifies(trait, factor)` - Cross-trait interactions (e.g., curiosity amplifies helpfulness)
- `transforms_to(trait, factor, count)` - Long-term personality evolution

### AI Knowledge Modeling
- **Expertise levels**: beginner, intermediate, advanced, expert - define AI's knowledge confidence
- **Domain connections** - model how knowledge areas reinforce each other in responses
- **Learning pathways** - define how AI acquires and integrates new knowledge

### Context-Aware Behaviors  
- **Conversation triggers**: trait thresholds, user emotional state, topic detection
- **Response preferences**: communication style, approach selection, topic focusing
- **Adaptive responses**: seek clarification, avoid complexity, prefer examples

### Interaction-Based Evolution
- **Learning triggers**: user feedback, successful interactions, topic exposure
- **Personality growth**: trait strengthening, new domain unlocking, connection formation
- **Memory formation**: persistent changes based on conversation patterns

## Semantic Analysis

Built-in validation detects:
- Circular dependencies in knowledge domains
- Conflicting trait modifiers  
- Non-deterministic evolution rules
- Unreachable behaviors
- Invalid domain references
- Unsafe trait modifications

## Docker Support

```bash
# Build container
docker build -f infrastructure/Dockerfile -t callosum-dsl .

# Run parser service
docker run -p 8001:8001 callosum-dsl
```

## Development

### Project Structure
```
callosum/
├── README.md                    # Main project documentation
├── package.json                 # Node.js workspace configuration
│
└── personality/dsl/             # Personality DSL Implementation
    ├── lib/                     # Core library modules
    │   ├── ast.ml               # Abstract Syntax Tree
    │   ├── compiler.ml          # Multi-target compilation
    │   ├── lexer.mll            # Lexical analysis
    │   ├── parser.mly           # Grammar parsing
    │   ├── semantic.ml          # Semantic analysis
    │   ├── types.ml             # Type definitions
    │   └── optimize.ml          # Optimization passes
    │
    ├── bin/                     # Executable entry point
    │   └── main.ml              # Command-line interface
    │
    ├── test/                    # Comprehensive test suite
    │   ├── test_parser.ml       # Main parser tests
    │   └── test_parse.ml        # Additional parsing tests
    │
    ├── examples/                # Sample personality definitions
    │   ├── README.md            # Examples documentation
    │   ├── sample_personality.colo    # Comprehensive example
    │   └── test_personality.colo      # Simple test example
    │
    ├── infrastructure/          # Docker deployment
    │   └── Dockerfile           # Container configuration
    │
    ├── dune-project             # OCaml build configuration
    └── dsl-parser.opam          # Package definition
```

### Testing
```bash
# Run all tests
dune runtest

# Run specific test category  
dune exec test/test_parser.exe
```

### Adding New Features

1. **Extend types** in `types.ml`
2. **Update lexer** in `lexer.mll` for new tokens
3. **Modify grammar** in `parser.mly` for syntax
4. **Add validation** in `semantic.ml` 
5. **Update compiler** in `compiler.ml` for new targets
6. **Write tests** in `test/test_parser.ml`

## API Reference

### Core Functions
```ocaml
(* Parse personality from string *)
val parse_personality_from_string : ?filename:string -> string -> 
  (personality, parse_error list) result

(* Compile to target format *)  
val compile : personality -> target -> ?context:string -> unit ->
  (string, compiler_error list) result

(* Semantic analysis *)
val analyze : personality -> analysis_result

(* Optimization *)
val optimize_personality : personality -> level -> 
  personality * stats
```

## File Extensions

- `.colo` - Personality definition files
- `.colo.json` - Compiled JSON output
- `.colo.lua` - Compiled Lua scripts

## License

MIT

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Add tests for new functionality
4. Ensure all tests pass (`dune runtest`)
5. Submit pull request

---

*Part of the Callosum AI Personality System*

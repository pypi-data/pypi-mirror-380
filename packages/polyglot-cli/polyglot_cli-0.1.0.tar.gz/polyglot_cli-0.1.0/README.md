# 🌍 Polyglot - AI Code Translator

An AI-powered CLI tool that translates code between programming languages using Claude Sonnet 4.5's extended thinking capabilities.

## Features

- 🧠 **Extended Thinking** - See the AI's reasoning process as it translates
- 🎨 **Idiomatic Translation** - Not just syntax conversion, but proper language idioms
- ⚡ **Smart Optimization** - Optimizes for target language best practices
- 📊 **Side-by-side Comparison** - Visual diff of source and target
- 🎯 **12+ Languages** - Python, Rust, Go, TypeScript, Java, C++, and more

## Installation

### Option 1: Install from PyPI (Recommended)
```bash
pip install polyglot-cli

# Set your API key
export ANTHROPIC_API_KEY='your-key-here'
```

### Option 2: Install from source
```bash
git clone https://github.com/samar/polyglot-cli.git
cd polyglot-cli
pip install -e .

# Set your API key
export ANTHROPIC_API_KEY='your-key-here'
```

### Option 3: Use pipx (Isolated installation)
```bash
pipx install polyglot-cli
export ANTHROPIC_API_KEY='your-key-here'
```

## Usage

### Translate a file
```bash
polyglot translate python rust --file example.py
```

### Translate from stdin
```bash
echo 'def hello(): print("hi")' | polyglot translate python go
```

### Save output
```bash
polyglot translate python rust --file example.py --output example.rs
```

### Hide AI reasoning
```bash
polyglot translate python rust --file example.py --no-thinking
```

### List supported languages
```bash
polyglot languages
```

## Examples

### Python → Rust
```bash
polyglot translate python rust --file example.py
```

The AI will:
1. Show its thinking process (how it approaches the translation)
2. Convert Python's dynamic types to Rust's static types
3. Replace Python's dict cache with Rust's HashMap
4. Use idiomatic Rust patterns
5. Show side-by-side comparison

### JavaScript → Go
```bash
polyglot translate javascript go --file api.js
```

Converts async/await to Go's goroutines and channels!

## Why Polyglot?

This showcases Claude Sonnet 4.5's **extended thinking** - you can literally see the AI reasoning through:
- Type system differences
- Memory management patterns
- Idiomatic conventions
- Performance trade-offs

It's not just translating syntax, it's understanding and adapting code philosophy between languages!

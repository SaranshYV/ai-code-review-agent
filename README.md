# 🤖 AI Code Review Agent

An intelligent code review and bug-fixing agent powered by AI. Analyzes your code for errors, security issues, performance problems, and provides automated fixes with detailed explanations.

## ✨ Features

- **Automatic Code Analysis**: Detects bugs, errors, and code quality issues
- **Multi-Language Support**: Python, JavaScript, TypeScript, Java, C++, Go, Rust, PHP, Ruby
- **Intelligent Fixing**: Generates corrected code with explanations
- **Comprehensive Reports**: Detailed analysis with categorized issues
- **Interactive Mode**: Paste code directly for quick analysis
- **Multiple Input Methods**: Analyze files or interactive input
- **JSON Report Export**: Save analysis results for documentation

## 🚀 Installation

### Prerequisites
- Python 3.8+
- OpenAI API Key

### Setup

1. Clone the repository:
```bash
git clone https://github.com/SaranshYV/ai-code-review-agent.git
cd ai-code-review-agent
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## 📖 Usage

### Analyze a File
```bash
python cli.py analyze myfile.py
```

With options:
```bash
python cli.py analyze myfile.py --language python --save-report
```

### Generate Fixes
```bash
python cli.py fix myfile.py
```

Save fixed code to a file:
```bash
python cli.py fix myfile.py --output fixed_file.py
```

### Interactive Mode
```bash
python cli.py interactive
```

Then paste your code and press Ctrl+D (Unix) or Ctrl+Z (Windows).

## 🔍 Analysis Categories

The agent analyzes code for:

- **Syntax Errors**: Invalid code structure
- **Logic Errors**: Incorrect program logic
- **Performance Issues**: Inefficient code patterns
- **Security Vulnerabilities**: Potential security risks
- **Code Style**: Naming, formatting, conventions
- **Best Practices**: Language-specific best practices
- **Memory Leaks**: Potential memory issues
- **Type Safety**: Type-related problems

## 📋 Configuration

Edit `.env` file to customize:

```ini
# API Configuration
OPENAI_API_KEY=your_key_here
MODEL_NAME=gpt-4
TEMPERATURE=0.7

# Analysis Settings
MAX_FILE_SIZE=50000
ANALYSIS_DEPTH=detailed
```

## 📊 Report Example

The agent generates detailed reports including:

1. **Summary**: Overview of code quality
2. **Issues Found**: Categorized by severity
3. **Explanations**: Why each issue matters
4. **Recommendations**: How to fix them
5. **Security**: Identified vulnerabilities

## 🛠️ Development

### Project Structure
```
ai-code-review-agent/
├── cli.py              # Command-line interface
├── code_analyzer.py    # Core analysis logic
├── config.py           # Configuration management
├── report_generator.py # Report generation
├── requirements.txt    # Dependencies
├── .env.example        # Environment template
└── README.md          # This file
```

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📝 License

MIT License - see LICENSE file for details

## ⚠️ Important Notes

- Requires OpenAI API key (GPT-4 or compatible)
- Analyze code responsibly
- Review AI suggestions before applying to production
- Keep API key secure in `.env` file

## 🐛 Known Limitations

- File size limited to MAX_FILE_SIZE (default 50KB)
- Requires internet connection for API calls
- Analysis quality depends on code clarity
- AI suggestions should be reviewed by humans

## 📞 Support

For issues and feature requests, please create an issue on GitHub.

---

**Made with ❤️ by AI Code Review Agent**

# 🧠 AI Coding Assistant

A powerful AI-powered coding assistant that intelligently enhances prompts before generating code.

**Built with:**
- FastAPI (Backend)
- OpenAI GPT-3.5-Turbo API (Code generation)
- Python (Frontend/CLI)

## ✨ New Features (v1.1.0)

### **Intelligent Prompt Enhancement Pipeline**
The assistant now automatically improves your prompts before sending them to OpenAI:

- 🔤 **Grammar & Punctuation Fix**: Standardizes your prompt format
- ✔️ **Clarity Validation**: Detects vague keywords and unclear requirements
- 📋 **Complexity Analysis**: Breaks down complex multi-step requests
- 🎯 **Best Practices**: Adds language-specific coding standards (Python, JavaScript, Java, C++)

### **Improved API Key Management**
- ✓ Fixed authentication errors with proper environment variable caching
- ✓ Automatic API key refresh on startup
- ✓ Better error handling and debugging

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment
# Create .env file:
# OPENAI_API_KEY=sk-proj-your-key-here
```

### Run Backend
```bash
# Start FastAPI server
uvicorn backend.app:app --reload
# Server runs on: http://127.0.0.1:8000
```

### Example Request
```bash
curl -X POST "http://127.0.0.1:8000/generate_code" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "create a calculator with add and multiply functions",
    "language": "Python"
  }'
```

## 📚 How the Prompt Enhancement Pipeline Works

When you provide a prompt like:
```
"write me a program that do something with numbers"
```

The pipeline automatically:

1. **Fixes Grammar** → "Write me a program that does something with numbers."
2. **Validates Clarity** → Detects "something" is vague, suggests being more specific
3. **Analyzes Complexity** → Breaks down into structured steps
4. **Adds Best Practices** → Includes language-specific coding standards
5. **Enhances Output** → Sends much better prompt to OpenAI

Result: **Better quality generated code** with fewer iterations!

## 📝 Supported Languages

- ✅ Python (with PEP 8 standards)
- ✅ JavaScript (with async/await best practices)
- ✅ Java (with SOLID principles)
- ✅ C++ (with STL and memory management)

## 🔧 Architecture

```
backend/
├── app.py          # FastAPI application & endpoints
├── utils.py        # Prompt enhancement pipeline & OpenAI integration
└── 
frontend/
├── main.py         # Frontend application
```

### Key Functions in `utils.py`

- `validate_clarity(prompt)` - Check requirement clarity
- `break_down_complex_request(prompt)` - Analyze and structure complex requests
- `add_best_practices(prompt, language)` - Add language-specific guidelines
- `fix_grammar(prompt)` - Standardize prompt format
- `enhance_prompt(prompt, language)` - Main pipeline orchestrator
- `generate_code_from_prompt(prompt, language)` - Generate code with enhanced prompt

## ⚙️ Configuration

### Environment Variables (.env)

```env
OPENAI_API_KEY=sk-proj-your-actual-api-key
```

**Important**: Do NOT wrap the API key in quotes!

## 🧪 Test Prompts

Try these to see the enhancement pipeline in action:

1. **Vague Request**: "write me a program that do something with numbers"
2. **Complex Request**: "create a calculator that can add and multiply and divide numbers with error handling"
3. **Good Request**: "Write a Python function that generates the first n fibonacci numbers"

## 🐛 Troubleshooting

### Authentication Error (401)
- Verify your API key is valid and not expired
- Check `.env` file doesn't have quotes around the key
- Restart the server after updating the key

### ImportError
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Make sure you're using a Python virtual environment

## 📋 Requirements

See `requirements.txt` for all dependencies.

## 📈 Roadmap

- [ ] Add caching for common prompts
- [ ] Implement prompt templates library
- [ ] Add code review/quality scoring
- [ ] Support for more programming languages
- [ ] Web UI with history and favorites

## 📄 License

MIT License - Feel free to use and modify

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests.

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Version**: 1.1.0  
**Last Updated**: April 6, 2026

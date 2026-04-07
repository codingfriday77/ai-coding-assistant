from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists (local development)
# On Render, environment variables are set directly in the dashboard
load_dotenv(override=False)

# Lazy initialization of the client - defer until actually needed
_client = None

def get_openai_client():
    """Get or initialize the OpenAI client."""
    global _client
    if _client is None:
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is not set.")
        _client = OpenAI(api_key=api_key)
    return _client
# ============ PROMPT ENHANCEMENT PIPELINE ============

def validate_clarity(prompt: str) -> tuple[bool, str]:
    """
    Validates if the prompt is clear and specific enough.
    Returns: (is_clear: bool, feedback: str)
    """
    clarity_issues = []
    
    # Check for minimum length
    if len(prompt.strip()) < 10:
        clarity_issues.append("Prompt is too short - please provide more details")
    
    # Check for vague keywords
    vague_words = ["something", "stuff", "thing", "it", "do something"]
    for word in vague_words:
        if word.lower() in prompt.lower():
            clarity_issues.append(f"Prompt contains vague word: '{word}' - be more specific")
    
    # Check for question mark (usually indicates clarity)
    has_question_format = "?" in prompt or "write" in prompt.lower() or "create" in prompt.lower()
    
    if clarity_issues:
        return False, " | ".join(clarity_issues)
    return True, "Prompt is clear and specific"

def break_down_complex_request(prompt: str) -> str:
    """
    Identifies complex requests and breaks them down into steps.
    """
    complexity_indicators = ["multiple", "and", "then", "after", "before", "with", "including"]
    
    # Check if prompt appears complex
    is_complex = any(indicator in prompt.lower() for indicator in complexity_indicators)
    
    if is_complex:
        breakdown = (
            f"{prompt}\n\n"
            "Break this down into steps:\n"
            "1. First step: [identify the main requirement]\n"
            "2. Second step: [identify supporting features]\n"
            "3. Third step: [identify edge cases]\n"
        )
        return breakdown
    
    return prompt

def add_best_practices(prompt: str, language: str) -> str:
    """
    Adds coding best practices and quality requirements to the prompt.
    """
    best_practices = {
        "Python": "Use clear variable names, add docstrings, handle errors with try-except, follow PEP 8 style",
        "JavaScript": "Use camelCase for variables, add comments, use const/let wisely, handle promises/async-await",
        "Java": "Use proper naming conventions, add documentation, handle exceptions, follow SOLID principles",
        "C++": "Use meaningful variable names, add comments, manage memory properly, use STL when possible",
        "default": "Write clean, readable code with comments, use meaningful variable names, handle errors appropriately"
    }
    
    practices = best_practices.get(language, best_practices["default"])
    
    enhanced = (
        f"{prompt}\n\n"
        f"Code Quality Requirements:\n"
        f"- Language: {language}\n"
        f"- Best practices: {practices}\n"
        f"- Add comments for complex logic\n"
        f"- Include error handling\n"
    )
    
    return enhanced

def fix_grammar(prompt: str) -> str:
    """
    Basic grammar and clarity improvements.
    """
    # Remove extra spaces
    prompt = " ".join(prompt.split())
    
    # Capitalize first letter
    if prompt and not prompt[0].isupper():
        prompt = prompt[0].upper() + prompt[1:]
    
    # Ensure it ends with proper punctuation
    if prompt and prompt[-1] not in ".!?":
        prompt += "."
    
    return prompt

def enhance_prompt(prompt: str, language: str) -> str:
    """
    Main prompt enhancement pipeline.
    Applies all enhancement steps in sequence.
    """
    print(f"[Pipeline] Original prompt: {prompt}\n")
    
    # Step 1: Fix grammar
    prompt = fix_grammar(prompt)
    print(f"[Step 1] Grammar fixed: {prompt}\n")
    
    # Step 2: Validate clarity
    is_clear, feedback = validate_clarity(prompt)
    print(f"[Step 2] Clarity check: {feedback}\n")
    
    # Step 3: Break down complex requests
    prompt = break_down_complex_request(prompt)
    print(f"[Step 3] Complexity analysis done\n")
    
    # Step 4: Add best practices
    prompt = add_best_practices(prompt, language)
    print(f"[Step 4] Best practices added\n")
    
    return prompt

# ============ END PROMPT ENHANCEMENT PIPELINE ============

def generate_code_from_prompt(prompt: str, language: str) -> str:
    # Enhance the prompt using the pipeline
    enhanced_prompt = enhance_prompt(prompt, language)
    
    full_prompt = f"Write a {language} program to: {enhanced_prompt}\n\nCode:\n"

    client = get_openai_client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful coding assistant."},
            {"role": "user", "content": full_prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()

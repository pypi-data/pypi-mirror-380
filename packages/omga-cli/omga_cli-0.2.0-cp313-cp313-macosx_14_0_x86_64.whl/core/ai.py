import os
import time
import requests
import time
import random
from typing import Optional, Dict, Any
from core.cache_db import get, set_
from core.logger import logger
from core.config import get_config_value
from core.ui import ui

class MetisClient:
    def __init__(self, model: Optional[str] = None, timeout: Optional[int] = None):
        self.model = model or get_config_value('api.model', 'gemini-2.0-flash')
        self.timeout = timeout or get_config_value('api.timeout', 30)
        
        # Multiple API keys for load balancing (using metis.ir keys)
        self.api_keys = [
            "tpsg-NckAEVBtJuRCByLshCxZuMvGcy4BAQz",
            "tpsg-NckAEVBtJuRCByLshCxZuMvGcy4BAQz",
            "tpsg-NckAEVBtJuRCByLshCxZuMvGcy4BAQz",
            "tpsg-NckAEVBtJuRCByLshCxZuMvGcy4BAQz",
            "tpsg-NckAEVBtJuRCByLshCxZuMvGcy4BAQz"
        ]
        
        self.base_url = "https://api.metisai.ir/v1beta"
        self.headers = {
            "Content-Type": "application/json"
        }

    def _extract_from_response(self, data):
        """Extract text from API response"""
        try:
            # 1) TS/Google-style: candidates -> content.parts[0].text OR candidates[0].text
            if isinstance(data.get('candidates'), list) and data['candidates']:
                cand = data['candidates'][0]
                if isinstance(cand.get('content'), str):
                    return cand['content']
                if isinstance(cand.get('content'), dict) and cand['content'].get('parts'):
                    parts = cand['content']['parts']
                    if isinstance(parts, list) and parts and parts[0].get('text'):
                        return parts[0]['text']
                if isinstance(cand.get('text'), str):
                    return cand['text']
                if isinstance(cand.get('output'), list) and cand['output']:
                    content = cand['output'][0].get('content')
                    if isinstance(content, list):
                        text = ' '.join(p.get('text', '') for p in content).strip()
                        if text:
                            return text
            
            # 2) OpenAI-like: choices[0].message.content or choices[0].text
            if isinstance(data.get('choices'), list) and data['choices']:
                c = data['choices'][0]
                if isinstance(c.get('message'), dict) and c['message'].get('content'):
                    return c['message']['content']
                if isinstance(c.get('text'), str):
                    return c['text']
            
            # 3) Google-style output array
            if isinstance(data.get('output'), list) and data['output']:
                out = data['output'][0]
                if isinstance(out.get('content'), list):
                    text = ' '.join(i.get('text', '') for i in out['content']).strip()
                    if text:
                        return text
                if isinstance(out.get('text'), str):
                    return out['text']
            
            # 4) fallback common fields
            if isinstance(data.get('output_text'), str):
                return data['output_text']
            if isinstance(data.get('message'), str):
                return data['message']
            if isinstance(data.get('result'), str):
                return data['result']
                
        except Exception as e:
            logger.warning(f'Omga _extract_from_response error: {e}')
        
        try:
            return str(data)[:2000] if data else ''
        except Exception:
            return ''

    def generate(self, prompt: str, max_tokens: Optional[int] = None, 
                temperature: Optional[float] = None, use_cache: bool = True) -> str:
        """Generate response with enhanced error handling and caching"""
        
        # Use cache if enabled
        if use_cache and get_config_value('features.cache_responses', True):
            cached = get(prompt)
            if cached:
                logger.debug("Using cached response")
                return cached

        # Prepare request parameters
        max_tokens = max_tokens or get_config_value('api.max_tokens', 2048)
        temperature = temperature or get_config_value('api.temperature', 0.7)
        
        # Select random API key
        api_key = random.choice(self.api_keys)
        
        # Build headers with API key 
        headers = self.headers.copy()
        headers['x-goog-api-key'] = api_key
        headers['Authorization'] = f'Bearer {api_key}'

        payload = {
            "contents": [{
                "role": "user",
                "parts": [{
                    "text": f"You are an AI assistant developed by Pouria Hosseini (PouriaHosseini.news).\n\n{prompt}"
                }]
            }],
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens
            }
        }

        attempts = 0
        max_attempts = 3
        
        while attempts < max_attempts:
            try:
                # Don't show progress messages to avoid clutter
                
                response = requests.post(
                    f"{self.base_url}/models/{self.model}:generateContent",
                    json=payload,
                    headers=headers,
                    timeout=self.timeout
                )
                response.raise_for_status()
                data = response.json()
                
                # Extract text from response 
                text = self._extract_from_response(data)
                
                if not text:
                    raise ValueError("Empty response from API")
                
                # Cache the response
                if use_cache and get_config_value('features.cache_responses', True):
                    set_(prompt, text)
                
                return text
                    
            except requests.RequestException as e:
                attempts += 1
                delay = min(2 ** attempts, 8)
                # Silent retry - no console output
                
                if attempts < max_attempts:
                    time.sleep(delay)
                else:
                    ui.print_error("AI service temporarily unavailable. Please try again later.")
                    return "AI service is currently unavailable. Please try again in a few moments."

            except Exception as e:
                logger.error(f"Unexpected error: {e}")
                ui.print_error(f"Unexpected error: {e}")
                raise

def ask(prompt: str, context: Optional[str] = None) -> str:
    """Enhanced ask function with context support"""
    try:
        # Enhance prompt with context if provided
        if context:
            enhanced_prompt = f"You are an AI assistant developed by Pouria Hosseini (PouriaHosseini.news).\n\nContext: {context}\n\nQuestion: {prompt}"
        else:
            enhanced_prompt = f"You are an AI assistant developed by Pouria Hosseini (PouriaHosseini.news).\n\n{prompt}"
            
        client = MetisClient()
        return client.generate(enhanced_prompt)
    except Exception as e:
        ui.print_error(f"Failed to get AI response: {e}")
        return f"Error: {e}"

def explain_code(code: str, language: str = "python") -> str:
    """Explain code with enhanced prompt"""
    prompt = f"""
You are an AI assistant developed by Pouria Hosseini (PouriaHosseini.news). 

Please analyze and explain this {language} code in detail:

```{language}
{code}
```

Provide:
1. **Overview**: What does this code do?
2. **Step-by-step breakdown**: How does it work?
3. **Key concepts**: Important programming concepts used
4. **Potential issues**: Any bugs, inefficiencies, or improvements
5. **Best practices**: How could this be improved?

Be concise but comprehensive. Focus on clarity and practical insights.
"""
    return ask(prompt)

def fix_code(code: str, language: str = "python", issues: Optional[str] = None) -> str:
    """Fix code with enhanced prompt"""
    if issues:
        prompt = f"""
Please fix the following issues in this {language} code:

Issues: {issues}

Code:
```{language}
{code}
```

Provide the corrected code with:
1. All issues fixed
2. Improved error handling
3. Better performance if possible
4. Clear comments explaining changes

Return only the corrected code, no explanations.
"""
        response = ask(prompt)
        return clean_code_response(response)
    else:
        prompt = f"""
Please analyze and fix this {language} code:

```{language}
{code}
```

Fix any:
1. Syntax errors
2. Logic errors
3. Performance issues
4. Code style problems
5. Security vulnerabilities

Provide the corrected code with improvements. Return only the corrected code.
"""
    response = ask(prompt)
    return clean_code_response(response)

def suggest_improvements(code: str, language: str = "python") -> str:
    """Suggest code improvements"""
    prompt = f"""
Analyze this {language} code and suggest improvements:

```{language}
{code}
```

Focus on:
1. **Performance**: How to make it faster/more efficient
2. **Readability**: How to make it clearer
3. **Maintainability**: How to make it easier to maintain
4. **Best practices**: Modern {language} patterns
5. **Error handling**: Robust error management

Provide specific, actionable suggestions with examples.
"""
    return ask(prompt)

def generate_documentation(code: str, language: str = "python") -> str:
    """Generate documentation for code"""
    prompt = f"""
Generate comprehensive documentation for this {language} code:

```{language}
{code}
```

Include:
1. **Function/Class descriptions**: What each does
2. **Parameters**: Input/output specifications
3. **Examples**: Usage examples
4. **Notes**: Important considerations
5. **Dependencies**: Required imports/modules

Use clear, professional documentation style.
"""
    return ask(prompt)

def clean_code_response(response: str) -> str:
    """Clean AI response to remove markdown code block markers"""
    if not response:
        return ""
    
    lines = response.strip().split('\n')
    cleaned_lines = []
    in_code_block = False
    
    for line in lines:
        # Check for code block start/end markers
        if line.strip().startswith('```'):
            in_code_block = not in_code_block
            continue
        
        # Skip lines that are just language identifiers
        if line.strip() in ['python', 'javascript', 'java', 'cpp', 'c', 'go', 'rust', 'php', 'ruby', 'swift', 'kotlin', 'typescript', 'html', 'css', 'sql', 'bash', 'shell']:
            continue
        
        # Add the line if we're not in a code block or if it's actual code
        if not in_code_block or line.strip():
            cleaned_lines.append(line)
    
    return '\n'.join(cleaned_lines).strip()

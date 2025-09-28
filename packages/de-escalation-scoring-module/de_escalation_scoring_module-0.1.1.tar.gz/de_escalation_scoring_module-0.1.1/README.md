# DeEscalation Scoring Module

[![PyPI version](https://badge.fury.io/py/de-escalation-scoring-module.svg)](https://badge.fury.io/py/de-escalation-scoring-module)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A Python module for evaluating escalation and de-escalation patterns in chat conversations using AI-powered scoring. Perfect for customer service, community management, and conflict resolution applications.

## 🚀 Features

- **AI-Powered Scoring**: Analyze chat conversations for escalation levels (1-5 scale)
- **Flexible API Support**: Works with Poe API, OpenAI, or any OpenAI-compatible endpoint
- **Multiple Input Formats**: Handle string conversations or structured message arrays
- **Batch Processing**: Score multiple conversations efficiently
- **Robust JSON Parsing**: Automatic handling of LLM response parsing
- **Easy Integration**: Simple API for developers and non-technical users
- **Coaching Tips**: Get actionable suggestions for improving conversations

## 📦 Installation

```bash
pip install de-escalation-scoring-module
```

## 🔧 Quick Setup

### 1. Environment Variables (Recommended)
```bash
export POE_API_KEY="your_poe_api_key_here"
```

### 2. Or use API key directly in code
```python
from de_escalation_scoring import DeEscalationScorer

scorer = DeEscalationScorer(api_key="your_poe_api_key_here")
```

## 📚 Usage Examples

### Basic Usage
```python
from de_escalation_scoring import DeEscalationScorer, score_chat

# Using environment variable for API key
scorer = DeEscalationScorer()

# Score a simple message
result = scorer.score_conversation("Hello, how can I help you today?")
print(result)
# Output: {"score": 5, "reason": "Polite and helpful greeting", "coaching_tip": "Great start to build rapport"}

# Quick scoring function
result = score_chat("I'm really frustrated with this service!")
print(result)
# Output: {"score": 2, "reason": "Shows frustration and dissatisfaction", "coaching_tip": "Acknowledge the frustration and ask for specifics"}
```

### Advanced Usage with Custom API
```python
# Using OpenAI API instead of Poe
scorer = DeEscalationScorer(
    api_key="your_openai_api_key",
    base_url="https://api.openai.com/v1",
    model="gpt-4",
    system_prompt="Analyze conversations for de-escalation patterns and provide constructive feedback."
)

result = scorer.score_conversation("I understand your concern. Let me help you solve this.")
```

### Conversation Thread Scoring
```python
# Score a multi-message conversation
messages = [
    "This service is terrible!",
    "I'm sorry to hear about your experience. Can you tell me what specifically went wrong?",
    "Well, my order was delayed and nobody told me.",
    "I apologize for the delay and lack of communication. Let me check your order status right away."
]

result = scorer.score_message_thread(messages)
print(f"Score: {result['score']}/5")
print(f"Reason: {result['reason']}")
print(f"Tip: {result['coaching_tip']}")
```

### Batch Processing
```python
conversations = [
    "Thank you for your help!",
    "This is unacceptable!",
    "I appreciate your patience while we resolve this."
]

results = scorer.batch_score(conversations)
for i, result in enumerate(results):
    print(f"Conversation {i+1}: Score {result['score']}/5")
```

### Structured Message Format
```python
chat_history = [
    {"role": "user", "content": "I need help with my account"},
    {"role": "assistant", "content": "I'd be happy to help you with your account. What specific issue are you experiencing?"},
    {"role": "user", "content": "I can't log in and it's really frustrating"}
]

result = scorer.score_conversation(chat_history)
```

## 🎯 Use Cases

### Customer Service
- **Real-time monitoring** of support conversations
- **Quality assurance** for customer service representatives
- **Training feedback** for support teams
- **Escalation prediction** to prevent conflicts

### Community Management
- **Forum moderation** assistance
- **Social media monitoring** for brand reputation
- **Discord/Slack channel** health monitoring
- **Online community** wellness tracking

### Conflict Resolution
- **Mediation support** in dispute resolution
- **Communication coaching** for better outcomes
- **De-escalation training** programs
- **Workplace communication** improvement

## 📊 Scoring System

| Score | Level | Description | Example |
|-------|--------|-------------|---------|
| 1 | Highly Escalated | Aggressive, hostile, threatening | "This is ridiculous! I demand to speak to your manager now!" |
| 2 | Escalated | Frustrated, angry, demanding | "I'm really upset about this delay. This is unacceptable." |
| 3 | Neutral | Matter-of-fact, neither calm nor agitated | "I have a problem with my order. Can you help?" |
| 4 | Calm | Polite, patient, understanding | "I understand these things happen. How can we fix this?" |
| 5 | De-escalating | Actively calming, empathetic, solution-focused | "I appreciate your patience. Let me personally ensure this gets resolved." |

## 🔑 API Configuration

### Supported APIs

#### Poe API (Default)
```python
scorer = DeEscalationScorer(
    api_key="your_poe_api_key",
    base_url="https://api.poe.com/v1",
    model="DeEscalationScoring"
)
```

#### OpenAI
```python
scorer = DeEscalationScorer(
    api_key="your_openai_api_key",
    base_url="https://api.openai.com/v1",
    model="gpt-4"
)
```

#### Azure OpenAI
```python
scorer = DeEscalationScorer(
    api_key="your_azure_api_key",
    base_url="https://your-resource.openai.azure.com/",
    model="gpt-4"
)
```

#### Custom/Local APIs
```python
scorer = DeEscalationScorer(
    api_key="your_api_key",
    base_url="http://localhost:8000/v1",
    model="your-custom-model"
)
```

## 🛡️ Error Handling

```python
try:
    result = scorer.score_conversation("Hello world")
    print(f"Score: {result['score']}")
except ValueError as e:
    print(f"JSON parsing error: {e}")
except Exception as e:
    print(f"API error: {e}")
```

## 🔧 Integration Examples

### Flask Web Application
```python
from flask import Flask, request, jsonify
from de_escalation_scoring import DeEscalationScorer

app = Flask(__name__)
scorer = DeEscalationScorer()

@app.route('/score', methods=['POST'])
def score_conversation():
    data = request.json
    result = scorer.score_conversation(data['conversation'])
    return jsonify(result)
```

### Discord Bot
```python
import discord
from de_escalation_scoring import DeEscalationScorer

scorer = DeEscalationScorer()

@bot.event
async def on_message(message):
    if not message.author.bot:
        result = scorer.score_conversation(message.content)
        if result['score'] <= 2:
            # Alert moderators for potential escalation
            await message.channel.send("🤖 Escalation detected. Moderator notified.")
```

### Slack Integration
```python
from slack_sdk import WebClient
from de_escalation_scoring import DeEscalationScorer

scorer = DeEscalationScorer()

def handle_message(event):
    text = event['text']
    result = scorer.score_conversation(text)
    
    if result['score'] <= 2:
        # Send coaching tip to manager
        client.chat_postMessage(
            channel="manager-alerts",
            text=f"Escalation detected. Coaching tip: {result['coaching_tip']}"
        )
```

## 🤖 For Non-Technical Users

If you're not a developer, you can still use this module by:

1. **Hiring a developer** to integrate it into your existing systems
2. **Using AI coding assistants** like ChatGPT, Claude, or GitHub Copilot
3. **Consulting with a technical specialist** for custom integration

### Sample Request for Developers:
> "Please integrate the de-escalation-scoring-module into our customer service system. We need to monitor chat conversations and get alerts when escalation levels are high (score ≤ 2). The module is available on PyPI as 'de-escalation-scoring-module'."

## 📋 Requirements

- Python 3.10 or higher
- `openai` library for API communication
- `json-repair` library for robust JSON parsing
- Valid API key for your chosen AI service

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔄 Changelog

### v0.1.1
- Initial release
- Support for Poe API and OpenAI-compatible endpoints
- Batch processing capabilities
- Comprehensive error handling
- Multiple input format support

---

**Made with ❤️ in Hackathon [Hack the Divide](https://luma.com/dtcw176s)**

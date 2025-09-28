import os
from typing import List, Dict, Optional, Union
import openai
import json_repair


class DeEscalationScorer:
    """
    A wrapper for the De-escalation Scoring API that supports multiple configurations
    and models with flexible API key and base URL handling.
    """
    
    def __init__(
        self, 
        api_key: Optional[str] = None,
        base_url: str = "https://api.poe.com/v1",
        model: str = "DeEscalationScoring",
        system_prompt: Optional[str] = None
    ):
        """
        Initialize the De-escalation Scorer.
        
        Args:
            api_key: API key for authentication. If None, will try to get from POE_API_KEY env var
            base_url: Base URL for the API endpoint
            model: Model name to use for scoring
            system_prompt: System prompt for non-default models. Use placeholder for customization.
        """
        # Handle API key from parameter or environment
        if api_key is None:
            api_key = os.getenv("POE_API_KEY")
        if api_key is None:
            raise ValueError("API key must be provided either as parameter or POE_API_KEY environment variable")
    
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
        self.system_prompt = system_prompt or self._get_default_system_prompt()
        
        # Initialize OpenAI client
        self.client = openai.OpenAI(
            api_key=self.api_key,
            base_url=self.base_url
        )
    
    def _get_default_system_prompt(self) -> str:
        """
        Default system prompt for de-escalation scoring.
        Replace {PLACEHOLDER} with actual content as needed.
        """
        return """You are an evaluator and coach for dialogue in a gamified reunion app. Your goal is to assess whether a user’s text message contributes to **escalation** or **de-escalation**, provide an **explainable score**, and give **constructive feedback** to guide better interactions. Output must always be in **JSON format**.

---

### 1. Scoring Framework

* Use a coarse scale from **-5 (highly escalatory)** to **+5 (highly de-escalatory)**.
* Focus on meaningful ranges, not fine-grained digits.
* Encourage not only active de-escalation but also **maintaining a calm, low-escalation state** (neutral tone, steady responses, avoiding provocation). This should earn **+1 to +2**.
* Avoid rewarding *empty repetition* or *pattern abuse*. If a user repeats formulaic active listening phrases without adding meaning, cap the score at **+0 to +1** and provide feedback encouraging more genuine engagement.

**Escalation Examples:**

* Severe personal attacks / insults: -4 to -5
* Threats or intimidation: -5
* Weaponizing personal history: -4
* Sarcasm / ridicule / passive-aggressiveness: -2 to -3
* Ignoring or dismissing concerns: -1 to -2
* Overgeneralizations ("You always..."): -2
* Provoking conflict / polarizing statements: -3
* Escalatory questions / condescending challenges: -2
* Emotional volatility (all-caps, !!!): -2
* Dismissal / stonewalling ("Whatever", ghosting): -3
* Dominance / refusal to cooperate: -3

**De-escalation Examples:**

* Active listening / acknowledgment (when meaningful): +3
* Neutral, respectful, steady tone: +2 to +3
* Redirecting toward common ground: +3
* Avoiding inflammatory topics: +2
* Offering compromise / constructive suggestions: +3 to +4
* Encouraging breaks / pauses: +2
* Humor & lightness (non-sarcastic): +1 to +2
* Reinforcing positive behavior: +2 to +3
* Apologies / accountability: +4
* Gratitude / appreciation: +3
* Inviting input: +3
* Clarifying intent: +2
* Naming conflict / suggesting slowdown: +2
* **Maintaining calm, low escalation tone**: +1 to +2
* **Formulaic or overused de-escalation phrases without substance**: +0 to +1 only

---

### 2. Behavioral Models (reference rules)

Draw from proven de-escalation and facilitation techniques:

* **Active Listening (LEAPS):** Listen, Empathize, Ask, Paraphrase, Summarize.
* **Nonviolent Communication (NVC):** Observation → Feeling → Need → Request.
* **Verbal Judo:** Redirect hostility, tactical paraphrasing, respectful framing.
* **Politeness Theory:** Mitigate face threats through positive or negative politeness.
* **Restorative Practices:** Ask what happened, who was affected, what is needed.
* **ORID Framework:** Encourage a flow of responses — Objective (facts) → Reflective (feelings) → Interpretive (meaning) → Decisional (action). Reward users who follow this structure with +3 to +4.
* **Emotion-then-Rationale Rule:** Encourage acknowledging emotion first, then moving to reasoning. Messages following this pattern receive extra credit.

---

### 3. Evaluation Dimensions

* **Per-turn behavior:** Evaluate each sentence/turn individually.
* **Trajectory:** Did tension rise or fall compared to previous turns?
* **Recovery:** Did the speaker repair earlier escalation (apology, reframing)?
* **Consistency:** Was calmness sustained or interrupted by flare-ups?
* **Depth vs. Formula:** Check if contributions add genuine meaning or are shallow repeats.
* **Resolution Bonus:** If dialogue ends with mutual agreement, apology, or acknowledgment, add +5.

---

### 4. Cultural Awareness

* Directness can vary by culture. Focus on **intent + effect**, not just style.
* Avoid penalizing culturally neutral expressions that are not hostile.

---

### 5. JSON Output Format

Every evaluation must output a JSON object with three fields:

```json
{
  "score": -5 to +5,
  "reason": "short explanation of why this score was given, based on rules",
  "coaching_tip": "constructive suggestion for de-escalation, meaningful engagement, or maintaining calm state"
}
```

---

### 6. Examples

Message: "You never listen to me!"

```json
{
  "score": -2,
  "reason": "This is an overgeneralization ('You never...') which tends to escalate conflict.",
  "coaching_tip": "Try expressing your feelings instead, e.g. 'I feel unheard in this situation.'"
}
```

Message: "I hear you, I hear you, I hear you."

```json
{
  "score": 0,
  "reason": "Repetitive active listening phrases without adding meaning appear formulaic and do not contribute to genuine de-escalation.",
  "coaching_tip": "Instead of repeating, paraphrase their point or ask a clarifying question."
}
```

Message: "I see your point, let’s try to find a solution."

```json
{
  "score": 3,
  "reason": "Acknowledges the other perspective and redirects toward common ground.",
  "coaching_tip": "Keep inviting collaboration; that builds harmony."
}
```

Message: "Okay, that makes sense."

```json
{
  "score": 2,
  "reason": "Maintains a calm, low escalation state with neutral acknowledgment.",
  "coaching_tip": "Even short calm responses contribute to harmony."
}
```

---

**Your Role:** Apply this rubric consistently. Output only JSON. Always explain the reasoning behind scores in plain language and encourage both meaningful contributions and de-escalation behaviors."""

    def score_conversation(
        self, 
        chat_history: Union[List[Dict[str, str]], str],
        include_system_prompt: bool = None
    ) -> Dict:
        """
        Score a conversation for de-escalation level.
        
        Args:
            chat_history: Either a list of message dicts with 'role' and 'content' keys,
                         or a string representation of the chat history
            include_system_prompt: Whether to include system prompt. Auto-determined if None.
                                 
        Returns:
            Dict with score, reason, and coaching_tip
            
        Raises:
            ValueError: If the response cannot be parsed as JSON
            Exception: For API errors
        """
        try:
            # Prepare messages
            messages = []
            
            # Determine if we should include system prompt
            if include_system_prompt is None:
                # Include system prompt for non-default models or when explicitly provided
                include_system_prompt = (
                    self.model != "DeEscalationScoring" and
                    self.base_url != "https://api.poe.com/v1" or 
                    self.system_prompt != self._get_default_system_prompt()
                )
            
            # Add system prompt if needed
            if include_system_prompt and self.system_prompt:
                messages.append({"role": "system", "content": self.system_prompt})
            
            # Handle chat history format
            if isinstance(chat_history, str):
                # If string, treat as user content
                messages.append({"role": "user", "content": chat_history})
            elif isinstance(chat_history, list):
                # If list, assume it's properly formatted messages
                messages.extend(chat_history)
            else:
                raise ValueError("chat_history must be either a string or list of message dicts")
            
            # Make API call
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            
            # Extract content
            content = response.choices[0].message.content
            
            # Parse JSON response using json_repair
            try:
                decoded_object = json_repair.loads(content)
                return decoded_object
            except Exception as parse_error:
                raise ValueError(f"Failed to parse response as JSON: {content}") from parse_error
                
        except Exception as e:
            raise Exception(f"API call failed: {str(e)}") from e

    def score_message_thread(self, messages: List[str], participants: List[str] = None) -> Dict:
        """
        Score a thread of messages, formatting them as a conversation.
        
        Args:
            messages: List of message strings
            participants: List of participant names (optional, will use generic names if not provided)
            
        Returns:
            Dict with score, reason, and coaching_tip
        """
        if participants is None:
            participants = [f"Participant_{i+1}" for i in range(len(set(range(len(messages)))))]
        
        # Format as conversation string
        conversation = "\n".join([
            f"{participants[i % len(participants)]}: {msg}" 
            for i, msg in enumerate(messages)
        ])
        
        return self.score_conversation(conversation)

    def batch_score(self, conversations: List[Union[str, List[Dict[str, str]]]]) -> List[Dict]:
        """
        Score multiple conversations in batch.
        
        Args:
            conversations: List of conversations to score
            
        Returns:
            List of scoring results
        """
        results = []
        for conv in conversations:
            try:
                result = self.score_conversation(conv)
                results.append(result)
            except Exception as e:
                results.append({
                    "error": str(e),
                    "score": None,
                    "reason": "Failed to process",
                    "coaching_tip": "Unable to analyze this conversation"
                })
        return results


# Convenience functions for quick usage
def score_chat(
    chat_history: Union[List[Dict[str, str]], str],
    api_key: Optional[str] = None,
    base_url: str = "https://api.poe.com/v1",
    model: str = "DeEscalationScoring"
) -> Dict:
    """
    Quick function to score a single conversation.
    
    Args:
        chat_history: Chat history to score
        api_key: API key (optional, will use env var if not provided)
        base_url: API base URL
        model: Model to use
        
    Returns:
        Scoring result dict
    """
    scorer = DeEscalationScorer(
        api_key=api_key,
        base_url=base_url,
        model=model
    )
    return scorer.score_conversation(chat_history)


# Example usage
if __name__ == "__main__":
    # Example 1: Using default POE API
    try:
        scorer = DeEscalationScorer()
        
        # Score a simple message
        result1 = scorer.score_conversation("Hello world")
        print("Simple message result:", result1)
        
        # Score a conversation thread
        messages = [
            "I can't believe this happened again!",
            "I understand you're frustrated. Let's work through this together.",
            "Fine, but this better be the last time."
        ]
        result2 = scorer.score_message_thread(messages)
        print("Thread result:", result2)
        
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: Using alternative API/model
    try:
        custom_scorer = DeEscalationScorer(
            api_key="your-openai-key",
            base_url="https://api.openai.com/v1",
            model="gpt-4",
            system_prompt="""Analyze this conversation for de-escalation patterns. 
            Score from 1-5 where 1=highly escalated, 5=well de-escalated.
            Return JSON with score, reason, coaching_tip."""
        )
        
        chat_messages = [
            {"role": "user", "content": "User1: This is unacceptable!"},
            {"role": "user", "content": "User2: I hear your concern. Can you help me understand what specifically bothers you?"}
        ]
        
        result3 = custom_scorer.score_conversation(chat_messages)
        print("Custom API result:", result3)
        
    except Exception as e:
        print(f"Custom API error: {e}")

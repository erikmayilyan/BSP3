from unittest.mock import patch
from agents.response_generation_agent import generate_response

@patch("agents.response_generation_agent.ask_llm")
def test_llm_returns_text(mock_ask_llm):
  mock_ask_llm.return_value = "The Erasmus programme allows students to study abroad."

  result = generate_response(
    "How does Erasmus work?",
    {"categories": ["mobility"]}
  )

  assert result == "The Erasmus programme allows students to study abroad."

@patch("agents.response_generation_agent.ask_llm")
def test_llm_exception_uses_fallback(mock_ask_llm):
    mock_ask_llm.side_effect = Exception("Ollama is unavailable")

    result = generate_response(
        "How does Erasmus work?",
        {"categories": ["mobility"]}
    )

    assert result.startswith("To apply for the Erasmus programme")
    
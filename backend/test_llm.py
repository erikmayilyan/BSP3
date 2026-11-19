import llm
from unittest.mock import patch, Mock

@patch("llm.send_request")
def test_ollama_request(mock_send):
  mock_response = Mock()
  mock_response.json.return_value = {
    "response": "Hello from Ollama!"
  }
  mock_send.return_value = mock_response

  result = llm.ask_llm("Say hello")

  assert result == "Hello from Ollama!"

  mock_send.assert_called_once_with(
    llm.ollama_host + "/api/generate",
    {
      "model": llm.ollama_model,
      "prompt": "Say hello",
      "stream": False
    }
  )

@patch("llm.send_request")
def test_ollama_json_mode(mock_send):
    mock_response = Mock()
    mock_response.json.return_value = {
        "response": '{"category": "academic"}'
    }
    mock_send.return_value = mock_response

    result = llm.ask_llm("Classify this request", json_mode=True)

    assert result == {"category": "academic"}
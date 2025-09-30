# Extended A2A

Extended Agent-to-Agent communication library with reasoning and tools messages.

## Installation

```bash
pip install extended_a2a
```

## Usage

```python
from extended_a2a import (
    new_agent_reasoning_message,
    new_agent_tools_message,
    create_agent_tool
)

# Create reasoning message
msg = new_agent_reasoning_message("My analysis shows...")

# Create tools message
tool = create_agent_tool("search", {"query": "test"})
tools_msg = new_agent_tools_message([tool])
```

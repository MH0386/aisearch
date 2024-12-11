from phi.agent import Agent
from phi.model.groq import Groq
from phi.playground import Playground, serve_playground_app
from phi.storage.agent.sqlite import SqlAgentStorage
from phi.tools.duckduckgo import DuckDuckGo

agent = Agent(
    name="Llama3",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    storage=SqlAgentStorage(table_name="llama3", db_file="agents.db"),
    add_history_to_messages=True,
    tools=[DuckDuckGo()],
    markdown=True,
)

app = Playground(agents=[ agent]).get_app()

if __name__ == "__main__":
    serve_playground_app(app="playground:app", reload=True)

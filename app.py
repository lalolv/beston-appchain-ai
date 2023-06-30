from vvhan.horoscope import HoroscopeTool
from regular.weather import WeatherTool

from langchain.agents import AgentType, initialize_agent
from langchain.llms import AzureOpenAI
from langchain.tools import DuckDuckGoSearchRun, OpenWeatherMapQueryRun
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
import chainlit as cl

# The search tool has no async implementation, we fall back to sync
@cl.langchain_factory(use_async=False)
def load():
    # user session
    # user_env = cl.user_session.get("env")
    # user_env.get("OPENWEATHERMAP_API_KEY")
    # 大模型 max_tokens = 4096
    llm = AzureOpenAI(
        deployment_name="gpt-35",
        model_name="gpt-35-turbo",
        temperature=0,
        streaming=True,
        max_tokens=2048,
        max_retries=1,
        callbacks=[FinalStreamingStdOutCallbackHandler()])

    # Tools
    tools = [
        WeatherTool(), 
        HoroscopeTool(), DuckDuckGoSearchRun()]
    # Return the agent
    return initialize_agent(
        tools, llm, 
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True
    )

# @cl.langchain_run
# async def run(agent, input):
#     # Since the agent is sync, we need to make it async
#     res = await cl.make_async(agent.run)(input=[input])
#     print(res)
#     await cl.Message(content=res).send()

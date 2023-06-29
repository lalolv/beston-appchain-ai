from vvhan.horoscope import HoroscopeTool
from langchain.agents import AgentType, initialize_agent
from langchain.llms import AzureOpenAI
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
# from langchain.prompts import MessagesPlaceholder
# from langchain.memory import ConversationBufferMemory
import chainlit as cl


# The search tool has no async implementation, we fall back to sync
@cl.langchain_factory(use_async=False)
def load():
    # Adding in memory
    # chat_history = MessagesPlaceholder(variable_name="chat_history")
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    # 大模型 max_tokens = 4096
    llm = AzureOpenAI(
        deployment_name="gpt-35",
        model_name="gpt-35-turbo",
        temperature=0,
        streaming=True,
        max_tokens=1024,
        max_retries=1,
        callbacks=[FinalStreamingStdOutCallbackHandler()])

    tools = [HoroscopeTool()]
    return initialize_agent(
        tools, llm, 
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, 
        verbose=True, 
        # memory=memory, 
        # agent_kwargs = {
        #     "memory_prompts": [chat_history],
        #     "input_variables": ["input", "agent_scratchpad", "chat_history"]
        # }
    )
    # agent.run("处女座本周的爱情运势如何?")

# @cl.langchain_run
# async def run(agent, input):
#     # Since the agent is sync, we need to make it async
#     res = await cl.make_async(agent.run)(input=[input])
#     print(res)
#     await cl.Message(content=res).send()

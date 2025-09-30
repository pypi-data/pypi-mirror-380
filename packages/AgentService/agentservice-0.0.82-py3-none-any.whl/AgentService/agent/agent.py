import json

from loguru import logger
from uuid import uuid4
from openai import AsyncOpenAI
from openai.types.responses import ResponseFunctionToolCall, ResponseOutputMessage, ResponseOutputText

from AgentService.db import Db
from AgentService.dtypes.db import method as dmth
from AgentService.dtypes.chat import Chat, ChatStatus
from AgentService.dtypes.message import Message, MessageType, ToolAnswer, Tool
from AgentService.dtypes.storage import Storage, StorageItem
from AgentService.types.agent_tool import AgentTool
from AgentService.types.response import AgentResponse, AgentResponseType


class Agent:
    model: str = "gpt-4.1-nano"
    temperature: float = 1.0
    max_tokens: int = 2048
    top_p: float = 1.0

    instructions: str = "You are a helpful assistant"

    system_prompts: list[str] = []
    prompt: str = "{text}"

    is_one_shot: bool = False

    def __init__(
        self,
        openai_key: str,
        tools: list[AgentTool] = None,
    ):

        self.log = logger.bind(classname=self.__class__.__name__)

        self.db = Db()
        self.client = AsyncOpenAI(api_key=openai_key)

        self.tools = tools if tools else []
        self.tools_schema = [tool.to_schema for tool in self.tools]

        self.system_prompts = list(map(lambda x: x.replace("\t", ""), self.system_prompts))
        self.instructions = self.instructions.replace("\t", "")

        self.log.debug(f"Created gpt like tools -> {self.tools_schema}")

    async def __system_prompt(self, i: int, context: dict) -> str:
        return self.system_prompts[i].format(**context)

    async def __prompt(self, text: str, context: dict) -> str:
        return self.prompt.format(text=text, **context)

    async def __generate(self, chat: Chat) -> AgentResponse:
        chat.status = ChatStatus.generating
        await self.db.ex(dmth.UpdateOne(Chat, chat, to_update="status"))

        messages: list[Message] = await self.db.ex(dmth.GetMany(Message, chat_id=chat.id))
        gpt_messages = []
        for message in messages:
            data = message.gpt_dump

            if isinstance(data, list):
                for row in data:
                    gpt_messages.append(row)

            else:
                gpt_messages.append(data)

        tools_schema = self.tools_schema[:]

        storage_item: StorageItem = await self.db.ex(dmth.GetOne(StorageItem))
        if storage_item:
            storages: list[Storage] = await self.db.ex(dmth.GetMany(Storage))

            tools_schema.append(
                {
                    "type": "file_search",
                    "vector_store_ids": list(map(lambda x: x.id, storages))
                }
            )

        try:
            response = await self.client.responses.create(
                model=self.model,
                input=gpt_messages,
                instructions=self.instructions,
                temperature=self.temperature,
                max_output_tokens=self.max_tokens,
                top_p=self.top_p,
                tools=tools_schema,
                tool_choice="auto"
            )

        except Exception as err:
            self.log.debug(json.dumps(gpt_messages, indent=2, ensure_ascii=False))
            self.log.debug(json.dumps(tools_schema, indent=2, ensure_ascii=False))

            raise err

        responses = []
        for i in response.output:
            if i.__class__ not in [ResponseFunctionToolCall, ResponseOutputMessage]:
                self.log.warning(f"Unsupported response type -> {i.__class__}")
                continue

            responses.append(i)

        if len(responses) != 1:
            self.log.debug(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))
            raise TypeError(f"Got many response types in 1 output -> {responses}")

        if isinstance(responses[0], ResponseFunctionToolCall):
            return AgentResponse(
                type=AgentResponseType.tools,
                content=[
                    Tool(
                        id=i.call_id,
                        name=i.name,
                        arguments=i.arguments
                    )
                    for i in responses
                ]
            )

        elif isinstance(responses[0], ResponseOutputMessage):
            texts = []
            for i in responses:
                for j in i.content:
                    if j.__class__ not in [ResponseOutputText]:
                        self.log.warning(f"Unsupported content type -> {j.__class__}")
                        continue

                    texts.append(j.text)

            return AgentResponse(
                type=AgentResponseType.answer,
                content="\n\n".join(texts)
            )

        else:
            self.log.debug(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))
            raise TypeError(f"Unsupported response type -> {responses[0]}")

    async def generate(self, chat: Chat) -> AgentResponse:
        try:
            return await self.__generate(chat)

        except Exception as err:
            self.log.exception(err)

            return AgentResponse(
                type=AgentResponseType.answer,
                content=str(err)
            )

    async def get_chat(self, chat_id: str, context: dict = {}) -> Chat:
        chat: Chat = await self.db.ex(dmth.GetOne(
            Chat,
            chat_id=chat_id,
            status={
                "$in": [ChatStatus.created.value, ChatStatus.idle.value, ChatStatus.tools.value]
            }
        ))
        if not chat:
            chat = Chat(
                id=uuid4().hex,
                chat_id=chat_id,
                status=ChatStatus.created,
                data=context
            )
            await self.db.ex(dmth.AddOne(Chat, chat))

        system_message: Message = await self.db.ex(dmth.GetOne(Message, chat_id=chat.id, type=MessageType.system.value))
        if not system_message:
            messages = []

            for i in range(len(self.system_prompts)):
                system_message = Message(
                    id=uuid4().hex,
                    chat_id=chat.id,
                    text=await self.__system_prompt(i, context),
                    type=MessageType.system
                )
                messages.append(system_message)

            await self.db.ex(dmth.AddOne(Message, system_message))

        return chat

    async def proccess_answer(self, answer: AgentResponse, chat: Chat) -> AgentResponse:
        if answer.type == AgentResponseType.tools:
            bot_message = Message(
                id=uuid4().hex,
                chat_id=chat.id,
                type=MessageType.tools,
                tools=answer.content
            )
            chat.status = ChatStatus.tools

        elif answer.type == AgentResponseType.answer:
            bot_message = Message(
                id=uuid4().hex,
                chat_id=chat.id,
                type=MessageType.assistant,
                text=answer.content
            )
            chat.status = ChatStatus.finished if self.is_one_shot else ChatStatus.idle

        else:
            raise ValueError(f"wrong answer type got {answer.type}, expected {AgentResponseType} like")

        await self.db.ex(dmth.AddOne(Message, bot_message))
        await self.db.ex(dmth.UpdateOne(Chat, chat, to_update="status"))

        return answer

    async def skip_tools(self, chat) -> str:
        messages: list[Message] = await self.db.ex(dmth.GetMany(Message, chat_id=chat.id))
        last_message: Message = messages[-1]

        if not last_message.tools:
            chat.status = ChatStatus.idle
            await self.db.ex(dmth.UpdateOne(Chat, chat, to_update="status"))
            return chat

        new_messages = [
            Message(
                id=uuid4().hex,
                chat_id=chat.id,
                type=MessageType.tool_answer,
                tool_answer=ToolAnswer(
                    id=tool.id,
                    name=tool.name,
                    text="Tool call skipped."
                )
            )
            for tool in last_message.tools
        ] + [
            Message(
                id=uuid4().hex,
                chat_id=chat.id,
                type=MessageType.assistant,
                text="skip"
            )
        ]
        await self.db.ex(dmth.AddMany(Message, new_messages))

        return chat

    async def answer_text(self, chat_id: str, text: str, context: dict = {}) -> AgentResponse:
        chat = await self.get_chat(chat_id, context)
        if chat.status == ChatStatus.tools:
            chat = await self.skip_tools(chat)

        user_message = Message(
            id=uuid4().hex,
            chat_id=chat.id,
            text=await self.__prompt(text, context),
            type=MessageType.user
        )
        await self.db.ex(dmth.AddOne(Message, user_message))

        answer = await self.generate(chat=chat)
        await self.proccess_answer(answer, chat)

        return answer

    async def answer_tools(self, chat_id: str, tool_answers: list[ToolAnswer] = None) -> AgentResponse:
        chat = await self.get_chat(chat_id)

        if chat.status != ChatStatus.tools:
            return AgentResponse(type=AgentResponseType.answer, content="No tools to answer")

        new_messages = []
        for tool_answer in tool_answers:
            new_messages.append(Message(
                id=uuid4().hex,
                chat_id=chat.id,
                type=MessageType.tool_answer,
                tool_answer=tool_answer
            ))
        await self.db.ex(dmth.AddMany(Message, new_messages))

        answer = await self.generate(chat=chat)
        await self.proccess_answer(answer, chat)

        return answer

    async def answer(self, chat_id: str, text: str = None, context: dict = {}, tool_answers: list[ToolAnswer] = None) -> AgentResponse:
        self.log.debug(f"Answer: {chat_id = }, {text = }, {context = }, {tool_answers = }")

        if text:
            return await self.answer_text(chat_id, text, context)

        elif len(tool_answers):
            return await self.answer_tools(chat_id, tool_answers)

        else:
            raise ValueError("Need text or tool answers to answer")

    async def create_storage(self, key: str) -> Storage:
        from AgentService.config import Config

        vector_store = await self.client.vector_stores.create(name="@".join([Config().project_name, key]))
        self.log.info(f"Created storage -> {vector_store.id}")

        return Storage(
            id=vector_store.id,
            key=key
        )

    async def update_storage(self, data: str, storage_id: str):
        files = await self.client.vector_stores.files.list(vector_store_id=storage_id)
        for file in files.data:
            await self.client.vector_stores.files.delete(
                vector_store_id=storage_id,
                file_id=file.id
            )
            self.log.info(f"Removed file from storage -> {storage_id}@{file.id}")

        await self.client.vector_stores.file_batches.upload_and_poll(
            vector_store_id=storage_id,
            files=[("data.json", data)]
        )
        self.log.info(f"Added data to storage -> {storage_id}")

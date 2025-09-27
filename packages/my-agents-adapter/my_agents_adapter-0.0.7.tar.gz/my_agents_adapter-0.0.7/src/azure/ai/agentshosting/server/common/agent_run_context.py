# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------
from ...models import AgentId, CreateResponse, ResponseConversation1
from .id_generator.id_generator import IdGenerator


class AgentRunContext:
    def __init__(self, request: CreateResponse, id_generator: IdGenerator, response_id: str, conversation_id: str):
        self._request = request
        self._id_generator = id_generator
        self._response_id = response_id
        self._conversation_id = conversation_id

    @property
    def request(self) -> CreateResponse:
        return self._request

    @property
    def id_generator(self) -> IdGenerator:
        return self._id_generator

    @property
    def response_id(self) -> str:
        return self._response_id

    @property
    def conversation_id(self) -> str:
        return self._conversation_id

    def get_agent_id_object(self) -> AgentId:
        if not self.request.agent:
            return None
        return AgentId(
            {
                "type": self.request.agent.type,
                "name": self.request.agent.name,
                "version": self.request.agent.version,
            }
        )

    def get_conversation_object(self) -> ResponseConversation1:
        if not self._conversation_id:
            return None
        return ResponseConversation1(id=self._conversation_id)

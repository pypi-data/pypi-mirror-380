from typing import Any, Callable, Literal, List, Optional
from dataclasses import dataclass
import contextlib
from starlette.websockets import WebSocket
from starlette.exceptions import HTTPException
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.requests import Request
from starlette.routing import Route, WebSocketRoute
from pydantic import BaseModel, PrivateAttr
import uvicorn
import asyncio
from websockets.sync.client import connect as connect_websocket
from websockets.exceptions import InvalidStatus
import json
import time
import traceback
from .content import MarkdownMessage, StatusUpdate, BaseMessage
from syngular_ai.content import Input
import requests

class RemoteRequestInput(BaseModel):
    id: str
    name: str
    text: str | None = None
    file: str | None = None
    _file_content_fn: Optional[Callable[[], bytes]] = PrivateAttr(default=None)


    def get_file_content(self) -> Optional[bytes]:
        if self._file_content_fn is not None:
            return self._file_content_fn()
        return None
    
class WebsocketBackendResponse(BaseModel):
    type: Literal['backend.response'] = 'backend.response'
    request_msg_id: str
    thread_id: str
    content: Any

class RemoteRequestPayload(BaseModel):
    type: Literal['new_user_message']
    content: str
    inputs: List[RemoteRequestInput]


class RemoteRequest(BaseModel):
    thread_id: str
    request_msg_id: str
    entrypoint_name: str
    payload: RemoteRequestPayload

@dataclass
class Entrypoint:
    name: str
    inputs: List[Input] | None
    func: Callable

entrypoints: dict[str, Entrypoint] = {}
async_entrypoints: dict[str, Entrypoint] = {}

def validate_entrypoint(name: str, inputs: List[Input] | None):
    if not name.startswith('@'):
        raise ValueError('Name must start with @')
    
    if inputs is not None and isinstance(inputs, list):
        for input in inputs:
            if not isinstance(input, Input):
                raise ValueError('All inputs must be subclasses of Input')

def entrypoint(name: str, inputs: List[Input] | None = None):
    validate_entrypoint(name, inputs)
    def decorator(func):
        entrypoints[name] = Entrypoint(
            name=name, inputs=inputs, func=func
        )
        return func
    
    return decorator


def async_entrypoint(name: str, inputs: List[Input] | None = None):
    validate_entrypoint(name, inputs)
    
    def decorator(func):
        async_entrypoints[name] = Entrypoint(
            name=name, inputs=inputs, func=func)
        return func
    
    return decorator


def is_authorized(subprotocols: list[str]):
    # TODO: actually check auth
    if len(subprotocols) != 2:
        return False
    if subprotocols[0] != "Authorization":
        return False
    # Here we are hard coding the token, in a real application you would validate the token
    # against a database or an external service.
    if subprotocols[1] != "token":
        # TODO: actually check the token
        return True
    return True


async def handle_async_request(msg, on_chunk):
    payload = msg["payload"]
    content = payload["content"]
    entrypoint = msg["entrypoint_name"]

    async for result in async_entrypoints[entrypoint].func(content):
        loop = asyncio.get_event_loop()
        # Use the event loop to run the on_chunk callback
        await loop.run_in_executor(None, on_chunk, result)


def handle_request(msg, on_chunk, api_url=None, api_key=None):
    payload = msg.payload
    content = payload.content
    entrypoint = msg.entrypoint_name
    inputs = payload.inputs if payload.inputs else []
    
    for input in inputs:
        if input.file is not None:
            if api_url is None or api_key is None:
                raise ValueError("API URL and API key must be provided to obtain file inputs")
            input._file_content_fn = lambda: get_file_for_input(api_url, api_key, input.id)
    
    if entrypoint in entrypoints:
        if inputs:
            results =  entrypoints[entrypoint].func(content, inputs)
        else:
            results =  entrypoints[entrypoint].func(content)
        for result in results:
            on_chunk(result)
        return
    
    if entrypoint in async_entrypoints:
        asyncio.run(handle_async_request(msg, on_chunk))

def handle_http_request(websocket: WebSocket, api_key: str):
    subprotocols = websocket.scope["subprotocols"]

    if not is_authorized(subprotocols):
        raise HTTPException(status_code=401, detail="Unauthorized")

    websocket.accept("Authorization")

    try:
        raw_msg = websocket.receive_json(mode="text")
        msg = RemoteRequest(**raw_msg)

        content = msg.payload.content
        entrypoint = msg.entrypoint
        thread_id = msg.thread_id

        if entrypoint not in entrypoints and entrypoint not in async_entrypoints:
            print(f"Entrypoint {entrypoint} not found")
            return

        def on_chunk(chunk, grouping_key):
            message = WebsocketBackendResponse(
                grouping_key=grouping_key,
                content=user_response_to_dict(chunk),
                thread_id=thread_id,
            )

            websocket.send_json(message.dict())

        handle_request(msg, on_chunk, api_key=api_key)
        
    finally:
        websocket.close()


def get_entrypoints():

    return [
        {
            'name': entrypoint.name,
            'inputs': [inp.model_dump() for inp in entrypoint.inputs] if entrypoint.inputs else None,
        }
        for entrypoint in list(entrypoints.values()) + list(async_entrypoints.values())
    ]


async def list_entrypoints(request: Request):
    return JSONResponse(get_entrypoints())


def listen(api_key: str, port: int, host: str):
    routes = [
        WebSocketRoute('/ws/entrypoint', endpoint=handle_http_request),
        Route('/api/entrypoints', endpoint=list_entrypoints, methods=['GET']),
    ]

    app = Starlette(routes=routes)

    uvicorn.run(app, host=host, port=port)

def dev_listen(api_key: str, api_url='wss://syngularai.com'):
    url = f'{api_url}/ws/dev-backend-handler/'
    headers = {
        "X-syngular-api-key": api_key,
    }

    while True:
        try:
            with connect_websocket(url, additional_headers=headers, subprotocols=["Authorization", "token"]) as agent_websocket:
                print("Connected.")

                # send the entrypoints
                agent_websocket.send(json.dumps({
                    "type": "backend.register",
                    "entrypoints": get_entrypoints(),
                }))


                for msg in agent_websocket:
                    raw_msg = json.loads(msg)
                    msg = RemoteRequest(**raw_msg)
                    
                    print("Received message: ", msg)

                    entrypoint_name = msg.entrypoint_name
                    content = msg.payload.content
                    thread_id = msg.thread_id

                    print("Received message for entrypoint: ", entrypoint_name)


                    try:
                        def on_chunk(chunk):
                            message = WebsocketBackendResponse(
                                type="backend.response",
                                thread_id=thread_id,
                                request_msg_id=msg.request_msg_id,
                                content=user_response_to_dict(chunk),
                            )

                            agent_websocket.send(message.json())

                        handle_request(msg, on_chunk, api_url=api_url, api_key=api_key)

                        agent_websocket.send(json.dumps({
                            "type": "backend.response_complete",
                            "thread_id": thread_id,
                            "request_msg_id": msg.request_msg_id,
                        }))
                    except Exception as e:
                        tb = traceback.format_exc()
                        print("Error handling message: ", e, tb)
                        agent_websocket.send(json.dumps({
                            "type": "backend.response_error",
                            "thread_id": thread_id,
                            "request_msg_id": msg.request_msg_id,
                            "error": tb,
                        }))

        except InvalidStatus as e:
            if e.response.status_code == 403:
                print("Invalid API key. Exiting...")
                return
            raise e
        except Exception as e:
            print("Error: ", e)
            print("Retrying in 1 second...")
            time.sleep(1)


def user_response_to_dict(response):
    if isinstance(response, BaseMessage):
        return response.dict()
    elif isinstance(response, StatusUpdate):
        return response.dict()
    elif isinstance(response, str):
        return MarkdownMessage(content=response).dict()

    raise ValueError(f"Unsupported response type: {type(response)}")


def get_file_for_input(api_url, api_key, input_id):
    protocol, rest = api_url.split("://", 1)
    
    if protocol == 'wss':
        protocol = 'https'
    elif protocol == 'ws':
        protocol = 'http'
    else:
        raise ValueError(f"Unsupported protocol: {protocol}")
    
    response =  requests.get(
        f'{protocol}://{rest}/api/inputs/{input_id}/file', 
        headers={
            "X-syngular-api-key": api_key
    })
    response.raise_for_status()
    return response.content
import uuid

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel, Field

import agent

app = FastAPI(title="Opti support agent")
sessions: dict[str, dict] = {}  # прототип сесії в пам'яті


class ChatIn(BaseModel):
    session_id: str | None = None
    message: str = Field(min_length=1, max_length=2000)


@app.get("/", include_in_schema=False)
def index():
    return FileResponse("index.html")  # проста сторінка чату


@app.post("/chat")
def chat(body: ChatIn):
    sid = body.session_id if body.session_id in sessions else uuid.uuid4().hex[:12]
    session = sessions.setdefault(sid, agent.new_session())
    try:
        reply = agent.handle(session, body.message.strip())
    except RuntimeError as e:  # немає ключа
        raise HTTPException(503, str(e))
    return {"session_id": sid, "reply": reply, "collected": session["fields"], "tickets": session["tickets"]}

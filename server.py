import asyncio
import os
import subprocess
import sys
from pathlib import Path

import httpx
import websockets
from fastapi import FastAPI, Request, Response, WebSocket
from fastapi.responses import FileResponse


ROOT = Path(__file__).parent
STREAMLIT_PORT = int(os.environ.get("STREAMLIT_INTERNAL_PORT", "8502"))
STREAMLIT_URL = f"http://127.0.0.1:{STREAMLIT_PORT}"
STREAMLIT_WS_URL = f"ws://127.0.0.1:{STREAMLIT_PORT}"

app = FastAPI()
streamlit_process = None


def start_streamlit():
    global streamlit_process
    if streamlit_process and streamlit_process.poll() is None:
        return

    cmd = [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        str(ROOT / "app.py"),
        "--server.headless=true",
        f"--server.port={STREAMLIT_PORT}",
        "--server.address=127.0.0.1",
        "--server.enableCORS=false",
        "--server.enableXsrfProtection=false",
    ]
    streamlit_process = subprocess.Popen(cmd, cwd=str(ROOT))


@app.on_event("startup")
async def startup():
    start_streamlit()
    async with httpx.AsyncClient(timeout=1.5) as client:
        for _ in range(60):
            try:
                response = await client.get(STREAMLIT_URL)
                if response.status_code < 500:
                    return
            except Exception:
                pass
            await asyncio.sleep(0.5)


@app.on_event("shutdown")
async def shutdown():
    if streamlit_process and streamlit_process.poll() is None:
        streamlit_process.terminate()


@app.get("/reminder-sw.js")
async def reminder_service_worker():
    return FileResponse(
        ROOT / "static" / "reminder-sw.js",
        media_type="application/javascript",
        headers={
            "Cache-Control": "no-cache, no-store, must-revalidate",
            "Service-Worker-Allowed": "/",
        },
    )


@app.api_route("/{path:path}", methods=["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", "HEAD"])
async def proxy_http(path: str, request: Request):
    start_streamlit()
    target = f"{STREAMLIT_URL}/{path}"
    if request.url.query:
        target = f"{target}?{request.url.query}"

    headers = {
        key: value
        for key, value in request.headers.items()
        if key.lower() not in {"host", "content-length"}
    }
    body = await request.body()

    async with httpx.AsyncClient(follow_redirects=False, timeout=None) as client:
        upstream = await client.request(
            request.method,
            target,
            headers=headers,
            content=body,
        )

    excluded = {"content-encoding", "content-length", "transfer-encoding", "connection"}
    response_headers = {
        key: value
        for key, value in upstream.headers.items()
        if key.lower() not in excluded
    }
    return Response(
        content=upstream.content,
        status_code=upstream.status_code,
        headers=response_headers,
        media_type=upstream.headers.get("content-type"),
    )


@app.websocket("/{path:path}")
async def proxy_websocket(websocket: WebSocket, path: str):
    start_streamlit()
    await websocket.accept()

    query = websocket.url.query
    target = f"{STREAMLIT_WS_URL}/{path}"
    if query:
        target = f"{target}?{query}"

    async with websockets.connect(target) as upstream:
        async def client_to_upstream():
            while True:
                message = await websocket.receive()
                if "text" in message:
                    await upstream.send(message["text"])
                elif "bytes" in message:
                    await upstream.send(message["bytes"])
                elif message.get("type") == "websocket.disconnect":
                    await upstream.close()
                    break

        async def upstream_to_client():
            async for message in upstream:
                if isinstance(message, bytes):
                    await websocket.send_bytes(message)
                else:
                    await websocket.send_text(message)

        await asyncio.gather(client_to_upstream(), upstream_to_client())

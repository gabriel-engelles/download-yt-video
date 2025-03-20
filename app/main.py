from fastapi import FastAPI
from fastapi.responses import FileResponse
from app.pytube_handler import baixar_video

app = FastAPI()

@app.get("/baixar_video/")
def baixar_video_api(url: str):
    file_path = baixar_video(url)

    if isinstance(file_path, str) and "erro" in file_path.lower():
        return {"status": "erro", "mensagem": file_path}

    return FileResponse(file_path, media_type="video/mp4", filename=file_path.split('/')[-1])

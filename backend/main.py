from fastapi import FastAPI, File, UploadFile, Query
from fastapi.responses import JSONResponse

app = FastAPI()


@app.post("/upload/")
async def upload_video(file: UploadFile = File(...), query: str = Query(...)):
    # Process video file (if needed)
    file_content = await file.read()
    file_size = len(file_content)  # Example: Get file size

    # Example response
    return JSONResponse(
        content={
            "message": f"Received file {file.filename} ({file_size} bytes) with query '{query}'"
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

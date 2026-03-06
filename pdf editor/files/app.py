from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
import io, os, uuid, base64
from typing import Optional
from pathlib import Path

app = FastAPI(title="PDF Studio")

UPLOAD_FOLDER = Path("uploads")
OUTPUT_FOLDER = Path("outputs")
UPLOAD_FOLDER.mkdir(exist_ok=True)
OUTPUT_FOLDER.mkdir(exist_ok=True)

sessions: dict = {}


@app.get("/", response_class=HTMLResponse)
async def index():
    html_path = Path("templates/index.html")
    return HTMLResponse(content=html_path.read_text(encoding="utf-8"))


class TextAnnotation(BaseModel):
    session_id: str
    page: int
    x: float
    y: float
    text: str
    color: str = "#000000"
    font_size: float = 14
    font: str = "Helvetica"

class HighlightAnnotation(BaseModel):
    session_id: str
    page: int
    x: float
    y: float
    width: float
    height: float
    color: str = "#FFFF00"

class UpdateAnnotation(BaseModel):
    session_id: str
    index: int
    x: Optional[float] = None
    y: Optional[float] = None
    text: Optional[str] = None

class RemoveAnnotation(BaseModel):
    session_id: str
    index: int

class RotatePage(BaseModel):
    session_id: str
    page: int
    angle: int = 90

class ExportRequest(BaseModel):
    session_id: str
    password: str = ""


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(400, "Only PDF files supported")
    session_id = str(uuid.uuid4())
    filepath = UPLOAD_FOLDER / f"{session_id}.pdf"
    content = await file.read()
    filepath.write_bytes(content)
    reader = PdfReader(str(filepath))
    pages_info = []
    for i, page in enumerate(reader.pages):
        box = page.mediabox
        pages_info.append({"page": i+1, "width": float(box.width), "height": float(box.height)})
    sessions[session_id] = {"original_path": str(filepath), "annotations": []}
    pdf_b64 = base64.b64encode(content).decode("utf-8")
    return {"session_id": session_id, "num_pages": len(reader.pages), "pages_info": pages_info, "pdf_data": pdf_b64}


@app.post("/add_text")
async def add_text(ann: TextAnnotation):
    if ann.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    idx = len(sessions[ann.session_id]["annotations"])
    sessions[ann.session_id]["annotations"].append({
        "type": "text", "page": ann.page, "x": ann.x, "y": ann.y,
        "text": ann.text, "color": ann.color, "font_size": ann.font_size, "font": ann.font
    })
    return {"success": True, "index": idx}


@app.post("/add_highlight")
async def add_highlight(ann: HighlightAnnotation):
    if ann.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    sessions[ann.session_id]["annotations"].append({
        "type": "highlight", "page": ann.page,
        "x": ann.x, "y": ann.y, "width": ann.width, "height": ann.height, "color": ann.color
    })
    return {"success": True}


@app.post("/update_annotation")
async def update_annotation(data: UpdateAnnotation):
    if data.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    anns = sessions[data.session_id]["annotations"]
    if data.index < 0 or data.index >= len(anns):
        raise HTTPException(400, "Invalid index")
    ann = anns[data.index]
    if data.x is not None: ann["x"] = data.x
    if data.y is not None: ann["y"] = data.y
    if data.text is not None: ann["text"] = data.text
    return {"success": True}


@app.post("/remove_annotation")
async def remove_annotation(data: RemoveAnnotation):
    if data.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    anns = sessions[data.session_id]["annotations"]
    if 0 <= data.index < len(anns):
        anns.pop(data.index)
    return {"success": True}


@app.get("/get_annotations")
async def get_annotations(session_id: str):
    if session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    return {"annotations": sessions[session_id]["annotations"]}


@app.post("/rotate_page")
async def rotate_page(data: RotatePage):
    if data.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    reader = PdfReader(sessions[data.session_id]["original_path"])
    writer = PdfWriter()
    for i, page in enumerate(reader.pages):
        if i == data.page - 1:
            page.rotate(data.angle)
        writer.add_page(page)
    rotated_path = UPLOAD_FOLDER / f"{data.session_id}_rotated.pdf"
    with open(rotated_path, "wb") as f:
        writer.write(f)
    sessions[data.session_id]["original_path"] = str(rotated_path)
    pdf_b64 = base64.b64encode(rotated_path.read_bytes()).decode("utf-8")
    return {"success": True, "pdf_data": pdf_b64}


@app.post("/export")
async def export_pdf(data: ExportRequest):
    if data.session_id not in sessions:
        raise HTTPException(400, "Invalid session")
    session = sessions[data.session_id]
    reader = PdfReader(session["original_path"])
    writer = PdfWriter()
    by_page: dict = {}
    for ann in session["annotations"]:
        by_page.setdefault(ann["page"], []).append(ann)
    for i, page in enumerate(reader.pages):
        pg = i + 1
        if pg in by_page:
            box = page.mediabox
            pw, ph = float(box.width), float(box.height)
            packet = io.BytesIO()
            c = canvas.Canvas(packet, pagesize=(pw, ph))
            for ann in by_page[pg]:
                if ann["type"] == "text":
                    c.setFillColor(HexColor(ann["color"]))
                    c.setFont(ann.get("font", "Helvetica"), ann.get("font_size", 14))
                    c.drawString(ann["x"], ann["y"], ann["text"])
                elif ann["type"] == "highlight":
                    c.setFillColor(HexColor(ann["color"]), alpha=0.35)
                    c.rect(ann["x"], ann["y"], ann["width"], ann["height"], fill=1, stroke=0)
            c.save()
            packet.seek(0)
            overlay = PdfReader(packet).pages[0]
            page.merge_page(overlay)
        writer.add_page(page)
    if data.password:
        writer.encrypt(data.password)
    out_path = OUTPUT_FOLDER / f"{data.session_id}_final.pdf"
    with open(out_path, "wb") as f:
        writer.write(f)
    return FileResponse(str(out_path), media_type="application/pdf", filename="edited_document.pdf")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)

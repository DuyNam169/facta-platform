from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from typing import Dict, Any

from app.schemas.detection import DetectionRequest, DetectionResponse
from app.services.detection_service import DetectionService
from app.core.dependencies import get_detection_service
from app.core.security import verify_api_key

router = APIRouter()

@router.post(
    "/detect/image",
    response_model=DetectionResponse,
    summary="Detect AI-generated or manipulated image"
)
async def detect_image(
    file: UploadFile = File(...),
    detection_service: DetectionService = Depends(get_detection_service),
    api_key: str = Depends(verify_api_key)
) -> DetectionResponse:
    """
    Analyze an image to detect if it's AI-generated or manipulated.
    
    - **file**: Image file (JPEG, PNG, WebP)
    - Returns: Detection result with confidence score
    """
    try:
        result = await detection_service.detect_image(file)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post(
    "/detect/text",
    response_model=DetectionResponse,
    summary="Detect AI-generated text"
)
async def detect_text(
    request: DetectionRequest,
    detection_service: DetectionService = Depends(get_detection_service),
    api_key: str = Depends(verify_api_key)
) -> DetectionResponse:
    """
    Analyze text to detect if it's AI-generated (GPT, etc.)
    
    - **text**: Text content to analyze
    - Returns: Detection result with confidence score
    """
    try:
        result = await detection_service.detect_text(request.text)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
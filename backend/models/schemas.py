from pydantic import BaseModel

class StartCallRequest(BaseModel):
    driver_name: str
    driver_phone: str
    load_number: str
    config_id: str

class WebhookPayload(BaseModel):
    call_id: str
    transcript: str

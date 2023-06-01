from pydantic import BaseModel, Field

class informationSchema(BaseModel):
    tanaman: str = Field(...)
    penyakit: str = Field(...)
    deskripsi: str = Field(...)
    solusi: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "tanaman":"rice",
                "penyakit":"yellowish",
                "deskripsi":"penyakit ini disebabkan oleh keamrau panjang",
                "solusi":"penggunaan pupuk dan saluran irigasi yang baik"
            }
        }
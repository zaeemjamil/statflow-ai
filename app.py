from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
import io

app = FastAPI(
    title="StatFlow AI",
    description="Automated statistical analysis API",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "app": "StatFlow AI",
        "status": "online",
        "message": "Statistical analysis API is running"
    }


@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Please upload a CSV file."
        )

    contents = await file.read()

    try:
        df = pd.read_csv(io.BytesIO(contents))
    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Could not read CSV file: {str(e)}"
        )

    missing_values = df.isnull().sum()

    return {
        "file_name": file.filename,
        "rows": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "column_names": df.columns.tolist(),
        "data_types": {
            column: str(dtype)
            for column, dtype in df.dtypes.items()
        },
        "missing_values": {
            column: int(value)
            for column, value in missing_values.items()
            if value > 0
        },
        "numeric_columns": df.select_dtypes(
            include="number"
        ).columns.tolist(),
        "categorical_columns": df.select_dtypes(
            include=["object", "category"]
        ).columns.tolist()
    }

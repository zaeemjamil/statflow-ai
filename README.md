# StatFlow AI

## Automated Statistical & Machine Learning Analysis

StatFlow AI is an automated statistical analysis workflow that transforms an uploaded dataset into a structured analytical report, AI-generated business insights, a professionally formatted PDF report, and a shareable Google Drive link.

The current implementation is built with:

- **n8n** for workflow automation
- **Python Native Code** for statistical calculations and machine learning
- **OpenRouter** for AI-powered interpretation
- **HTML/CSS** for report design
- **PDFPipe** for PDF generation
- **Google Drive** for report storage and sharing

---

## Demo Output

The published version produces a 4-page statistical and machine-learning report containing:

- Executive Summary
- Descriptive Statistical Findings
- Correlation Analysis
- Business Insights
- Risk Analysis
- Data-Driven Recommendations
- Multiple Linear Regression Evaluation
- Professional PDF Report
- Shareable Google Drive Link

### Sample Results

| Metric | Result |
|---|---:|
| Clean Observations | 238 |
| Training Observations | 190 |
| Testing Observations | 48 |
| R² | 0.1986 |
| MAE | 999.97 |
| RMSE | 1308.62 |
| Average Profit | -401.50 |

---

## Features

### Automated Dataset Upload

Users upload a structured dataset through an n8n Form.

### Data Preparation

The workflow performs basic preprocessing including:

- Duplicate detection
- Missing-value filtering
- Numeric data preparation
- Removal of rows that fail required analysis conditions

### Statistical Analysis

The current Python layer calculates:

- Count
- Mean
- Median
- Standard Deviation
- Minimum
- Maximum
- Correlations

### Correlation Analysis

The published sample identifies the following relationships:

| Variable Pair | Correlation |
|---|---:|
| Unit Price vs Revenue | 0.69 |
| Units Sold vs Revenue | 0.504 |
| Revenue vs Profit | 0.438 |
| Advertising Spend vs Profit | -0.37 |
| Unit Price vs Profit | 0.329 |
| Discount vs Revenue | -0.108 |

### Machine Learning

The current version implements **Multiple Linear Regression** using custom Python matrix operations.

The workflow includes:

- 80/20 train-test split
- Regression coefficients
- Intercept
- Predictions
- MAE
- RMSE
- R²
- Sample predictions

The current implementation does not use scikit-learn.

### AI-Powered Interpretation

OpenRouter AI receives the calculated statistical and machine-learning results and generates:

- Key Findings
- Strongest Correlations
- Business Insights
- Risks
- Recommendations
- Bottom Line

The AI is instructed to use only the supplied analytical results and avoid inventing numerical values.

### Professional PDF Reporting

The workflow converts the AI analysis into a styled HTML report and generates a PDF using PDFPipe.

The report includes:

- Branded cover
- Executive summary
- KPI cards
- Statistical findings
- Correlation tables
- Business insights
- Risks
- Recommendations
- Final business conclusion

### Google Drive Delivery

After PDF generation:

1. The PDF is uploaded to Google Drive.
2. The file is given viewer access through link sharing.
3. A shareable Google Drive URL is generated.
4. The final form displays the report link to the user.

---

## System Architecture

```text
User
  │
  ▼
n8n Form Trigger
  │
  ▼
Extract Dataset
  │
  ▼
Remove Duplicates
  │
  ▼
Filter / Data Quality
  │
  ├──────────────────┐
  ▼                  ▼
Statistical        Machine
Analysis           Learning
  │                  │
  └────────┬─────────┘
           ▼
         Merge
           │
           ▼
      OpenRouter AI
           │
           ▼
    Python Final Report
           │
           ▼
   Format Report for PDF
           │
           ▼
 Generate HTML Template
           │
           ▼
        PDFPipe
           │
           ▼
     Google Drive
           │
           ▼
       Share File
           │
           ▼
    Create PDF Link
           │
           ▼
     Final Form Result

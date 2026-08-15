# StatFlow AI

## Automated Statistical & Machine Learning Analysis

StatFlow AI is an automated statistical analysis workflow that transforms an uploaded dataset into a structured analytical report, AI-generated business insights, a professionally formatted PDF report, and a shareable Google Drive link.

The current implementation is built around **n8n workflow automation**, **custom Python statistical calculations**, **OpenRouter AI**, **PDFPipe**, and **Google Drive**.

---

## Demo Output

The current published version produces a 4-page statistical and machine-learning report containing:

- Executive summary
- Descriptive statistical findings
- Correlation analysis
- Business insights
- Risk analysis
- Data-driven recommendations
- Multiple Linear Regression evaluation
- PDF report generation
- Shareable Google Drive link

### Current sample report

The published sample uses a retail-sales dataset with **238 clean observations**.

Key reported model results:

| Metric | Result |
|---|---:|
| Clean observations | 238 |
| Training observations | 190 |
| Testing observations | 48 |
| R² | 0.1986 |
| MAE | 999.97 |
| RMSE | 1308.62 |
| Average Profit | -401.50 |

---

# Features

## Automated Dataset Upload

Users upload a dataset through an n8n Form.

The current implementation is designed around structured tabular data such as CSV datasets.

## Data Cleaning

The workflow performs basic preprocessing including:

- Duplicate detection
- Missing-value filtering
- Numeric data extraction
- Removal of rows failing required analysis conditions

## Statistical Analysis

The current Python analysis layer calculates:

- Count
- Mean
- Median
- Standard deviation
- Minimum
- Maximum
- Pearson-style correlations

The current implementation performs these calculations using custom Python logic rather than external statistical libraries.

## Correlation Analysis

The workflow calculates relationships between selected numerical variables and sends the results to the AI interpretation layer.

The published sample report identifies:

- Unit Price vs Revenue: 0.69
- Units Sold vs Revenue: 0.504
- Revenue vs Profit: 0.438
- Advertising Spend vs Profit: -0.37
- Unit Price vs Profit: 0.329
- Discount vs Revenue: -0.108

## Machine Learning

The current version implements **Multiple Linear Regression** using custom Python matrix operations.

The implementation includes:

- 80/20 train-test split
- Regression coefficients
- Intercept
- Predictions
- MAE
- RMSE
- R²
- Sample predictions

The current regression implementation is written manually and does not depend on scikit-learn.

## AI-Powered Interpretation

Statistical and machine-learning results are passed to an OpenRouter-hosted language model.

The AI is instructed to:

- Use only the supplied analytical results
- Avoid inventing numerical values
- Identify important findings
- Explain business implications
- Highlight risks
- Provide recommendations

## Professional PDF Report

The report is converted into a styled HTML document and then generated as PDF using PDFPipe.

The report contains:

- Branded cover section
- Executive summary
- KPI cards
- Statistical findings
- Correlation tables
- Business insights
- Risks
- Recommendations
- Final business conclusion

## Google Drive Delivery

After PDF generation:

1. The PDF is uploaded to Google Drive.
2. The file is shared using "Anyone with the link" viewer permission.
3. A shareable Google Drive URL is generated.
4. The final form displays the report link to the user.

---

# System Architecture

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
  ├───────────────┐
  ▼               ▼
Statistical     Machine
Analysis        Learning
  │               │
  └───────┬───────┘
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

    # StatFlow AI

## Automated Statistical & Machine Learning Analysis

StatFlow AI is an automated data-analysis workflow built with n8n, Python, OpenRouter AI, PDFPipe, and Google Drive.

The system accepts a structured dataset, performs statistical analysis and multiple linear regression, generates AI-powered business insights, creates a professional PDF report, and returns a shareable Google Drive link.

## Workflow

Dataset Upload  
↓  
Data Extraction & Cleaning  
↓  
Statistical Analysis  
↓  
Multiple Linear Regression  
↓  
OpenRouter AI Analysis  
↓  
HTML Report  
↓  
PDF Generation  
↓  
Google Drive Upload  
↓  
Shareable PDF Link

## Current Features

- Dataset upload through n8n Form
- Duplicate removal and basic data filtering
- Descriptive statistics
- Correlation analysis
- Multiple Linear Regression
- MAE, RMSE and R² evaluation
- AI-generated findings, risks and recommendations
- Professional HTML/PDF report
- Google Drive upload and sharing
- Automatic PDF link delivery

## Technology Stack

- n8n
- Python Native Code
- OpenRouter
- HTML/CSS
- PDFPipe
- Google Drive

## Sample Results

The published sample report contains:

| Metric | Result |
|---|---:|
| Clean observations | 238 |
| Training observations | 190 |
| Testing observations | 48 |
| R² | 0.1986 |
| MAE | 999.97 |
| RMSE | 1308.62 |
| Average Profit | -401.50 |

## Current Status

**Working Published Prototype**

The current version is focused on a structured retail-sales analysis workflow.

## Future Roadmap

Future versions will expand the system toward:

- Dynamic analysis for different dataset types
- Pandas / NumPy integration
- SciPy and Statsmodels
- Scikit-learn machine learning
- Automated statistical test selection
- Automated charts and dashboards
- Power BI / Plotly integration
- Multi-agent statistical analysis

## Author

**Zaeem Jamil**  
BS Statistics

## Disclaimer

StatFlow AI is an analytical automation project. Results should be reviewed and validated before being used for high-impact decisions.

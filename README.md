# Agrivoltaic Data Analysis – Ghana

This project explores environmental and operational insights from a pilot agrivoltaic system in Ghana, combining solar energy generation with crop farming. The goal is to use data to understand how solar panels affect local microclimate and crop-growing conditions, and to offer recommendations for system design in tropical regions like Ghana.

---

## Project Overview

Agrivoltaic systems allow both **farming** and **solar energy** production on the same land. This is especially useful in countries like Ghana that face both energy needs and food security challenges. However, installing solar panels changes the local environment (shade, temperature, humidity), and we need to know **how this affects crops**.

This project uses data from a real-world pilot site in Ghana to analyze environmental variables across different test plots:
- **Control Field**: Traditional farming without solar panels
- **Agrivoltaic Plot**: Raised solar panels over crops  
- **Ground-mounted PV**: Solar energy setup with no crops

---

## Objectives

- Understand the effect of solar panels on sunlight, temperature, and moisture
- Compare conditions in shaded (agrivoltaic) vs. unshaded (control) plots
- Identify seasonal and daily trends in environmental variables
- Provide **data-driven recommendations** for future agrivoltaic systems
- Create interactive visualizations for real-time data exploration

---

## Research Questions

1. How do solar irradiation and temperature vary between plot types?
2. What are the differences in humidity and soil moisture between plots?
3. How do these variables change during the day and across months?
4. Are microclimate changes under panels statistically significant?
5. What practical recommendations can we provide for system design?

---

## Dataset Description

- **Source**: Responsible AI Lab (RAIL), Ghana  
- **Location**: Pilot agrivoltaic site with three plot types
- **Time**: Data collected during May, June, July, August, and October
- **Variables**:  
  - Irradiation (W/m²)  
  - Temperature (°C)  
  - Relative Humidity (%)  
  - Soil Moisture (%)  
  - Rainfall (mm)  
  - Time and Month

---

## Project Structure

```
agrivoltaic-analysis/
│
├── Data/                     # Raw and cleaned data files
│   ├── Raw/                  # Original source data (untouched)
│   └── Processed/            # Cleaned and transformed data
│       └── merged.csv        # Main dataset for analysis
│
├── Notebooks/                # Jupyter notebooks for EDA and analysis
│   ├── Data_Cleaning.ipynb   # Data preprocessing and cleaning
│   ├── agrivoltaics_report.qmd # Quarto report with analysis
│   └── Data_Analysis.zip     # Compressed data analysis files
│
├── Results/                  # Plots and analysis results
│   ├── *.png                 # PNG format images
│   ├── *.jpg                 # JPG format images
│   └── *.html                # Interactive HTML plots
│
├── Dashboard/                # Interactive Dash application
│
├── Presentation/             # Final presentation slides
│
├── Docs/                     # PDF reports, documentation, and report file
│
└── README.md                 # Project overview and instructions
```

---

## Key Deliverables

### ✅ Completed
- **Data Cleaning & Preprocessing**: Comprehensive data cleaning pipeline in `Data_Cleaning.ipynb`
- **Exploratory Data Analysis**: Statistical analysis and visualization in `agrivoltaics_report.qmd`
- **Interactive Dashboard**: Dash application with real-time data visualization
- **Monthly Rainfall Patterns**: Analysis of seasonal rainfall trends
- **Environmental Conditions by Plot Type**: Comparison of sensor data across different plot types
- **Dataset Overview**: Statistical summary and data type distribution
- **Comprehensive Visualizations**: 40+ charts covering temperature, humidity, soil moisture, and irradiance

### 🔄 In Progress
- **Presentation Slides**: Final project presentation

---

## Interactive Dashboard

The project includes a **Dash application** that provides:
- **Real-time data visualization** of environmental conditions
- **Monthly rainfall patterns** with interactive charts
- **Environmental conditions comparison** across plot types
- **Dataset overview** with statistical summaries
- **Responsive design** with modern UI/UX

### Running the Dashboard
```bash
cd Dashboard
python agrivoltaic_dashboard.py
```

---

## Analysis Highlights

### Environmental Variables Analyzed
- **Temperature**: Daily and monthly trends across plot types
- **Humidity**: Relative humidity patterns and comparisons
- **Soil Moisture**: Moisture retention under different conditions
- **Irradiance**: Solar radiation patterns and efficiency
- **Rainfall**: Seasonal precipitation analysis

### Key Findings
- **Temperature Regulation**: Agrivoltaic plots show moderated temperature extremes
- **Moisture Retention**: Enhanced soil moisture under solar panel shade
- **Seasonal Patterns**: Clear monthly trends in all environmental variables
- **Plot Comparisons**: Statistical differences between control, agrivoltaic, and ground PV plots

---

## Technical Stack

- **Python**: Data analysis and visualization
- **Pandas**: Data manipulation and cleaning
- **Plotly**: Interactive visualizations
- **Dash**: Web application framework
- **NumPy**: Numerical computations
- **Quarto**: Scientific reporting
- **Jupyter**: Interactive analysis notebooks

---

## Project Status

✅ **Data Exploration & Cleaning**: Complete  
✅ **Interactive Dashboard**: Complete  
✅ **Statistical Analysis**: Complete 
✅ **Visualization Suite**: Complete  
✅ **Final Report**: Complete  
🔄 **Presentation**: In Progress  

---

## Contributing

This project is educational and part of a capstone/final project. Contributions or feedback are welcome.

---

## References

- Responsible AI Lab – [Agrivoltaic Dataset (Ghana)](https://www.kaggle.com/datasets/responsibleailab/agrivoltaic-dataset-ghana)
- Barron-Gafford, G.A. et al. (2019). *Agrivoltaics Provide Mutual Benefits Across the Food–Energy–Water Nexus in Drylands*. Nature Sustainability.

---

## Contact

Created by: Nadia, Cynthia, Annick, Hadidja  
Institution: kLab Rwanda  


you can check our dashboard here: https://data-pilot-agrivoltaic-system-1.onrender.com/
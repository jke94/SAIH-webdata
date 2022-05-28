# SAIH-webdata
A couple of python scripts to extract the data for the SAIH web. The SAIH is the acronyms about "Sistema Automático de Información Hidrológica".

# Runtime environment path
**IMPORTANT NOTE:** All the scripts must be executed from the base repository path.

## 1. Extract and plotting data.

### 1.1. Extract the data.
```
python .\src\saih-web-scraping\saih-data-scraper.py
```

### 1.2. Plotting the data.

- Plotting the rain in the last 36h.

```
python .\src\saih-plotting-data\saih-rain-36h-subplots.py
```

- Plotting the temperature in the last 36h.

```
.\src\saih-plotting-data\saih-temperature-36h-subplots.py
```

- Plotting the temperature in the last 24h with a heatmap.py.

```
.\src\saih-plotting-data\saih-temperature-24h-heatmap.py
```
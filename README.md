# SAIH-webdata
A couple of python scripts to extract the data for the SAIH web. The SAIH is the acronyms about "Sistema Automático de Información Hidrológica".

- Official Website: [saihduero.es](https://www.saihduero.es/)

# Runtime environment path
**IMPORTANT NOTE:** All the scripts must be executed from the base repository path.

## 1. Extract and plotting data.

### 1.1. Extract the data.
```
python .\src\saih-web-scraping\saih-data-scraper.py
```
- Generated data files:

![imagen](https://user-images.githubusercontent.com/53972851/181630652-9105601e-11e2-4762-8e22-5646db7954c8.png)

### 1.2. Plotting the data.

#### 1.2.1 - Plotting the rain in the last 36h.

```
python .\src\saih-plotting-data\saih-rain-36h-subplots.py
```

- Generated image example:

![imagen](https://user-images.githubusercontent.com/53972851/181630424-643dfddc-d9da-470f-8595-3e218d105cd9.png)

#### 1.2.2 - Plotting the temperature in the last 36h.

```
python .\src\saih-plotting-data\saih-temperature-36h-subplots.py
```

- Generated image example:

![imagen](https://user-images.githubusercontent.com/53972851/181630049-3c4fdc0f-ca0e-4145-86cc-8bd0c2ca310a.png)

#### 1.2.3 - Plotting the temperature in the last 24h with a heatmap.py.

```
python .\src\saih-plotting-data\saih-temperature-24h-heatmap.py
```

- Generated image example:

![imagen](https://user-images.githubusercontent.com/53972851/181631180-18cba238-f797-4d60-ae93-55661540b6fd.png)

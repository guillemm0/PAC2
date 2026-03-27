# CO₂ emissions by sector - Data package

This data package contains the data that powers the chart ["CO₂ emissions by sector"](https://ourworldindata.org/grapher/co-emissions-by-sector?v=1&csvType=full&useColumnShortNames=false) on the Our World in Data website.

## CSV Structure

The high level structure of the CSV file is that each row is an observation for an entity (usually a country or region) and a timepoint (usually a year).

The first two columns in the CSV file are "Entity" and "Code". "Entity" is the name of the entity (e.g. "United States"). "Code" is the OWID internal entity code that we use if the entity is a country or region. For most countries, this is the same as the [iso alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) code of the entity (e.g. "USA") - for non-standard countries like historical countries these are custom codes.

The third column is either "Year" or "Day". If the data is annual, this is "Year" and contains only the year as an integer. If the column is "Day", the column contains a date string in the form "YYYY-MM-DD".

The remaining columns are the data columns, each of which is a time series. If the CSV data is downloaded using the "full data" option, then each column corresponds to one time series below. If the CSV data is downloaded using the "only selected data visible in the chart" option then the data columns are transformed depending on the chart type and thus the association with the time series might not be as straightforward.


## Metadata.json structure

The .metadata.json file contains metadata about the data package. The "charts" key contains information to recreate the chart, like the title, subtitle etc.. The "columns" key contains information about each of the columns in the csv, like the unit, timespan covered, citation for the data etc..

## About the data

Our World in Data is almost never the original producer of the data - almost all of the data we use has been compiled by others. If you want to re-use data, it is your responsibility to ensure that you adhere to the sources' license and to credit them correctly. Please note that a single time series may have more than one source - e.g. when we stich together data from different time periods by different producers or when we calculate per capita metrics using population data from a second source.

### How we process data at Our World In Data
All data and visualizations on Our World in Data rely on data sourced from one or several original data providers. Preparing this original data involves several processing steps. Depending on the data, this can include standardizing country names and world region definitions, converting units, calculating derived indicators such as per capita measures, as well as adding or adapting metadata such as the name or the description given to an indicator.
[Read about our data pipeline](https://docs.owid.io/projects/etl/)

## Detailed information about each time series


## Buildings
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Buildings” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Building subsector contains CO₂, CH₄ and N₂O emissions from the following activities:
  - Residential.
  - Commercial and public services.

  Please note that only on-site fuel combustion is covered here. Emissions associated with use of electricity are reported under electricity/heat.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Industry
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Industry” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Industry sector contains emissions from the following activities:
  - CO₂ emissions from Cement Manufacture.
  - N₂O emissions from Adipic and Nitric Acid Production.
  - F-Gases from Electronics Manufacturing (semiconductor, flat panel display (FPD) and photovoltaic (PV)).
  - SF6 from Electric Power Systems.
  - PFCs and SF6 from Metal Production (PFCs as by-product of aluminum production, SF6 from magnesium production).
  - HFCs from Uses of Substitutes for Ozone-Depleting Substances (ODS).
  - HFCs from HCFC-22 Production.
  - N₂O and CH₄ emissions from Other Industrial activities (non-agriculture).

  Please note that for the purpose of Climate Watch dataset, all fluorinated gases are reported as aggregated F-gas.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Land-use change and forestry
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Land-use change and forestry” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Land-Use Change and Forestry sector contains emissions from the following activities:
  - CO₂ emissions from Forest land and Net forest conversion (forestland converted to cropland and grassland).
  - CO₂ emissions from Drained organic soils.
  - CO₂ and CH₄ emissions from Fires in organic soils.
  - CH₄ and N₂O emissions from Forest fires.

  Please note that the forest land emissions data reflects emissions from changes in forest land area between reported years of Forest Resource Assessment (FRA) submitted by countries. The data is published every 5 years, and emissions values are estimated by interpolating data over those 5-year periods.

  Please note recent change of FAO's approach for reporting emissions from fires in organic soils (part of the "Burning Biomass"): only values from Southern-east Asia countries are included in country, regional and global aggregates (of burning biomass and subsequently land use total).

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Other fuel combustion
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Other fuel combustion” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Other fuel combustion subsector contains emissions from the following activities:
  - CO₂, CH₄, and N₂O emissions from Agriculture/forestry, fishing, and other fuel consumption.

  Other fuel consumption includes emissions from military fuel use.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Transport
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Transport” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Transportation subsector contains CO₂, CH₄ and N₂O emissions from the following activities:
  - Road.
  - Rail.
  - Domestic aviation.
  - Pipeline transport.
  - Domestic navigation.
  - Non-specified transport (all emissions from transport not specified elsewhere).

  Please note that transport emissions for world total includes international marine bunkers and international aviation bunkers, which are not included in transportation at a national or regional level.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Manufacturing and construction
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Manufacturing and construction” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Manufacturing/Construction subsector contains CO₂, CH₄ and N₂O emissions from the following activities:
  - Mining and quarrying.
  - Construction.
  - Manufacturing.
  - Iron and Steel.
  - Chemical and petrochemical.
  - Non-ferrous metals.
  - Non-metallic minerals.
  - Transport equipment.
  - Machinery.
  - Food and tobacco.
  - Paper, pulp and printing.
  - Wood and wood products.
  - Textile and leather.
  - Non-specified industry.

  Please note that part of the emissions might be reallocated to industrial processes and product use category under the 2006 IPCC GLs.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Fugitive emissions
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Fugitive emissions” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Fugitive Emissions subsector contains fugitive CO₂ and CH₄ emissions from the following activities:
  - CO₂ from Flaring.
  - CH₄ from Coal mining.
  - CH₄ from Natural gas and oil systems.
  - Production.
  - Flaring and venting.
  - Transmission and distribution.
  - CH₄ and N₂O from Other energy sources (solid fuels, oil and natural gas, incineration and open burning of waste).

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Electricity and heat
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Electricity and heat” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Electricity/heat subsector contains CO₂, CH₄ and N₂O emissions from the following activities:
  - Main activity producer of electricity and heat (electricity plants, combined heat and power plants, heat plants).
  - Unallocated autoproducers.
  - Other energy industry own use.

  Please note that part of the emissions might be reallocated to industrial processes and product use category under the 2006 IPCC GLs.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


## Aviation and shipping
Emissions are measured in tonnes.
Last updated: February 10, 2026  
Next update: February 2027  
Date range: 1990–2023  
Unit: tonnes  


### How to cite this data

#### In-line citation
If you have limited space (e.g. in data visualizations), you can use this abbreviated in-line citation:  
Climate Watch (2026) – with major processing by Our World in Data

#### Full citation
Climate Watch (2026) – with major processing by Our World in Data. “Aviation and shipping” [dataset]. Climate Watch, “Greenhouse gas emissions by sector” [original data].
Source: Climate Watch (2026) – with major processing by Our World In Data

### How is this data described by its producer - Climate Watch (2026)?
Bunker fuels contain CO₂ emissions from international marine and aviation bunkers. The split of domestic and international are determined by the departure and landing locations, and not by the nationality of the ship/airline.

  Bunker Fuels are shown as a sector, but excluded from national totals for Energy (including energy subsector Transport) and Total GHG emissions, in accordance with IPCC Guidelines. In other words, except at World level, Total GHG emissions (and accordingly Energy sector, and Transport sub-sector emissions) do not include bunker fuel emissions.

### Source

#### Climate Watch – Greenhouse gas emissions by sector
Retrieved on: 2026-02-10  
Retrieved from: https://www.climatewatchdata.org/data-explorer/historical-emissions  


    
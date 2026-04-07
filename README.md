# Exploratory Data Analysis on Car Dataset

## **1. Objective**
I wanted to perform Exploratory Data Analysis (EDA) on the 'car.csv' dataset to:
- Get a better understanding of the dataset.
- Find interesting patterns and relationships.
- Visualize the data to support insights and possible future analysis.

## 2. **Dataset Overview**
- The dataset originally had 848 rows and 12 columns.
- Some issues I noticed:
    *   Missing values in some columns.
    *   Numbers mixed with symbols in fields like 'Price'.

    *   Some duplicates and inconsistencies in text fields.

## **3**. **Data Exploration**
*   Observed summary statistics for numeric fields.
*   Checked missing values and unique values.

## **4. Data Cleaning**

*   Handling Missing Values:
    *   Filled missing numeric columns using KNN Imputer.
    *   Filled missing categorical values like colour with 'Unknown'.

*   Removing Duplicates:
    *  Removed duplicate rows based on 'name'.

*  Standardizing Columns:
    *   Renamed columns to make them consistent.
    *   Converted all text columns such as 'name', 'brand', 'fuel', 'transmission', 'colour' to lowercase.

*   Cleaning Numeric Data:
    *  Removed symbols from price.
    *   Extracted numbers from 'mileage', 'engine_cc', 'km_run', 'make_year'.
    *   Converted them to integers.



*   Feature Engineering:
    *  Extracted brand from the name column.
    *   Calculated 'car_age' as 2025 - make_year.
    *   Dropped rows with invalid years like years greater than 2025 and less than 1975.

## **5. Data Visualization**

I made several plots to understand the data better:


*   Correlation heatmap to see relationships between numeric columns.
*   Pie chart for transmission types.

*   Car color distribution bar chart.
*   Top 10 car brands bar chart.

*   Bubble plot for fuel type distribution.
*   Scatter plot of 'price' vs 'make_year'.
*   Scatter plot of 'car_age' vs 'mileage'.
*   Line plot of average price of top brands.
*   'price' vs 'brand' boxplot.

## **6. Insights**

The following are the observations obtained from the exploratory data analysis on the car.csv dataset:

1.   Newer cars and cars with bigger engines generally cost more while older cars are usually cheaper.
1.  Most cars have manual transmission. Automatic cars are much less common.
1.  Petrol cars are the most common fuel type followed by diesel and very few cars are electric or hybrid.
1.  Hyundai, Tata, and Mahindra are the most frequently listed brands.
Other brands like Toyota, Kia, Ford, Honda, and Chevrolet appear less often.
2.  Silver, white, and other neutral colors are the most popular.
Bright colors like yellow, green, and brown are rare.
2. Some brands like Chevrolet and Honda have consistent price ranges. Other brands like Toyota and Hyundai show wide price variation with some expensive cars.

## **7. Conclusion**

The cleaned dataset is ready for further analysis or price prediction. It is observed that the used car market is dominated by manual petrol cars in neutral colors. Similarly, newer and bigger cars cost more while older cars are cheaper. Popular brands like Hyundai, Tata, and Mahindra appear most often and prices vary by brand and car age.

## **8. Applications**
The cleaned dataset can be used for given applications:

1.   Build price prediction models.

1.   Build vehicle rfecommendation system so that buyers can get guidance on popular brands, colors, and price ranges.
2.   Build a model that detects the environmental impact of the vehicle based on the car age, mileage and kilometer run.















































  


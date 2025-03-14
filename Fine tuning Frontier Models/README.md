Product Price Prediction with Fine-Tuned GPT Models

Overview - 
This project explores various machine learning and generative AI techniques to predict the price of products based on their descriptions. We curate data from the Amazon Reviews Dataset, apply traditional ML models for benchmarking, and compare their performance against LLM-based price estimations. Finally, we fine-tune a GPT model to optimize its performance for structured price prediction.

Project Pipeline :
The project consists of four major steps:

1) Data Curation

Extracted and cleaned product descriptions from the Hugging Face Amazon Reviews Dataset.
Selected relevant categories (Tools, Cell Phones, Toys, Appliances) to reduce dataset size while maintaining diversity.
Processed textual data for efficient tokenization and feature extraction.


2) Traditional Machine Learning Benchmarking

Implemented and evaluated baseline ML models (Random Forest, Linear Regression, SVR, etc.).
Compared their performance in predicting product prices.


3) GPT-Based Predictions

Tested OpenAI’s GPT-4o and GPT-4o-mini for price estimation.
Compared results with human predictions to assess LLM's generalization capabilities.


4) Tuning GPT for Custom Pricing Model

Fine-tuned GPT-4o-mini using curated product descriptions and real prices.
Used OpenAI Fine-Tuning API for enhanced price estimation accuracy.


Performance Comparison
(Lower is Better)
Random Number Generator	- $386
Constant Predictor (Mean Price) -	$118
Linear Regression -	$104
SVR Model -	$93
Random Forest -	$90
Human Prediction -	$141
GPT-4o-mini -	$67
GPT-4o (Fine-tuned) -	$58


Key Insights- 
LLMs outperform traditional models in estimating product prices based on textual descriptions.
Fine-tuned GPT-4o achieves the best accuracy, highlighting the importance of domain adaptation.
Human predictions lag behind GPT models, emphasizing the potential of AI-driven estimations.


Technology Stack -
LLM Frameworks: OpenAI GPT, Hugging Face Transformers
Machine Learning: Scikit-learn, NumPy, Pandas
Fine-tuning Tools: OpenAI Fine-Tuning API, Weights & Biases
Data Processing: Hugging Face Datasets, Matplotlib
Backend & Automation: Python, Pickle, CSV Handling


Installation & Usage -
1. Clone the Repository
git clone https://github.com/yourusername/Product-Price-Prediction.git  
cd Product-Price-Prediction

2. Install Dependencies
pip install -r requirements.txt

3. Run Notebooks Step-by-Step
1_DataCuration.ipynb → Data extraction & cleaning
2_TraditionalMLComparison.ipynb → Benchmark traditional ML models
3_Gptmodels_comparisons.ipynb → Compare GPT models with humans
4_Finetuning_gpt.ipynb → Fine-tune GPT for improved accuracy


Conclusions - 
Fine-tuning LLMs significantly enhances prediction accuracy in structured tasks.
GPT-4o outperforms all traditional models, even when fine-tuned on a small dataset.

This work bridges the gap between traditional ML and LLM-based inference for price prediction tasks.


Future Work -
Fine-tune models on larger datasets for even better accuracy.
Explore multi-modal LLMs integrating both text & images for price estimation.
Implement real-time pricing API for dynamic price forecasting.\


Contributors - 
Atharva Mahindrakar 
atharva77.mahindrakar@gmail.com
Steps to run the project

1: Extract the file "Offline_PDF_Reading_Chat_Bot"

2: Open VS Code

3: Instll Dependencies by
Running: pip install -r requirements 

4: Run:
(i) pip install "huggingface_hub>=0.23" transformers sentence-transformers
(ii) cd models
(iii) huggingface-cli download sentence-transformers/all-MiniLM-L6-v2 --local-dir all-MiniLM-L6-v2
(iv) huggingface-cli download microsoft/phi-2 --local-dir phi-2

to install the offline model phi2

5: run streamlit run streamlit_app.py
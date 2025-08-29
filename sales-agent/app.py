from langchain_tavily import TavilySearch
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
import streamlit as st
from dotenv import load_dotenv
from fpdf import FPDF
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
import io
import tempfile # For temporary file handling
from langchain.document_loaders import CSVLoader    
load_dotenv()


# Add custom CSS for white background and black text
st.markdown("""
    <style>
        .stApp {
            background-color: white;
        }
        .stTextInput label, .stTextArea label, .stRadio label {
            color: black !important;
        }
        .stRadio [role="radiogroup"] label {
            color: black !important;
        }
        /* Add these specific styles for radio buttons */
        .stRadio div[role="radiogroup"] div {
            color: black !important;
        }    
        .stMarkdown {
            color: black;
        }
        .stSubheader {
            color: black;
        }
        div[data-baseweb="select"] span {
            color: black;
        }
        /* Add these new styles for headings */
        .stTitle {
            color: black !important;
        }
        h1, h2, h3 {
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

#================== custom css changes end =====================

# Model
# llm = ChatGroq(model="openai/gpt-oss-20b")
llm = ChatGroq(model="llama3-8b-8192")

#Tool
search_tool = TavilySearch(topic="general", max_results=2)


def generate_insights( company_name, product_name, company_url, company_competitors):
    #perform search
    search_query = f"Site:{company_url} company strategy, leadership, competitors, business model"
    search_results = search_tool.invoke(search_query)
    print("\n Search Results: ", search_results)

    messages = [
    SystemMessage("You are a sales assistant that provides concise and structured insights."),
    HumanMessage(content=f"""
        Company Info from Tavily: {search_results}
        
        Company: {company_name}
        Product: {product_name}
        Company URL: {company_url}
        Competitors: {company_competitors}
        
        Generate a two-page summary including:
        1. Company strategy related to {product_name}
        2. Possible competitors or partnerships (including {company_competitors})
        3. Leadership and decision-makers relevant to this area
        4. Recent news or changes in strategy
        5. Recent funding or financial info
        6. Recent product launches or updates
        7. Market position and unique selling points
        8. Any challenges or pain points the company is facing
        9. Relevant industry trends impacting the company
        10. Any other relevant sales insights
        11. Suggestions for approaching the company for sales
        12. Use bullet points, headings, and subheadings for clarity.
        13. Keep it concise and focused on actionable sales insights.
        14. Avoid generic statements; be specific to the company and product.
        Format output in clear sections with bullet points.
        """)
    ]

    model_response = llm.invoke(messages)
    print("\n Model Response: ", model_response.content)
    return model_response.content

def create_pdf(report_content, company_name):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, f'Sales Insights Report - {company_name}', 0, 1, 'C')
    pdf.ln(10)
    
    pdf.set_font('Arial', '', 10)
    lines = report_content.split('\n')
    for line in lines:
        if line.strip():
            pdf.cell(0, 6, line.encode('latin-1', 'replace').decode('latin-1'), 0, 1)
        else:
            pdf.ln(3)
    
    pdf_output = io.BytesIO()
    pdf_string = pdf.output(dest='S').encode('latin-1')
    pdf_output.write(pdf_string)
    pdf_output.seek(0)
    return pdf_output.getvalue()



# ======= UI with Streamlit =====================
st.title("💼 AI Sales Assistant Agent")
st.subheader("Generate A Report")
st.divider()

# Comapny Name
company_name = st.text_input("Enter Company Name:")

# prduct Name
product_name = st.text_input("Enter Product Name:") 

#Company URL
company_url = st.text_input("Enter Company URL:")   

#Competitors
competitors = st.text_area("Enter Competitors (comma-separated):")

# Generate Report Button
report = None  # ---->ADDED REPORT VARIABLE TO TRACK GENERATED REPORTS
if st.button("Generate Report"):
    if company_name and company_url:
        with st.spinner("Generating Report..."):
            result = generate_insights(company_name, product_name, company_url, competitors)
            st.divider()
            st.write(result)
             # Assign the result to the report variable
            report = result
    if report is not None:
        # download as a text file
        st.download_button("Download Report", report, file_name="sales_report.txt", mime="text/plain")
        
        # download as a pdf file
        pdf_data = create_pdf(report, company_name)
        st.download_button(
            "Download Report as PDF",
            pdf_data,
            file_name=f"sales_report_{company_name}.pdf",
            mime="application/pdf"
        )
    else:
        st.warning("Please enter a company name and URL")

#================================test start==============================
#MOVED DOWNLOAD BUTTON OUTSIDE AND MADE IT CONDITIONAL
# if report is not None:
#     st.download_button("Download Report", report, file_name="sales_report.txt", mime="text/plain")

# CSV Analysis Section
csv_file = None
analysis_type = st.radio(
    "Choose Analysis Type",
    ["Custom Question", "Company Strategy", "Competitor Mentions", "Leadership Insights"]
)

# Input box for custom question
question = None
if analysis_type == "Custom Question":
    question = st.text_input("Enter your custom question:")

prompt_template = ChatPromptTemplate.from_template(
    """You are a sales assistant agent. Based on the provided context, generate insights.

Task: {task}
Context: {context}

Answer:"""
)

# Create a chain using the Groq model
analysis_chain = LLMChain(llm=llm, prompt=prompt_template)

# Sidebar
with st.sidebar:
    st.markdown("⚙️ Settings")
    
    temp = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.7,  # default
        step=0.1)
    
    stream = st.toggle("Stream")                


with st.sidebar:
    st.markdown("### 📂 Upload Data")
    csv_file_path = st.file_uploader("Upload a CSV file", type="csv")

    if csv_file_path is not None:
        # https://python.langchain.com/docs/how_to/document_loader_csv/
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp_file:
            tmp_file.write(csv_file_path.getvalue())
            tmp_file_path = tmp_file.name
        
        csv_loader = CSVLoader(file_path=tmp_file_path)
        csv_file = csv_loader.load()
        print("FILE UPLOADED: ", csv_file[:1])


if st.button("Run Analysis"):
    if csv_file is not None:
        with st.spinner("Analyzing..."):
            if analysis_type == "Custom Question":
                task = question if question else "Provide general insights."
            elif analysis_type == "Company Strategy":
                task = "Summarize the company’s strategy and key business focus areas."
            elif analysis_type == "Competitor Mentions":
                task = "Identify and summarize competitors mentioned in the data."
            elif analysis_type == "Leadership Insights":
                task = "Extract insights about company leadership, management structure, new products and decisions."

            # Convert CSV docs into plain text context
            context = "\n".join([doc.page_content for doc in csv_file])

            response = analysis_chain.invoke({"task": task, "context": context})

            st.subheader("Analysis Response")
            st.write(response["text"])
             # SIMPLIFIED DOWNLOAD BUTTON FOR ANALYSIS (REMOVED DUPLICATE GENERATE REPORT LOGIC)
            st.download_button(
                label="Download Analysis",
                data=response["text"],
                file_name="ai_analysis_report.txt",
                mime="text/plain",
                key="analysis_download"
            )
    else:
        st.warning("Please upload a CSV file first.")            
#================================test end==============================




from nuclia import sdk
import requests
import os
# from dotenv import load_dotenv

from nuclia import sdk
import streamlit as st


KB_URL = 'https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/4abbf482-7dfd-405f-b005-94eb0903aa6a'
API_KEY = 'eyJhbGciOiJSUzI1NiIsImtpZCI6InNhIiwidHlwIjoiSldUIn0.eyJpc3MiOiJodHRwczovL2F3cy11cy1lYXN0LTItMS5udWNsaWEuY2xvdWQvIiwiaWF0IjoxNzM3NTQ1ODc2LCJzdWIiOiJhZWNjMjU5OC0zNGI5LTQ5YjMtOTVlMS1mOGZmOWIzZGY4NTkiLCJqdGkiOiI0Y2E2NzdlNy1kZDc0LTRiZDEtYmI4MC03YzgyMWU3NzM3MWUiLCJleHAiOjE3NjkwODE4NzMsImtleSI6IjZmMmE0ZjhiLTUwYTctNGZkMy1hZWVjLTBmY2QyNWI3OTYyMiIsImtpZCI6ImQ4ZGI1Y2RmLTg5ZjAtNGZiNS1iZjFiLTBhMjY4MjViZjZmZiJ9.hdJxRBdSfZw7wRmptIv8hymGCCOuuKbHadR8ayEVMiifxhATf4FrxTuul_17fKpDsbe2AtvADhh0BRI54OutN1Bz4cn93zsjj3uTrifo9KcI3fGAmCfIV0rIP7LTdKHUZ_ooCdphdqS_mBrdWIQ18Id19wsPMEH1wV9WYK2bJJ8Qeo7I5Pj7R0RNIt8yG5GEto1SLr4w62WZJmBEDjycBucRv04YKdhAD3-_fHfXNbhGsC4lLiidSy8lE9HBHcK22BtJSflcovfmNgh43sIXt0g6bTjLpEQwc3fkxS7Bp2FeyOgz8MPfhSS-dVeVr0fJeeQ4hkCDB2HcUF3PkJWXG0YV1n4nkkz2grmTDeTo8SNaxt1kKrgWTPTuUGS4kZolBi8aQ-Xsfbj2zmyYDyaVjwWW9ul2QtqSsYBK1fJhnIBnW0nNdnAvJ9lto0MnSKvy7-tiABFmZGgUZnLUSaMdxo4fxPuISXqzICge8SsMJBrDmZDkDOQF3sJJH5OLnkQELgF4tgo4wuBjJSbu4chrdhcPCWLxlOvU8auWO573QWcuR3ew1-maTMHKevPRBQYSthdaKlm11soQOA3HXVcuizVqo6YIwDV3mmvv3rtAWTzQ9BzxSvo0tLMddXUsyDQBqdeiN-1CbTtFnDRIrdZjCLVbUNgc-60w77VlBeykYuo'


try:
    kb = sdk.NucliaAuth().kb(url=KB_URL, token=API_KEY)
    print(kb,"Authentication successful!")
except Exception as e:
    print("Error:", e)

# search = sdk.NucliaSearch()
# response=search.ask(
#     apikey=API_KEY,
#     knowledgebox="4abbf482-7dfd-405f-b005-94eb0903aa6a",
#     zone="aws-us-east-2-1",
#     # query="ParityQC's expertise in quantum architecture",
#     query="quantum news today",
#     src="https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/4abbf482-7dfd-405f-b005-94eb0903aa6a",
#     context=[],
#     show=["basic","values","origin"],
#     features=["keyword","semantic"],
#     highlight=False,
#     citations=False,
#     rephrase=True,
#     debug=False,
#     show_hidden=False,
#     reranker="predict",
#     autofilter=False,
#     rag_strategies=[{"name":"neighbouring_paragraphs","before":2,"after":2}],
#     shards=[],
# )
# print(response)


def get_query(query):
    search = sdk.NucliaSearch()
    response=search.ask(
        apikey=API_KEY,
        knowledgebox="4abbf482-7dfd-405f-b005-94eb0903aa6a",
        zone="aws-us-east-2-1",
        query=query,#"ParityQC's expertise in quantum architecture
        src="https://aws-us-east-2-1.nuclia.cloud/api/v1/kb/4abbf482-7dfd-405f-b005-94eb0903aa6a",
        context=[],
        show=["basic","values","origin"],
        features=["keyword","semantic"],
        highlight=False,
        citations=False,
        rephrase=True,
        debug=False,
        show_hidden=False,
        reranker="predict",
        autofilter=False,
        rag_strategies=[{"name":"neighbouring_paragraphs","before":2,"after":2}],
        shards=[],
    )
    return response


st.sidebar.markdown(
    """
    <style>
    .large-dashboard-title {
        font-size: 20pt;
        font-family: Roboto, sans-serif;
        color: rgb(0, 0, 0);
        font-weight: bold;
    }
    </style>
    <div class="large-dashboard-title">Dashboard</div>
    """,
    unsafe_allow_html=True
)
st.sidebar.markdown(
    """
    <style>
    .stRadio > div {
        margin-bottom: 15px; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

option = st.sidebar.radio(
    "Choose an option:",
    ["News Selection", "Context Review", "Commentary Input", "Progress Visualization"]
)

if option == "News Selection":
    st.write("News item selection panel")
elif option == "Context Review":
    st.header("Quantum News Insight Tool")
    query=st.text_input("enter your query")
    if query:
        st.write(get_query(query))
   
    else:
        st.write("Please enter a question.")

elif option == "Commentary Input":
    st.write("Commentary input field")
elif option == "Progress Visualization":
    st.write("Process progress visualization")




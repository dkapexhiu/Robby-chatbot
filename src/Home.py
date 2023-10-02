import streamlit as st


#Config
st.set_page_config(layout="wide", page_icon="💬", page_title="Document Chatbot OpenAI 🤖")


#Contact
with st.sidebar.expander("📬 Contact"):

    st.write("**Twitter:** [@danielkapexhiu](https://twitter.com/danielkapexhiu)")
    st.write("**Mail** : daniel.kapexhiu@gmail.com")
    st.write("**Created by Daniel**")


#Title
st.markdown(
    """
    <h2 style='text-align: center;'>Multi Document ChatBot</h1>
    """,
    unsafe_allow_html=True,)

st.markdown("---")


#Description
st.markdown(
    """ 
    <h5 style='text-align:center;'>I'm a chatbot assistant, an intelligent chatbot created by combining 
    the strengths of Langchain and Streamlit. I use large language models to provide
    context-sensitive interactions. My goal is to help you better understand your data.
    I support PDF, TXT, CSV, Youtube transcript 🧠</h5>
    """,
    unsafe_allow_html=True)
st.markdown("---")


#Robby's Pages
st.subheader("🚀 Chatbot's Pages")
st.write("""
- **Chatbot-Chat**: General Chat on data (PDF, TXT,CSV) with a [vectorstore](https://github.com/facebookresearch/faiss) (index useful parts(max 4) for respond to the user) | works with [ConversationalRetrievalChain](https://python.langchain.com/en/latest/modules/chains/index_examples/chat_vector_db.html)
- **Chatbot-Sheet** (beta): Chat on tabular data (CSV) | for precise information | process the whole file | works with [CSV_Agent](https://python.langchain.com/en/latest/modules/agents/toolkits/examples/csv.html) + [PandasAI](https://github.com/gventuri/pandas-ai) for data manipulation and graph creation
- **Chatbot-Youtube**: Summarize YouTube videos with [summarize-chain](https://python.langchain.com/en/latest/modules/chains/index_examples/summarize.html)
""")
st.markdown("---")


#Contributing
st.markdown("### 🎯 Contributing")
st.markdown("""
**Chatbot is under regular development. Feel free to contribute and help me make it even more data-aware!**
""", unsafe_allow_html=True)






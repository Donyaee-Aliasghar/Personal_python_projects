import streamlit as st
import pandas as pd

from utils.gc_calculator import sliding_gc_calculator
from utils.io_helper import parser_sequence_file

st.set_page_config(page_title="GC content calculator", layout="centered")
st.title("🧬 GC content calculator")
st.markdown("Calculating GC content with sliding window for FASTA and FASTQ files")


uploaded_file = st.file_uploader("📤 Upload FASTA or FASTQ file", type=["fasta", "fa", "fastq"])
window_show = st.number_input("📏 Window size ", min_value=10, value=100, step=10)
step = st.number_input("↔️ Step size ", min_value=10, value=100, step=10)

if uploaded_file and st.button("🚀 GC content calculate"):
    records = parser_sequence_file(uploaded_file)

    for record in records:
        st.subheader(f"📌 Record: {record.id}")
        data = sliding_gc_calculator(record.id, window_show=window_show, step_size=step)

        if not data:
            st.warning("⚠️ The sequence length is less than the window size.")
            continue
        df = pd.DataFrame(data, columns=["Position", "GC content (%)"])
        st.line_chart(df.set_index("Position"))

        csv_name = f"results/{record.id}_gc.csv"
        df.to_csv(csv_name, index=False)

        st.success(f"✅ Saved :{csv_name}")
        st.download_button("📥 CSV download", df.to_csv(index=False), file_name=f"{record.id}_gc.csv", mime="text/csv")

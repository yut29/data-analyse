import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('数据分析应用')

# 1. 上传数据表 CSV
uploaded_file = st.file_uploader("选择一个 CSV 文件", type="csv")

if uploaded_file is not None:
    # 读取 CSV 文件
    df = pd.read_csv(uploaded_file)

    # 2. 展示表格前 5 行
    st.subheader('数据预览')
    st.write(df.head())

    # 3. 选择表格中的某一列进行分析，展示 boxplot 图
    st.subheader('列分析')
    selected_column = st.selectbox('选择一列进行分析', df.columns)
    
    fig, ax = plt.subplots()
    ax.boxplot(df[selected_column])
    ax.set_title(f"{selected_column} 的 Boxplot 图")
    st.pyplot(fig)

    # 4. 分析异常值
    st.subheader('异常值分析')
    q1 = df[selected_column].quantile(0.25)
    q3 = df[selected_column].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = df[(df[selected_column] < lower_bound) | (df[selected_column] > upper_bound)]
    
    if len(outliers) > 0:
        st.write(f"在 {selected_column} 列中发现 {len(outliers)} 个异常值：")
        st.write(outliers)
    else:
        st.write(f"在 {selected_column} 列中未发现异常值。")

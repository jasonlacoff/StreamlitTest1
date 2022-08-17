import streamlit as st

st.title('test')

df = pd.DataFrame(
    np.random.randn(50, 20),
    columns=('col %d' % i for i in range(20)))

st.dataframe(df)  # Same as st.write(df)


st.dataframe(df, 200, 100)

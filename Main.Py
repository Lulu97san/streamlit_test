import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('streamlit 入門')
st.sidebar.write('Interactive WidgetsInteractive Widgets')

""" 'Start!!'

latest_iteration = st.empty()
bar = st.progresss(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!!'

text = st.sidebar.text_input('あなたの趣味を教えてください')
condition = st.sidebar.slider('あなたの今の調子は?',0,100,50)


'あなたの趣味:', text
'コンディション:', condition """
#if st.checkbox('Show Image'):
#    img = Image.open('オーロラ.jpg')
#    st.image(img, caption='Kohei Imanishi', use_column_width=True)

#Image.open()


#df = pd.DataFrame(
#    np.random.rand(100,2)/[50,50]+[35.69,139.70],
#    columns=['lat','lon']
#)

#st.map(df)
#st.line_chart(df)

#st.write(df)

#st.dataframe(df, width=100,height=100  )
#st.table(df, width=100,height=100  )

"""
# 章
## 節
### 項
'''python
import streamlit as st
import numpy as np
import pandas as pd
'''

"""

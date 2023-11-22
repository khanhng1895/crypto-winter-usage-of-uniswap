import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Crypto Data Visualization")

# Monthly Number of Swap Transactions For each Network
st.subheader("Monthly Number of Swap Transactions For each Network")
undefined29 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/50707d5c-8903-4af3-8b53-c5c737105302/data/latest")
fig29 = px.bar(undefined29.astype({'NETWORK': 'string'}), 
            x='DATE', 
            y='TOTAL_TXNS', 
            color='NETWORK'
            )
fig29.update_layout(title="Monthly Number of Swap Transactions For each Network")
st.plotly_chart(fig29)

# Monthly Number of Swappers For each Network
st.subheader("Monthly Number of Swappers For each Network")
undefined30 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/50707d5c-8903-4af3-8b53-c5c737105302/data/latest")
fig30 = px.bar(undefined30.astype({'NETWORK': 'string'}), 
            x='DATE', 
            y='USERS', 
            color='NETWORK'
            )
fig30.update_layout(title="Monthly Number of Swappers For each Network")
st.plotly_chart(fig30)

# Monthly Swap Volume for each Network
st.subheader("Monthly Swap Volume for each Network")
undefined31 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/50707d5c-8903-4af3-8b53-c5c737105302/data/latest")
fig31 = px.bar(undefined31.astype({'NETWORK': 'string'}), 
            x='DATE', 
            y='TOTAL_VOLUME_USD', 
            color='NETWORK'
            )
fig31.update_layout(title="Monthly Swap Volume for each Network")
st.plotly_chart(fig31)

# Total Number of Swap Transactions for Each Network
st.subheader("Total Number of Swap Transactions for Each Network")
undefined22 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig22 = px.bar(undefined22.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='TOTAL_TXNS', 
            color='NETWORK'
            )
fig22.update_layout(title="Total Number of Swap Transactions for Each Network")
st.plotly_chart(fig22)

# Total Number of Swappers for Each Network
st.subheader("Total Number of Swappers for Each Network")
undefined23 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig23 = px.bar(undefined23.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='USERS', 
            color='NETWORK'
            )
fig23.update_layout(title="Total Number of Swappers for Each Network")
st.plotly_chart(fig23)

# Total Swap Volume for Each Network
st.subheader("Total Swap Volume for Each Network")
undefined24 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig24 = px.bar(undefined24.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='TOTAL_VOLUME_USD', 
            color='NETWORK'
            )
fig24.update_layout(title="Total Swap Volume for Each Network")
st.plotly_chart(fig24)

# Categorizing Users Based on Their Type
st.subheader("Categorizing Users Based on Their Type")
undefined17 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/bb63897c-a1e0-4dfc-91d6-6629259ed4c7/data/latest")
fig17 = px.bar(undefined17.astype({'NETWORK': 'string'}), 
            x='TYPE', 
            y='USERS', 
            color='NETWORK',
            barmode='group'
            )
fig17.update_layout(title="Categorizing Users Based on Their Type")
st.plotly_chart(fig17)

# Categorizing Transactions Based on Their Fee Amounts
st.subheader("Categorizing Transactions Based on Their Fee Amounts")
undefined18 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/49f16bed-e7fe-4921-89f1-97f746ea31e4/data/latest")
fig18 = px.bar(undefined18.astype({'NETWORK': 'string'}), 
            x='FEE_TYPE', 
            y='TXNS', 
            color='NETWORK',
            barmode='group'
            )
fig18.update_layout(title="Categorizing Transactions Based on Their Fee Amounts")
st.plotly_chart(fig18)

# Top 10 Most Popular Tokens for Swapping
st.subheader("Top 10 Most Popular Tokens for Swapping")
undefined19 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/3d3bc4bd-0065-4ef8-bf3e-a0e306b6c513/data/latest")
fig19 = px.bar(undefined19.astype({'SYMBOL_OUT': 'string'}), 
            x='NETWORK', 
            y='TOTAL_VOLUME_USD', 
            color='SYMBOL_OUT',
            barmode='group'
            )
fig19.update_layout(title="Top 10 Most Popular Tokens for Swapping")
st.plotly_chart(fig19)

# Top 10 Tokens with the Highest Swap Activity
st.subheader("Top 10 Tokens with the Highest Swap Activity")
undefined20 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/779d79c8-ce2b-4768-a94b-97ed4acb1093/data/latest")
fig20 = px.bar(undefined20.astype({'SYMBOL_IN': 'string'}), 
            x='NETWORK', 
            y='TOTAL_VOLUME_USD', 
            color='SYMBOL_IN',
            barmode='group'
            )
fig20.update_layout(title="Top 10 Tokens with the Highest Swap Activity")
st.plotly_chart(fig20)

# Categorizing users based on the number of transactions
st.subheader("Categorizing users based on the number of transactions")
undefined21 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/e614933a-ee4b-4bfe-b485-7be96f167240/data/latest")
fig21 = px.bar(undefined21.astype({'TX_TYPE': 'string'}), 
            x='NETWORK', 
            y='USERS', 
            color='TX_TYPE',
            barmode='group'
            )
fig21.update_layout(title="Categorizing users based on the number of transactions")
st.plotly_chart(fig21)

# Average Volume of Swaps per User
st.subheader("Average Volume of Swaps per User")
undefined25 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig25 = px.bar(undefined25.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='AVERAGE_VOLUME_PER_USER', 
            color='NETWORK'
            )
fig25.update_layout(title="Average Volume of Swaps per User")
st.plotly_chart(fig25)

# Average Number of Swap Transactions per User
st.subheader("Average Number of Swap Transactions per User")
undefined26 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig26 = px.bar(undefined26.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='AVERAGE_TXNS_PER_USER', 
            color='NETWORK'
            )
fig26.update_layout(title="Average Number of Swap Transactions per User")
st.plotly_chart(fig26)

# Total Fee Volume for Each Network
st.subheader("Total Fee Volume for Each Network")
undefined27 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig27 = px.bar(undefined27.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='TOTAL_FEE_USD', 
            color='NETWORK'
            )
fig27.update_layout(title="Total Fee Volume for Each Network")
st.plotly_chart(fig27)

# Average Fee Volume for Each Network
st.subheader("Average Fee Volume for Each Network")
undefined28 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/578412e4-7543-4b2a-8489-637552a27e7d/data/latest")
fig28 = px.bar(undefined28.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='AVG_FEE_USD', 
            color='NETWORK'
            )
fig28.update_layout(title="Average Fee Volume for Each Network")
st.plotly_chart(fig28)

# Categorizing Users Based on Their Retention Duration
st.subheader("Categorizing Users Based on Their Retention Duration")
undefined33 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/13a0017f-e54a-4720-8a67-c81902f6dcfe/data/latest")
fig33 = px.bar(undefined33.astype({'TYPE': 'string'}), 
            x='NETWORK', 
            y='TRADERS', 
            color='TYPE',
            barmode='group'
            )
fig33.update_layout(title="Categorizing Users Based on Their Retention Duration")
st.plotly_chart(fig33)

# Average Time Gap Between Token Listings on Each Network
st.subheader("Average Time Gap Between Token Listings on Each Network")
undefined34 = pd.read_json("https://api.flipsidecrypto.com/api/v2/queries/2d33dc69-1075-48bd-85a2-f69c003eb98b/data/latest")
fig34 = px.bar(undefined34.astype({'NETWORK': 'string'}), 
            x='NETWORK', 
            y='AVERAGE_TIME_DIFFERENCE_IN_HOURS', 
            color='NETWORK'
            )
fig34.update_layout(title="Average Time Gap Between Token Listings on Each Network")
st.plotly_chart(fig34)

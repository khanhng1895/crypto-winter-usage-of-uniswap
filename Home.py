import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
st.set_page_config(layout="wide")

col1, col2, col3 = st.columns([1,3,1])
with col1:
  st.image("https://assets.website-files.com/637be5d0f2736f32b8ad98cd/6390a10538dcb05321596402_uniswap.jpeg", width=200,)
with col2:
  st.markdown(f'<h1 style="font-weight:bold;font-family:Georgia;font-size:60px;text-align:center;text-shadow: 5px 5px black;color:#48f7e9;">{"Crypto Winter Usage of Uniswap"}</h1>', unsafe_allow_html=True)
with col3:
  st.image("https://assets.website-files.com/637be5d0f2736f32b8ad98cd/6390a10538dcb05321596402_uniswap.jpeg", width=200,)

st.header(":blue[INTRODUCTION]")

st.write("Uniswap is a decentralized exchange (DEX) that allows users to swap any ERC-20 tokens without intermediaries or fees. It also enables users to provide liquidity to the platform and earn a share of the trading fees. Uniswap is one of the most popular and widely used DEXs in the crypto space, with over $1.7 billion in total value locked (TVL) as of September 21, 2023")

st.subheader(":red[TRADING VOLUME]")

st.write(":blue[The trading volume on Uniswap is the total amount of tokens swapped on the platform in a given period]. It reflects the level of activity and demand for the service. The chart below shows the weekly trading volume on Uniswap till September 2023.")

col1, col2 = st.columns([3,1])

with col1:
  df1 = pd.read_csv('Charts/1_Uniswap_Trading_Volume(Defillama).csv')
  
  fig_1 = px.bar(df1, x="TIMESPAN", y="VOLUME", color="MARKET_STATE", title="1. Uniswap Trading Volume(Defillama)", height=500)
  fig_1.update_layout(hovermode="x unified")
  st.plotly_chart(fig_1, use_container_width=True)

  df2 = pd.read_csv('Charts/1a_Trading_Volumes_of_Other_Dexes.csv')
  
  fig_2 = px.line(df2, x="TIMESPAN", y="VOLUME", color="PROTOCOLS", title="1a. Trading Volumes of Other Dexes", height=500)
  fig_2.update_layout(hovermode="x unified")
  st.plotly_chart(fig_2, use_container_width=True)

# st.dataframe(df1)




# """Initialize Flipside with your API Key / API Url"""
# flipside = Flipside("c503c1cb-b42e-4980-8aa5-1255823998a3", "https://api-v2.flipsidecrypto.xyz")
# sql = """SELECT date_trunc(week, date) AS timespan, CASE WHEN date <= '2022-01-01' THEN 'Before Bear' ELSE 'Current Bear' END AS market_state, sum (volume) AS volume FROM external.defillama.fact_dex_volume WHERE protocol LIKE 'uniswap%' GROUP BY 1,2"""
# """Run the query against Flipside's query engine and await the results"""
# query_result_set = flipside.query(sql)
# print(query_result_set)

# data = query_result_set.loc[records]
# df = pd.DataFrame(data)
# st.dataframe(query_result_set)

with col2:
  st.write("👈👈As we can see, the trading volume on Uniswap reached an :blue[all-time high of 26.7 billion dollars in Nov 2022,] coinciding with the peak of the crypto bull market. However, since then, the trading volume has shown a downward trend, reaching a :red[low of 3.2 billion dollars in December 2023], a :red[decline of 88.01%]. The run is characterized by periodic spikes out of which :blue[March 2023 is a notable date of 26.15 billion dollars] trading volume. This value is impressive given the current state of the cryptoverse.")

  st.write("Also, the pyramid shape of all the trading volumes of other DEXes shows the decline in values with time and uniswap leading the pack with a great margin.")
  
  st.markdown("""The decline in trading volume can be attributed to several factors, such as:
  - The overall decrease in market sentiment and interest in crypto, as evidenced by the falling prices and volumes of major cryptocurrencies like Bitcoin and Ethereum.
  - The increase in gas fees on the Ethereum network, which makes swapping tokens on Uniswap more expensive and less attractive for users.
  - The emergence of competitors and alternatives to Uniswap, such as other DEXs on Ethereum (e.g., SushiSwap, Curve, Balancer) or on other blockchains (e.g., PancakeSwap on Binance Smart Chain, QuickSwap on Polygon, ThorSwap on ThorChain).
  - The regulatory uncertainty and scrutiny around crypto, especially in the US, where Uniswap has a large user base. For example, in July 2023, Uniswap Labs announced that it would restrict access to certain tokens on its web interface for US users, citing compliance reasons.
  """)
  
st.subheader(":red[USERS STATS]")

st.write("The number of users on Uniswap is the total number of unique addresses that have interacted with the Uniswap smart contracts in a given period. It reflects the size and diversity of the user base. The users will be categorized into new users and active users stats.")

col0, col00, col000 = st.columns([1.3,1,1])

with col00:
  st.subheader(":blue[NEW USERS STATS]")

col3, col4 = st.columns([1,1])

with col3:
  df3 = pd.read_csv('Charts/2_Weekly_New_Users_of_Uniswap.csv')
  
  fig_3 = px.bar(df3, x="TIMESPAN", y="NEW_USERS", color="MARKET_STATE", title="2. Weekly New Users of Uniswap", height=500)
  fig_3.update_layout(hovermode="x unified")
  st.plotly_chart(fig_3, use_container_width=True)

with col4:
  df4 = pd.read_csv('Charts/2a_Weekly_New_User_ of_Uniswap_by_Chains.csv')
  
  fig_4 = px.line(df4, x="TIMESPAN", y="NEW_USERS", color="BLOCKCHAIN", title="2a. Weekly New Users of Uniswap by Chains", height=500)
  fig_4.update_layout(hovermode="x unified")
  st.plotly_chart(fig_4, use_container_width=True)

st.write("As we can see, the number of users on Uniswap also reached an all-time high of 1.7 million in May 2022, but then declined steadily, reaching a low of 0.6 million in July 2023, a drop of 64.7%. The number of users slightly increased to 0.7 million in August 2023, but it is still far below the previous highs.")

col0, col00, col000 = st.columns([1.3,1,1])

with col00:
  st.subheader(":blue[ACTIVE USERS STATS]")

col4, col5 = st.columns([1,1])

with col4:
  df4 = pd.read_csv('Charts/3_Weekly_Active_Users_of_Uniswap.csv')
  
  fig_4 = px.bar(df4, x="TIMESPAN", y="ACTIVE_USERS", color="MARKET_STATE", title="3. Weekly Active Users of Uniswap", height=500)
  fig_4.update_layout(hovermode="x unified")
  st.plotly_chart(fig_4, use_container_width=True)

with col5:
  df5 = pd.read_csv('Charts/3a_Weekly_Active_Users_of_Uniswap_by_Chains.csv')
  
  fig_5 = px.line(df5, x="TIMESPAN", y="ACTIVE_USERS", color="BLOCKCHAIN", title="3a. Weekly Active Users of Uniswap by Chains", height=500)
  fig_5.update_layout(hovermode="x unified")
  st.plotly_chart(fig_5, use_container_width=True)

st.write("As we can see, the number of users on Uniswap also reached an all-time high of 1.7 million in May 2022, but then declined steadily, reaching a low of 0.6 million in July 2023, a drop of 64.7%. The number of users slightly increased to 0.7 million in August 2023, but it is still far below the previous highs.")

col6, col7, col8 = st.columns([1,1,1])

with col6:
  df6 = pd.read_csv('Charts/4_Active_Users_of_Uniswap_Before_&_After_Bear_Market.csv')
  
  fig_6 = px.bar(df6, x="MARKET_STAT", y="ACTIVE_USERS", color="MARKET_STAT", title="4. Active Users of Uniswap Before & After Bear Market", height=500)
  fig_6.update_layout(hovermode="x unified")
  st.plotly_chart(fig_6, use_container_width=True)

with col7:
  df7 = pd.read_csv('Charts/4a_Active_and_Inactive_Users_of_Uniswap_Before_&_After_Bear_Market.csv')
  
  fig_7 = px.bar(df7, x="MARKET_STAT", y="ACTIVE_USERS", color="MARKET_STAT", title="4a. Active and Inactive Users of Uniswap Before & After Bear Market ", height=500)
  fig_7.update_layout(hovermode="x unified")
  st.plotly_chart(fig_7, use_container_width=True)

with col8:
  df8 = pd.read_csv('Charts/4b_Active_Users_That_Have_Stopped_Using_Uniswap_After_Bear_Market.csv')
  
  fig_8 = px.bar(df8, x="TYPE", y="ACTIVE_USERS", color="TYPE", title="4b. Active Users That Have Stopped Using Uniswap After Bear Market", height=500)
  fig_8.update_layout(hovermode="x unified")
  st.plotly_chart(fig_8, use_container_width=True)

st.markdown("""The decline in the number of users can be explained by similar factors as the decline in trading volume, such as:

- The loss of interest and confidence in crypto, as many users may have exited the market or moved to other platforms or assets.
- The high gas fees on Ethereum, which may deter new or casual users from using Uniswap, especially for small or frequent trades.
- The competition and innovation in the DEX space, which may attract users to try out other platforms or features that offer better performance, lower fees, or more options.
- The regulatory pressure and uncertainty, which may discourage users from using Uniswap, especially in jurisdictions where crypto is banned or restricted.""")

st.subheader("LIQUIDITY")

st.write("The liquidity on Uniswap is the total amount of tokens locked in the Uniswap liquidity pools, which enable users to swap tokens on the platform. It reflects the depth and availability of the market. The chart below shows the monthly liquidity on Uniswap from January 2022 to August 2023.")

col9, col10 = st.columns([2,1])

with col9:
  df9 = pd.read_csv('Charts/5_Weekly_Net_Liquidity_Provided_on_Uniswap.csv')
  
  fig9 = px.bar(df9, x="TIMESPAN", y=["ADDED_USD_LIQ", "-REMOVED_USD_LIQ"], title="5. Weekly Liquidity Added and Removed on Uniswap(USD)", height=500)
  fig9.update_layout(hovermode="x unified")
  # Add Scatter plot
  fig9.add_scatter(x=df9['TIMESPAN'], y=df9['CUMUL_NET_USD_LIQ'], name="CUMUL_NET_USD_LIQ", line_color="yellow")
  st.plotly_chart(fig9, use_container_width=True)

with col10:
  df9 = pd.read_csv('Charts/5_Weekly_Net_Liquidity_Provided_on_Uniswap.csv')
  
  fig9a = px.line(df9, x="TIMESPAN", y="NET_USD_LIQ", title="5. Weekly Net Liquidity on Uniswap", height=500)
  fig9a.update_layout(hovermode="x unified")
  st.plotly_chart(fig9a, use_container_width=True)

col11, col12, col13 = st.columns([1,1,1])

with col11:
  df9 = pd.read_csv('Charts/5_Weekly_Net_Liquidity_Provided_on_Uniswap.csv')
  
  fig11 = px.bar(df9, x="TIMESPAN", y=["ADDED_TOKEN0_USD", "-REMOVED_TOKEN0_USD"], title="5. Weekly Liquidity Added and Removed From Token0 on Uniswap(USD)")
  fig11.update_layout(hovermode="x unified")
  st.plotly_chart(fig11, use_container_width=True)

with col12:
  df9 = pd.read_csv('Charts/5_Weekly_Net_Liquidity_Provided_on_Uniswap.csv')
  
  fig12 = px.bar(df9, x="TIMESPAN", y=["ADDED_TOKEN1_USD", "-REMOVED_TOKEN1_USD"], title="5i. Weekly Liquidity Added and Removed From Token1 Uniswap(USD)")
  fig12.update_layout(hovermode="x unified")
  st.plotly_chart(fig12, use_container_width=True)

with col13:
  df9 = pd.read_csv('Charts/5_Weekly_Net_Liquidity_Provided_on_Uniswap.csv')
  
  fig13 = px.line(df9, x="TIMESPAN", y=["NET_TOKEN0_USD", "NET_TOKEN1_USD"], title="5ii. Weekly Net Liquidity Added and Removed on Uniswap(USD)")
  fig13.update_layout(hovermode="x unified")
  st.plotly_chart(fig13, use_container_width=True)

st.write("As we can see, the liquidity on Uniswap reached an all-time high of $8.3 billion in May 2022, but then declined sharply, reaching a low of $1.4 billion in July 2023, a plunge of 83.1%. The liquidity slightly recovered to $1.7 billion in August 2023, but it is still far below the previous highs.")

col0, col00, col000 = st.columns([1,1.5,1])

with col00:
  st.subheader(":green[Top 100 Liquidity Providers on Uniswap]")

df14 = pd.read_csv('Charts/5a_Top_100_Liquidity_Providers_on_Uniswap.csv')

st.dataframe(df14)

col14, col15, = st.columns([1,1])

with col14:
  df14 = pd.read_csv('Charts/5b_Active_and_Inactive_LPs.csv')
  
  fig14 = px.bar(df14, x="TYPE", y="NUMBERS", color="TYPE", title="5b. Active and Inactive LPs", height=500)
  fig14.update_layout(hovermode="x unified")
  st.plotly_chart(fig14, use_container_width=True)

st.markdown("""The decline in liquidity can be attributed to several factors, such as:

- The decrease in the value of the tokens locked in the liquidity pools, as the prices of most cryptocurrencies have fallen significantly since May 2022.
- The increase in the risk and volatility of providing liquidity, as the market conditions have become more unpredictable and unstable, leading to higher impermanent loss and lower returns for liquidity providers.
- The migration of liquidity to other platforms or protocols, as some liquidity providers may have withdrawn their funds from Uniswap and moved them to other DEXs or yield farming opportunities that offer higher rewards, lower fees, or more security.
- The expiration or termination of liquidity incentives, such as the Uniswap Grants Program, which ended in June 2023, or the Uniswap V3 liquidity mining program, which ended in August 2023.""")

st.header("CONCLUSION")

st.write("In conclusion, the crypto winter has had a significant impact on the usage of Uniswap, as the trading volume, number of users, and liquidity have all declined substantially since the peak in May 2022. This decline can be explained by various factors, such as the overall market downturn, the high gas fees on Ethereum, the competition and innovation in the DEX space, and the regulatory pressure and uncertainty.")

st.write("However, despite the challenges and difficulties, Uniswap remains one of the most popular and widely used DEXs in the crypto space, with a loyal and diverse user base, a strong and innovative team, and a robust and flexible protocol. Uniswap has also been constantly improving and evolving, such as launching Uniswap V3 in May 2022, which introduced new features and benefits for users and liquidity providers, such as concentrated liquidity, multiple fee tiers, and improved capital efficiency.")

st.write("Therefore, it is possible that Uniswap will recover and regain its momentum once the market conditions improve and the demand for decentralized and permissionless trading increases. Uniswap may also benefit from the upcoming developments and trends in the crypto space, such as the Ethereum 2.0 upgrade, which aims to reduce gas fees and increase scalability, the growth of layer 2 solutions, which enable faster and cheaper transactions, and the adoption of cross-chain and multichain interoperability, which enable more access and liquidity for users and assets.")

st.header("RECOMMENDATIONS")

st.markdown("""Some possible recommendations for Uniswap to improve or adapt to the crypto bear market are:

- To increase the trading volume and user base, Uniswap could offer more incentives and rewards for users and liquidity providers, such as airdrops, governance tokens, fee discounts, or referral programs. Uniswap could also leverage its community and social media presence to promote its platform and educate potential users about the benefits and features of Uniswap.
- To reduce the gas fees and improve the user experience, Uniswap could accelerate its integration with layer 2 solutions, such as Optimism or Arbitrum, which enable faster and cheaper transactions on Ethereum. Uniswap could also explore other scaling options, such as zk-rollups, sidechains, or cross-chain bridges, which could increase the accessibility and liquidity of Uniswap.
- To cope with the competition and innovation in the DEX space, Uniswap could continue to develop and enhance its protocol, such as Uniswap V3, which introduced concentrated liquidity, multiple fee tiers, and improved capital efficiency. Uniswap could also collaborate and partner with other DeFi projects and protocols, such as lending, borrowing, or insurance platforms, to create synergies and value-added services for users.
- To address the regulatory pressure and uncertainty, Uniswap could adopt a proactive and transparent approach to compliance and governance, such as following the best practices and standards in the industry, engaging with regulators and policymakers, and empowering its users and stakeholders to participate in the decision-making process. Uniswap could also seek legal advice and support from reputable and experienced firms or organizations in the crypto space.""")

st.subheader("IMPORTANT REFERENCE MATERIALS")

st.markdown("""
1. [Uniswap Says It Now Collects Certain Data From Users. ](https://decrypt.co/115200/uniswap-now-collects-certain-data-users).
2. [Uniswap Team Admits It Is Storing User Data - InsideBitcoins. ](https://insidebitcoins.com/news/uniswap-team-admits-it-is-storing-user-data-should-you-be-worried).
3. [How to view my Uniswap Wallet activity – Uniswap Labs. ](https://support.uniswap.org/hc/en-us/articles/11306225627789-How-to-view-my-Uniswap-Wallet-activity).
4. [Uniswap Updates Privacy Policy: Will Track User Data for ... - Tokenist.](https://tokenist.com/uniswap-updates-privacy-policy-will-track-user-data-for-optimization/).
5. [Where to buy Uniswap: UNI swaps bear market for 26% gain - CoinJournal.](https://coinjournal.net/news/where-to-buy-uniswap-uni-swaps-bear-market-for-26-weekly-gains/).
6. [Uniswap's DEX volume declines: What's next? - AMBCrypto.](https://ambcrypto.com/uniswaps-dex-volume-declines-whats-next/).
7. [BNB (BNB) and Uniswap (UNI) Battling the Bear Market, While Pomerdoge ....](https://www.deccanherald.com/brandspot/sponsored/bnb-bnb-and-uniswap-uni-battling-the-bear-market-while-pomerdoge-pomd-is-projected-to-return-17x-soon-2684642).
8. [Big Eyes Coins And Uniswap Look To Give Some Advances Over The Bear Market.](https://www.analyticsinsight.net/big-eyes-coins-and-uniswap-look-to-give-some-advances-over-the-bear-market/).
""")




         

         

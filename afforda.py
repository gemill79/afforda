import streamlit as st

st.title("Fasteignakaupaútreikningar")

st.markdown("**Sláðu inn fjárhæðir í milljónum króna (m.kr.)**")

asettverd_mkr = st.number_input("1) Ásett verð eignarinnar (m.kr.)", min_value=0.0)
fasteignamat_mkr = st.number_input("2) Fasteignamat þinnar eignar (m.kr.)", min_value=0.0)
eftirstodvar_mkr = st.number_input("3) Eftirstöðvar lána (m.kr.)", min_value=0.0)
ltv_prcnt = st.slider("4) Veðhlutfall bankans (LTV %)", min_value=0, max_value=100, value=70)

if st.button("Reikna"):
    asettverd = asettverd_mkr * 1_000_000
    fasteignamat = fasteignamat_mkr * 1_000_000
    eftirstodvar = eftirstodvar_mkr * 1_000_000
    ltv_hlutfall = ltv_prcnt / 100

    eigid_fe = fasteignamat - eftirstodvar
    max_lan = asettverd * ltv_hlutfall
    lanathorf = asettverd - eigid_fe
    max_heimilt_verd = eigid_fe / (1 - ltv_hlutfall)

    st.markdown("### Niðurstöður")
    st.write(f"1) Eigið fé: **{eigid_fe / 1_000_000:,.1f} m.kr.**")
    st.write(f"2) Lán sem þarf: **{lanathorf / 1_000_000:,.1f} m.kr.**")
    st.write(f"3) Mesta lán m.v. LTV: **{max_lan / 1_000_000:,.1f} m.kr.**")

    if lanathorf > max_lan:
        vantar = lanathorf - max_lan
        st.error(f"4) Þig vantar: **{vantar / 1_000_000:,.1f} m.kr.**")
        st.warning(f"5) Þú hefur efni á eign að hámarki: **{max_heimilt_verd / 1_000_000:,.1f} m.kr.**")
    else:
        st.success("Til hamingju! Þú hefur nægilegt eigið fé skv. reglum bankans.")


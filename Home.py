import streamlit as st
#from streamlit_modal import Modal


# main
st.image("./images/logo.png", width=80)

st.markdown('''
<h2><span style="color: #CE411D;">BITAMIN</span> 채팅에 오신 것을 환영합니다!</h2>
''', unsafe_allow_html=True)
st.markdown("비타민에 대한 정보와 세션 자료들을 편리하게 탐색해보세요.")
st.markdown("지금 바로 시작하려면 **시작하기** 버튼을 누르세요!")

st.markdown('<a href="/second" target="_self">👉 <span style="color: #CE411D;">**시작하기**</span></a>', unsafe_allow_html=True)


# linktree
st.markdown(
    """
<style>
.link-card {
    display: flex;
    flex-direction: column;
    padding: 15px;
    margin-bottom: 10px;
    border: 1px solid #E8DDDA;
    border-radius: 25px;
    background-color: white; 
    box-shadow: 0px 0px 5px #F4EDEC;
}
.link-card:hover {
  background-color: #FFF6F3;
}
a {
    color: black!important;
    text-decoration: none!important;
}
</style>
""",
    unsafe_allow_html=True,
)


def create_link_card(title, url):
    container = st.container()
    container.markdown(
        f'<div class="link-card"><a href="{url}" target="_blank">{title}</a></div>',
        unsafe_allow_html=True,
    )
    return container



# 링크 1
create_link_card(
    "☕ 비타민 네이버 공식 카페",
    "https://cafe.naver.com/bitamin123/2512",
)

# 링크 2
create_link_card(
    "📔 비타민 네이버 공식 블로그",
    "https://blog.naver.com/bita_min",
)

# 링크 3
create_link_card(
    "🙋 비타민 12기 운영진 지원 링크",
    "https://www.python.org/",
)
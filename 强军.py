import streamlit as st
import random

# 页面标题和描述
st.set_page_config(page_title="习近平强军思想学习系统", page_icon=":guardsman:")
st.title("习近平强军思想学习系统")
st.write("本系统旨在帮助您更好地理解和掌握习近平的强军思想。")

# 总书记强军语录模块
st.header("📜 总书记强军语录")
with st.expander("建设一支听党指挥的军队"):
    st.write("“人民军队是人民的军队，必须把人民放在心中最高的位置，始终保持同人民群众的血肉联系，真正成为人民满意的军队。”")
    st.caption("来源：2018年4月16日，习近平在中央军委改革工作会议上讲话。")

with st.expander("推动军事斗争准备"):
    st.write("“在复杂多变的国际安全形势下，必须强化军事斗争准备，增强备战打仗的意识，确保能够打赢未来的战争。”")
    st.caption("来源：2016年7月30日，习近平在中国人民解放军建军89周年庆祝大会上讲话。")

with st.expander("提高军事现代化水平"):
    st.write("“我们要加快实现军事现代化，建设一支能够打胜仗、作风优良的人民军队，为维护国家安全和发展利益提供有力保障。”")
    st.caption("来源：2015年11月16日，习近平在中国人民解放军仪式上讲话。")

with st.expander("科技兴军"):
    st.write("“科技是战斗力的核心，要加快推进科技强军，依靠创新驱动，增强我军的科技实力，实现军事现代化的跨越式发展。”")
    st.caption("来源：2017年8月1日，习近平在建军90周年庆祝大会上讲话。")

with st.expander("以战促建"):
    st.write("“建设一支听从指挥、能打胜仗的军队，必须树立‘以战促建’的理念，注重实战化训练，提升部队的整体作战能力。”")
    st.caption("来源：2019年10月1日，习近平在国庆70周年阅兵式上的讲话。")

with st.expander("增强忧患意识"):
    st.write("“我们要始终保持清醒的头脑，增强忧患意识，立足新发展阶段，积极应对各种风险挑战。”")
    st.caption("来源：2020年1月3日，习近平在中央军委2019年度工作总结会议上讲话。")

with st.expander("落实强军目标"):
    st.write("“要坚持以政治建军为统领，把思想政治工作贯穿于军队建设全过程，为实现强军目标提供坚强思想保证。”")
    st.caption("来源：2016年1月6日，习近平在中央军委全体会议上讲话。")

with st.expander("深化国防和军队改革"):
    st.write("“深化国防和军队改革，调整优化部队结构，不断增强战略性、前瞻性，提升打赢能力，确保我们在未来战争中立于不败之地。”")
    st.caption("来源：2017年5月24日，习近平在全军政治工作会议上讲话。")

with st.expander("推动国际军事合作"):
    st.write("“在全球化的时代背景下，我们要积极参与国际军事合作，构建新型军事关系，促进共同安全，维护世界和平。”")
    st.caption("来源：2017年9月3日，习近平在习近平主席与军事领域外宾座谈会上的讲话。")

with st.expander("维护国家安全"):
    st.write("“国家安全是安身立命之本，必须强化安全意识，提高防范和应对能力，确保人民安居乐业。”")
    st.caption("来源：2014年11月15日，习近平在中央国家安全委员会第一次会议上讲话。")

# 设置一个分隔符
st.markdown("---")

# 添加问答测试
st.header("📚 强军思想问答")
st.write("测试一下您的理解！请根据问题选择正确的答案。")

# 定义问题和答案
questions = {
    "习近平的强军思想提出了什么样的军队建设目标？": {
        "options": ["建设一支世界一流的军队", "建设一支科技化军队", "建设一支大规模军队"],
        "answer": "建设一支世界一流的军队"
    },
    "强军思想中的四个基本方针是什么？": {
        "options": ["政治建军、改革强军、科技兴军、依法治军", "改革强军、人才强军、科技强军、依法治军", "依法治军、装备建设、政治建军、人才培养"],
        "answer": "政治建军、改革强军、科技兴军、依法治军"
    },
    # 添加更多问题...
}

# 用户答题
score = 0
for question, q_info in questions.items():
    with st.expander(question):
        user_answer = st.radio("", q_info["options"], key=question, label_visibility="collapsed")
        if user_answer == q_info["answer"]:
            score += 1

# 显示得分
if st.button("提交答案"):
    st.markdown(f"### 您的得分是：{score}/{len(questions)}")
    if score == len(questions):
        st.success("恭喜！您完全理解了强军思想的关键内容。")
    else:
        st.warning("您还有提升的空间，可以回头复习一下关键内容。")

# 添加页面底部的版权信息和作者
st.markdown("---")
st.write("© 2024 强军思想学习系统")
st.write("作者：王妍茹", unsafe_allow_html=True)
st.markdown(
    """
    <style>
    .stApp { 
        font-family: Arial, sans-serif; 
        color: #333;
        background-color: #f9f9f9;
    }
    footer { 
        font-size: 0.8rem;
        position: fixed;
        bottom: 10px;
        right: 10px;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True
)
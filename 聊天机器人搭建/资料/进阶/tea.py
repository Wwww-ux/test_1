import streamlit as st

#页面配置
st.set_page_config(
    page_title="Streamlit 聊天机器人教学版", #设置网页标题
    page_icon="🤖",  #设置网页图标
    layout = 'wide'

)

#页面标题
st.title("🤖Streamlit AI 聊天机器人演示") #设置页面标题
st.markdown('### 核心功能：各类用户输入控件+标准聊天界面')  #设置三级标题用‘###’,二级标题用‘##’
st.divider() #分割线

#侧边栏
with st.sidebar:
    st.title("机器人设置")  #侧边栏标题
    bot_name = st.text_input("机器人名称","智能助手")  #文本输入框——.text_input("输入框标题","默认名称")
    model_mode = st.selectbox(  #下拉选择框——.selectbox("输入框标题",["选项1","选项2"])  #只能选择给定值
        '选择对话模型风格',
        ["通用闲聊", "专业问答", "幽默搞笑", "温柔体贴", "严肃认真"]
    )
    reply_len  = st.radio(    #单选框——.radio("输入框标题",["选项1","选项2"])
        '回复长度',
        ["简短", "中等", "详细"]
    )
    enable_func = st.multiselect( #多选框——.multiselect("输入框标题",["选项1","选项2"])  #可选择多个值
        '开启附加功能',
        ['语音输入', '语音输出', '表情包回复', '图片生成', '代码高亮']
    )
    temperature =st.slider( #滑动条——.slider("输入框标题",最小值,最大值,默认值)
        'AI创意程度',
        min_value=0.0,
        max_value=1.0,
        value=0.5,
        step=0.1
    )
    auto_clear = st.checkbox(    #复选框——.checkbox("输入框标题",默认值)
        '发送后自动清空输入',
        value = False
    )

#主页面，用户信息输入区
st.header("用户信息输入区")  #设置标题，与markdown不同，标题会加粗
col1,col2 = st.columns(2)   #设置分页---.columns(数值)表示分为‘数值’列，返回一个列表
with col1:  #第一列
    user_nick = st.text_input("您的昵称",placeholder="请输入您的昵称")  #文本输入框——.placeholder表示输入框内的提示文字
    user_age = st.number_input("您的年龄",min_value=0,max_value=120,value=18,step=1)  #数字输入框——.number_input("输入框标题",最小值,最大值,默认值,步长)

with col2:  #第二列
    user_sex = st.selectbox("您的性别",["男","女","其他"])  
    user_mood = st.slider(
        '您的心情指数',
        min_value=0,
        max_value=10,
        value=5,
        step=1
    )
st.divider()

st.header("AI 聊天界面")  #设置标题
#如果输入框（text_input,number_input,chat_input）内容发生变化，则代码从上到下重新执行
#导致变量被清空,不能用普通变量存储

#使用seeion_state存储消息缓存，避免刷新页面导致消息丢失
if 'messages' not in st.session_state:  #如果消息缓存不存在，则创建一个空列表
    st.session_state['messages'] = []   
else:
    for data in st.session_state['messages']:  #如果消息缓存存在，则遍历消息缓存列表
        with st.chat_message(data['role']):  #用户消息显示区——.chat_message("user")表示用户消息
            st.markdown(data['content'])  #显示用户输入内容
user_input = st.chat_input("请输入您的问题或想法")  #聊天输入框——.chat_input("输入框提示词")
if user_input:
    #使用streamlit中提供的消息缓存机制seeion_state
    st.session_state['messages'].append({"role": "user", "content": user_input})  #将用户输入内容存入消息缓存列表

    with st.chat_message("user"):  #用户消息显示区——.chat_message("user")表示用户消息
        st.markdown(user_input)  #显示用户输入内容
        ai_reply = f"""
            你好 {user_nick if user_nick else '用户'}
            你当前的心情指数为：{user_mood}
            你发送的内容：{user_input}
            ---
            机器人配置：
            - 机器人名称：{bot_name}
            - 对话模型风格：{model_mode}
            - 回复长度：{reply_len}
            - 开启附加功能：{', '.join(enable_func) if enable_func else '无'}
            - AI创意程度：{temperature}
            ---
            """
    st.session_state['messages'].append({"role": "assistant", "content": ai_reply})  #将AI回复内容存入消息缓存列表
    with st.chat_message("assistant"):
        st.markdown(ai_reply)  #AI消息显示区——.chat_message("assistant")表示AI消息
    

#模拟AI回复

    
#如果自动清空聊天记录 ，则调用st.rerun()重新运行代码，刷新页面
if auto_clear:
    st.rerun()  #重新运行代码，刷新页面


if st.button("清空聊天记录"):  #按钮——.button("按钮标题")
    st.session_state['messages'] = []  #清空消息缓存列表
    st.rerun()  #重新运行代码，刷新页面
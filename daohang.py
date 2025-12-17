import streamlit as st
import pandas as pd
from datetime import datetime

# 页面基础配置（必须放在所有streamlit命令之前）
st.set_page_config(
    page_title="多功能数字平台",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 全局自定义CSS（统一深色主题风格）
st.markdown("""
    <style>
    /* 全局深色背景与文字色 */
    .main, .stApp {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    /* 进度条颜色 */
    .stProgress > div > div > div > div {
        background-color: #2196F3;
    }
    /* 状态文字色 */
    .success { color: #4CAF50; }
    .warning { color: #FFC107; }
    .danger { color: #F44336; }
    /* 代码块样式 */
    .code-block {
        background-color: #FFFFFF;
        color: #000000;
        padding: 15px;
        border-radius: 5px;
        font-family: monospace;
        border: 1px solid #EEEEEE;
        font-size: 14px;
    }
    /* 音乐播放器卡片样式 */
    .song-card {
        background-color: #2D2D2D;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        margin-bottom: 1.5rem;
    }
    /* 按钮样式优化 */
    div.stButton > button {
        background-color: #4A6FA5;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 0;
        font-size: 1rem;
        transition: all 0.2s ease;
    }
    div.stButton > button:hover {
        background-color: #38588C;
        transform: translateY(-2px);
    }
    /* 隐藏默认页脚和菜单 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# 创建四大功能标签页
tab1, tab2, tab3, tab4 = st.tabs(["📋 学生数字档案", "🖼️ 相册", "🎬 视频播放", "🎵 音乐播放"])

# ===================================== 标签页1：学生数字档案 =====================================
with tab1:
    st.title("学生 小亮 - 数字档案")
    st.markdown("---")
    
    # 1. 基础信息模块
    with st.container():
        st.subheader("📋 基础信息")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("学生ID: NO2023-001")
            st.write("性别: 男")
        with col2:
            st.write("注册时间: 2023-09-01")
            st.write("精神状态: ✅ 正常")
        with col3:
            st.write("当前等级: 安全 (基础)")
    st.markdown("---")
    
    # 2. 技能矩阵模块
    with st.container():
        st.subheader("💻 技能矩阵")
        skill_data = {
            "技能": ["C++", "Python", "Java"],
            "掌握度": ["95%", "87%", "68%"],
            "变化": ["↑5%", "↓2%", "↓10%"]
        }
        skill_df = pd.DataFrame(skill_data)
        cols = st.columns(3)
        for i, col in enumerate(cols):
            with col:
                st.write(f"**{skill_df['技能'][i]}**")
                st.progress(float(skill_df['掌握度'][i].replace('%', ''))/100)
                st.write(f"变化: {skill_df['变化'][i]}")
    st.markdown("---")
    
    # 3. 课程进度模块
    with st.container():
        st.subheader("📚 Streamlit课程进度")
        st.progress(0.20)
    st.markdown("---")
    
    # 4. 任务日志模块
    with st.container():
        st.subheader("📝 任务日志")
        task_data = {
            "日期": ["2025-10-01", "2025-11-01", "2025-12-01"],
            "任务": ["学生成绩系统", "课程管理系统", "教师信息录入"],
            "状态": ["✅ 完成", "● 进行中", "❌ 未完成"],
            "难度": ["★★☆☆☆", "★★★☆☆", "★★★★☆"]
        }
        task_df = pd.DataFrame(task_data)
        st.dataframe(
            task_df,
            hide_index=True,
            column_config={
                "状态": st.column_config.TextColumn(width="small", help="任务当前状态"),
                "难度": st.column_config.TextColumn(width="small")
            }
        )
    st.markdown("---")
    
    # 5. 最新代码成果模块
    with st.container():
        st.subheader("💻 最新代码成果")
        code_content = '''
def main():
    # 创建画布：宽11英寸，高1英寸（适配"ACCESS GRANTED"文字展示）
    plt.figure(figsize=(11,1))
    # 隐藏坐标轴（只展示文字，不显示图表边框/刻度）
    plt.axis('off')
    # 在画布中央添加文字："ACCESS GRANTED"（授权通过）
    plt.text(0.5, 0.5, 'ACCESS GRANTED', 
             fontsize=20,  # 字体大小20号
             ha='center',  # 水平居中
             va='center')  # 垂直居中
    # 保存图片到本地，文件名为result.png
    plt.savefig('result.png')
    # 在streamlit侧边栏展示保存的图片
    st.sidebar.image('result.png')
'''
        st.markdown(f"<div class='code-block'>{code_content}</div>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 6. 系统消息模块
    with st.container():
        st.subheader("📢 系统消息")
        st.write("✅ 下一个任务目标已解锁。")
        st.write("📌 任务: 课程管理系统")
        st.write(f"🕒 时间: {datetime(2023, 12, 12, 12, 43, 48)}")
        st.write("系统状态: 在线 | 授权等级: 已认证")

# ===================================== 标签页2：相册 =====================================
with tab2:
    st.title("我的相册")
    
    # 初始化图片索引
    if 'img_ind' not in st.session_state:
        st.session_state['img_ind'] = 0
    
    # 图片数据
    images = [
        {
            'url': "https://www.baltana.com/files/wallpapers-2/Cute-Cat-Images-07756.jpg",
            'text': '猫'
        },
        {
            'url': "https://cdn.britannica.com/82/232782-050-8062ACFA/Black-labrador-retriever-dog.jpg",
            'text': '狗'
        },
        {
            'url': "https://live.staticflickr.com/2686/4497672316_d283310530_3k.jpg",
            'text': '狮子'
        }
    ]
    
    # 显示当前图片（居中布局）
    col_center = st.columns(3)[1]  # 中间列显示图片
    with col_center:
        st.image(
            images[st.session_state['img_ind']]['url'],
            caption=images[st.session_state['img_ind']]['text'],
            use_column_width=True
        )
    
    # 切换图片函数
    def next_img():
        st.session_state['img_ind'] = (st.session_state['img_ind'] + 1) % len(images)
    
    def prev_img():
        st.session_state['img_ind'] = (st.session_state['img_ind'] - 1) % len(images)
    
    # 切换按钮（居中排列）
    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.button("◀ 上一张", on_click=prev_img, use_container_width=True)
    with col2:
        st.button("下一张 ▶", on_click=next_img, use_container_width=True)

# ===================================== 标签页3：视频播放 =====================================
with tab3:
    st.title("🎬 无敌少侠 播放页面")
    st.caption("成人向超级英雄动画 | 第一季共8集")
    st.divider()
    
    # 视频数据
    video_data = {
        1: {
            "title": "无敌少侠 第一季",
            "episode": "第1集",
            "video_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/89/57/34588655789/34588655789-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&gen=playurlv3&deadline=1765769180&uipk=5&oi=144233936&os=estgcos&og=cos&platform=html5&nbs=1&trid=892b33054ef1477b848438c08f93f32h&upsig=efdcae877b74d7889deeaa8c304cde2c&uparams=e,mid,gen,deadline,uipk,oi,os,og,platform,nbs,trid&bvc=vod&nettype=0&bw=631478&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1",
            "description": "马克·格雷森开始显现超级英雄的能力，在父亲全能侠的指导下训练，首次执行任务却遭遇外星怪物袭击，险些丧命。"
        },
        2: {
            "title": "无敌少侠 第一季",
            "episode": "第2集",
            "video_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/85/37/28841543785/28841543785-1-192.mp4?e=ig8euxZM2rNcNbR1nwdVhwdlhWR3hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&uipk=5&platform=html5&trid=b77f8fd0d500434593908856ae14a31O&mid=0&gen=playurlv3&os=zosbv&deadline=1765770171&oi=1385955528&nbs=1&og=hw&upsig=669cc4bed17ec2ca2e750c319bf8b305&uparams=e,uipk,platform,trid,mid,gen,os,deadline,oi,nbs,og&bvc=vod&nettype=1&bw=946018&agrr=1&buvid=&build=7330300&dl=0&f=O_0_0&orderid=0,3",
            "description": "马克加入全球防卫局，结识原子伊娃等英雄，同时全能侠在执行任务时的异常行为让马克产生怀疑，反派机器人开始策划阴谋。"
        },
        3: {
            "title": "无敌少侠 第一季",
            "episode": "第3集",
            "video_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/50/86/34557988650/34557988650-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&oi=144233936&platform=html5&trid=2b2fe6a979a8420b9c7ca8eae1b9d1bO&os=08hbv&og=hw&deadline=1765770231&uipk=5&mid=0&nbs=1&gen=playurlv3&upsig=c05a82938d0db45b5cc5cc4052dede7e&uparams=e,oi,platform,trid,os,og,deadline,uipk,mid,nbs,gen&bvc=vod&nettype=1&bw=490645&f=O_0_0&agrr=1&buvid=&build=7330300&dl=0&orderid=0,3",
            "description": "马克与原子伊娃执行救援任务时产生分歧，全能侠突然暴露出真实身份和目的，对地球英雄展开残酷屠杀，马克的世界观崩塌。"
        },
        4: {
            "title": "无敌少侠 第一季",
            "episode": "第4集",
            "video_url": "https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/29/69/34551496929/34551496929-1-192.mp4?e=ig8euxZM2rNcNbRVhzdVhwdlhWdzhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&deadline=1765770412&uipk=5&oi=144233936&platform=html5&gen=playurlv3&os=estgcos&trid=e89c066fc5bb463d9c5704efe364308O&nbs=1&og=hw&upsig=8ac6399df45b6e798346db89a83c2c7a&uparams=e,mid,deadline,uipk,oi,platform,gen,os,trid,nbs,og&bvc=vod&nettype=1&bw=826365&dl=0&f=O_0_0&agrr=1&buvid=&build=7330300&orderid=0,3",
            "description": "马克为阻止父亲的暴行与其展开殊死搏斗，全球防卫局残余成员集结反击，原子伊娃的秘密能力成为对抗全能侠的关键。"
        }
    }
    
    # 集数选择按钮
    st.subheader("选择集数")
    col_btns = st.columns(len(video_data))
    selected_episode = 1
    for idx, (ep_num, ep_info) in enumerate(video_data.items()):
        with col_btns[idx]:
            if st.button(ep_info["episode"], key=f"video_btn_{ep_num}"):
                selected_episode = ep_num
    
    # 播放选中视频
    current_video = video_data[selected_episode]
    st.video(current_video["video_url"], format="video/mp4")
    st.write(f"**{current_video['episode']}简介**：{current_video['description']}")
    st.divider()
    
    # 剧集总介绍
    st.subheader("剧集总介绍")
    total_intro = """
《无敌少侠》（Invincible）改编自罗伯特·柯克曼创作的同名漫画，讲述了少年马克·格雷森在17岁时觉醒超级能力，
跟随父亲——地球最强英雄全能侠学习如何成为一名超级英雄。然而随着剧情推进，马克逐渐发现父亲所属的维特拉姆星人
并非守护地球的英雄，而是意图殖民地球的侵略者，父子二人因此走向对立，马克在残酷的现实中成长，
肩负起保护地球和家人的重任。该剧以黑暗写实的风格、紧凑的剧情和深刻的人物刻画著称，是成人向超级英雄动画的经典之作。
"""
    st.write(total_intro)

# ===================================== 标签页4：音乐播放 =====================================
with tab4:
    st.title("🎵 轻听 · 简易音乐播放器")
    
    # 初始化歌曲索引
    if 'current_song_idx' not in st.session_state:
        st.session_state.current_song_idx = 0
    
    # 切换歌曲函数
    def prev_song():
        st.session_state.current_song_idx = (st.session_state.current_song_idx - 1) % len(music_list)
    
    def next_song():
        st.session_state.current_song_idx = (st.session_state.current_song_idx + 1) % len(music_list)
    
    # 音乐列表
    music_list = [
        {
            "album_img": "http://p1.music.126.net/5zAv9nKlwj80OearK5Vrjw==/109951169686963932.jpg?param=130y130",
            "singer": "罗森涛",
            "song_name": "小孩",
            "audio_url": "https://music.163.com/song/media/outer/url?id=2166584564.mp3"
        },
        {
            "album_img": "http://p2.music.126.net/lCblKUB1hLND5FxiVI1_Lw==/109951164919449758.jpg?param=130y130",
            "singer": "7opy",
            "song_name": "晚风",
            "audio_url": "https://music.163.com/song/media/outer/url?id=1441758494.mp3"
        },
        {
            "album_img": "http://p1.music.126.net/W1kczDCB4-r-uNAznD1ljg==/108851651165850.jpg?param=130y130",
            "singer": "万能青年旅店",
            "song_name": "杀死那个石家庄人",
            "audio_url": "https://music.163.com/song/media/outer/url?id=386844.mp3"
        }
    ]
    
    # 获取当前歌曲
    current_song = music_list[st.session_state.current_song_idx]
    
    # 歌曲信息卡片
    with st.container():
        st.markdown('<div class="song-card">', unsafe_allow_html=True)
        col_img, col_info = st.columns([1, 4], gap="medium")
        with col_img:
            st.image(current_song["album_img"], width=130, output_format="PNG")
        with col_info:
            st.markdown(f"### 🎶 {current_song['song_name']}")
            st.markdown(f"<p style='font-size:1.1rem; color:#CCCCCC;'>歌手：{current_song['singer']}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 音频播放控件
    st.audio(current_song["audio_url"], format="audio/mp3")
    
    # 切换按钮
    col_prev, col_next = st.columns([1, 1], gap="large")
    with col_prev:
        st.button("◀ 上一首", on_click=prev_song, use_container_width=True)
    with col_next:
        st.button("下一首 ▶", on_click=next_song, use_container_width=True)

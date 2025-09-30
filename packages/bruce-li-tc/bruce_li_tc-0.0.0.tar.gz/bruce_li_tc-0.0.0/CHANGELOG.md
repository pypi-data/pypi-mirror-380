# 变更日志

## [v0.8.0] - 版本发布
### 新增功能
- 描述新功能...

### 修复问题  
- 修复的问题...

# 变更日志
## [0.7.4] - wechatauto包
### 变更
- 修改crawl函数里面见名知意
## [0.7.3] - wechatauto包
### 修复
- 修改,有的时候点击头像第一次个人资料弹不出来,重复点击2次
### 变更
- 添加了新功能,加入回复间隔时间，以及和当前时间间隔数，比如7天，可更改当前时间
```python
from bruce_li_tc.wechatauto.wechat_video_automator.bruce_uiauto.bruce_uiautomation import WeChatVideoCrawler,handle_single_comment
# 1. 创建爬虫管理器实例
crawler = WeChatVideoCrawler()
# 2. 初始化（启动w、定位窗口等）
crawler.initialize(back_click_model=True)
# 3. 执行爬取！一句话搞定！
crawler.set_comment_callback(handle_single_comment)
video_list_data = crawler.crawl("关键字",
                                comment_key=["评论中的关键字","评论中的关键字2","评论中的关键字3"],
                                skip_comment=True,
                                comment_list=["回复话1","回复话2","回复话3"],
                                comment_day="7",
                                comment_datetime="2025-9-26 15:05:00",
                                Interval_count=5,
                                Interval_seconds=1)
print("video_list_data",video_list_data)
```

## [0.7.2] - wechatauto包
### 修复
- 加入回复条数触发等待时间

## [0.7.1] - wechatauto包
### 修复
- 修复了导包的问题，0.7.0不可用

## [0.7.0] - wechatauto包
### 变更
- 添加了新功能，与0.6.7旧版本可能不太兼容
- 1.根据关键字,自动化搜索对应视频，按顺序点开，然后查看带评论关键字comment_key，并进行回复随机话comment_list和关注，继续下一个用户， 
回调函数handle_single_comment也只会返回符合带评论关键字comment_key的评论，不会返回所有评论
- 2.更新了后台点击功能，0.6.7还是前台点击功能
```python
from bruce_li_tc.wechatauto.wechat_video_automator.bruce_uiauto.bruce_uiautomation import WeChatVideoCrawler,handle_single_comment
# 1. 创建爬虫管理器实例
crawler = WeChatVideoCrawler()
# 2. 初始化（启动w、定位窗口等）
crawler.initialize(back_click_model=True)
# 3. 执行爬取！一句话搞定！
crawler.set_comment_callback(handle_single_comment)
video_list_data = crawler.crawl("关键字",comment_key=["评论中的关键字","评论中的关键字2","评论中的关键字3"],skip_comment=True,comment_list=["回复话1","回复话2","回复话3"])
print("video_list_data",video_list_data)
```
## [0.6.7] - wechatauto包

### 新增
- 1.根据关键字,自动化搜索对应视频，按顺序点开，并获取所有评论，有回调函数handle_single_comment可自行处理后续的评论
```python
from bruce_li_tc.wechatauto.wechat_video_automator.bruce_uiauto.bruce_uiautomation import WeChatVideoCrawler,handle_single_comment
# 1. 创建爬虫管理器实例
crawler = WeChatVideoCrawler()
# 2. 初始化（启动w、定位窗口等）
crawler.initialize(scroll_video_comment_time=0.5)
# 3. 执行爬取！一句话搞定！
crawler.set_comment_callback(handle_single_comment)
video_list_data = crawler.crawl("关键字",skip_comment=True)
print("video_list_data",video_list_data)
#获取视频列表数据
```
- 2.根据关键字,自动化搜索对应视频，按顺序点开，不获取评论，只获取视频的详情
```python
from bruce_li_tc.wechatauto.wechat_video_automator.bruce_uiauto.bruce_uiautomation import WeChatVideoCrawler,handle_single_comment
# 1. 创建爬虫管理器实例
crawler = WeChatVideoCrawler()
# 2. 初始化（启动w、定位窗口等）
crawler.initialize(scroll_video_comment_time=0.5)
# 3. 执行爬取！一句话搞定！
video_list_data = crawler.crawl("关键字")
print("video_list_data",video_list_data)
#获取视频列表数据
```
### 变更
- 优化了某项功能的性能。

### 修复
- 修复了某个具体问题。
...
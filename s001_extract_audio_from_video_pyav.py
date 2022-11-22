# -*- coding: utf-8 -*-
"""
@author: zhubin
@email:zhubinnju@outlook.com
@license: Apache Licence
@software:PyCharm
@file: s001_extract_audio_from_video_pyav.py
@time: 2022/11/22 11:36
"""
import av

video_path = "F:\\Video\\part1_proposal\\0001.哔哩哔哩-【李佳琦】20200603带货直播回放.mp4_chunk_0.mp4_window_size_59_proposal_0_59.mp4"
input_container = av.open(video_path)

# 获取音频流
input_stream = input_container.streams.get(audio=0)[0]

output_container = av.open('demo.mp3', 'w')
output_stream = output_container.add_stream('mp3')
for frame in input_container.decode(input_stream):
    frame.pts = None
    for packet in output_stream.encode(frame):
        output_container.mux(packet)

for packet in output_stream.encode(None):
    output_container.mux(packet)

output_container.close()

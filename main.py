from function import *
print("### here we start ###")
# using textblob lib

text_P = """Recently, I purchased a new smartphone, and I have to say I am thoroughly impressed with its performance. 
        The camera quality is outstanding, capturing vibrant and detailed photos even in low-light conditions. 
        The user interface is intuitive and user-friendly, making it easy to navigate through various apps and settings. 
        Additionally, the battery life exceeded my expectations, lasting throughout the day with heavy usage. 
        The sleek design and high-resolution display further enhance the overall user experience. 
        I highly recommend this smartphone to anyone in search of a reliable and feature-packed device."""

text_N = """ I recently purchased a new laptop, and I have to say I am quite disappointed with its performance. 
        The battery life is abysmal, barely lasting a couple of hours even with minimal usage. The software is buggy, 
        and I've encountered frequent crashes, making it a frustrating experience. The build quality feels cheap, 
        and the keyboard is not comfortable to type on. I regret my decision and would not recommend this laptop to 
        anyone in need of a reliable and efficient device."""

print(blob_fun(text_N))
# print(vader_fun(text_N))
import os
import requests
from bs4 import BeautifulSoup
n1=0
def printf():
    print("1.This is What?")
    print("2.what use Search,and Search")
    print("3.Exit")
def printuse():
    print("1.bing")
    print("2.百度")
    print("3.360")
def Search1():
    search_query = input("Search:")
    url = "https://cn.bing.com/search"
    params = {"q": search_query}
    result = requests.get(url, params=params)
    # 解析搜索结果页面
    soup = BeautifulSoup(result.content, 'html.parser')
    search_results = soup.find_all('li', class_='b_algo')

# 遍历前10个搜索结果并输出标题和链接
    for i, result in enumerate(search_results[:10]):
        title = result.find('h2').get_text()
        link = result.find('a')['href']
        print(f"{i+1}. {title}\n   {link}")
def Search2():
    search_term = input("Search:")
    url = "https://www.baidu.com/s"
    params = {"wd": search_term}
    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("div", class_="result")
    num_results = len(results)
    print(f"\n共找到 {num_results} 条结果：\n")

    for i, result in enumerate(results):
        if i == 10:
            break    
        title_tag = result.find("h3")
        if not title_tag:
            continue
        title = title_tag.get_text()
    
        link_tag = result.find("a")
        if not link_tag:
            continue
        link = link_tag["href"]    
    print(f"{i+1}. {title}\n  {link}\n")
def search3():
    search_term = input("请输入搜索内容：")

    url = "https://www.so.com/s"
    params = {"q": search_term}

    response = requests.get(url, params=params)
    soup = BeautifulSoup(response.text, "html.parser")

    results = soup.find_all("li", class_="res-list")
    num_results = len(results)

    print(f"\n共找到 {num_results} 条结果：\n")

    for i, result in enumerate(results):
        if i == 10:
            break
    
        title_tag = result.find("h3")
        if not title_tag:
            continue
        title = title_tag.get_text()
    
        link_tag = result.find("a")
        if not link_tag:
            continue
        link = link_tag["href"]
    
        print(f"{i+1}. {title}\n  {link}\n")
def main():
    printf()
    n1=input("use:")
    if n1==1:
        print("I not this is what?")
    if n1==2:
        printuse()
        n2=input("use:")
        if n2==1:
            Search1()
        if n2==2:
            Search2()
        if n2==3:
            search3()
        if n2>3:
            print("没有功能",n2)
    if n1==3:
        exit()
while True:
    try:
        main()
    except:
        print("Bug")
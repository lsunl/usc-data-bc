# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
import pandas as pd
from selenium import webdriver



executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser("chrome", **executable_path, headless = False)


def scrape_all():

#grab news title and first paragraph
    news_url = "https://mars.nasa.gov/news/"
    response = requests.get(news_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    first_article = soup.find('div', class_='image_and_description_container')
    news_title = soup.find('div', class_='content_title').find('a').text
    news_p = soup.find('div', class_='rollover_description_inner').text


#grab the featured image url
    featured_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(featured_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    featured_image_url = soup.find('a', class_='button fancybox')['data-fancybox-href']
    featured_image_url='https://www.jpl.nasa.gov'+ featured_image_url


#grab the weather data from the twitter account
    twitter_url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(twitter_url)

    soup = BeautifulSoup(browser.html, 'html.parser')
    mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text


#grab the facts table and convert it to a html table via pandas
    facts_url = "https://space-facts.com/mars/"
    facts_table = pd.read_html(facts_url)
    facts_df = facts_table[0]
    facts_df.columns = ["Facts", "Data"]
    facts_df.set_index(["Facts"])
    html_table = facts_df.to_html()
    # return html_table




#grab the photo title and photo url for each of the Hemispheres
#store all the data in dictionaries
    hemisphere_image_urls = []


    driver = webdriver.Chrome()
    hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    driver.get(hemi_url)

    xpaths = ['//*[@id="product-section"]/div[2]/div[1]/div/a', '//*[@id="product-section"]/div[2]/div[2]/div/a', '//*[@id="product-section"]/div[2]/div[3]/div/a', '//*[@id="product-section"]/div[2]/div[4]/div/a']
    for x in xpaths:
        driver.find_element_by_xpath(x).click()
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        atro = soup.find("div", class_="downloads")
        atr = atro.find("a")
        img_url = atr.get('href')
        title = soup.find("h2","title").text
        dict_ = {"title": title, "img_url": img_url}
        hemisphere_image_urls.append(dict_)
    #     driver.execute_script("window.history.go(-1)")
        driver.back()


    mars_data = {
        "news_title": news_title,
        "news_para": news_p,
        "featured_image": featured_image_url,
        "weather": mars_weather,
        "hemisphere": hemisphere_image_urls
    }

    return mars_data




if __name__ == '__main__':
    scrape_all()

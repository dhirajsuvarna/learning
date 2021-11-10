import scrapy

class TripAdvisorSpider(scrapy.Spider):
    name = "TripAdvisorSpider"

    start_urls = ["https://www.tripadvisor.in/Restaurant_Review-g297628-d1389538-Reviews-Time_Traveller-Bengaluru_Bangalore_District_Karnataka.html"]

    def parse(self, response):
        reviews = response.css('div.review-container')
        for review in reviews:
            yield {
                'name' : review.css('div.member_info').css('div.info_text.pointer_cursor').css('div::text').get(),
                'date' : 'dummy date', 
                'rating' : 'dummy rating',
                'review' : 'dummy review',
                
            }

        next_page = response.css('div.unified.ui_pagination').css('a.nav.next.ui_button.primary').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
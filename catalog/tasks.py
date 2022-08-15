from celery import shared_task
from django.core.mail import send_mail as django_send_mail
from bs4 import BeautifulSoup
import requests
from .models import Author, Quote


@shared_task
def send_mail(text, email):
    django_send_mail("Reminder", text, 'admin@example.com', [email])


@shared_task
def add_quotes():
    count = 0
    while True:
        url = 'https://quotes.toscrape.com/'
        r = requests.get(url)
        s = BeautifulSoup(r.content, 'html.parser')
        quotes = s.find_all("div", {"class": "quote"})
        for i in quotes:
            if i.span.text not in Quote.objects.filter(message=i.span.text).exists():
                author = i.small.text
                description_url = requests.get(url+i.a.get('href'))
                soup_description = BeautifulSoup(description_url.content, 'html.parser')
                description = soup_description.find("div", {"class": "author-description"})
                author1 = Author.objects.get_or_create(name=author, defaults={'description': description.text})
                Quote.objects.create(message=i.span.text, author=author1[0])
                count += 1
                if count == 5:
                    break
        if count < 5:
            next_url = s.find("li", {"class": "next"}).a.get("href")
            url = url + next_url
            if next_url is None:
                django_send_mail("Quotes have ended!", "The are not new quotes in this site!", "admin@test.com",
                                 ['admin@example.com'])
                break

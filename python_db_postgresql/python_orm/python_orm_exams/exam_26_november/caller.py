import os
import django
from django.db.models import QuerySet, Count, Max, Min, Avg

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import Article, Author, Review


def get_authors(search_name=None, search_email=None) -> str:
    if search_email is None and search_name is None:
        return ""

    authors = Author.objects.all()

    if search_name:
        authors = authors.filter(full_name__icontains=search_name)

    if search_email:
        authors = authors.filter(email__icontains=search_email)

    authors = authors.order_by('-full_name')

    result = [
        f"Author: {author.full_name}, email: {author.email}, status: {'Banned' if author.is_banned else 'Not Banned'}"
        for author in authors]

    return '\n'.join(result)


def get_top_publisher():
    top_author = Author.objects.annotate(articles=Count('article')
                                         ).order_by('-articles', 'email'
                                                    ).filter(articles__gt=0).first()

    if top_author is None:
        return ""

    return f"Top Author: {top_author.full_name} " \
           f"with {top_author.articles} published articles." if top_author else ""


def get_top_reviewer():
    top_reviewer = Author.objects.annotate(total_reviews=Count('review')
                                           ).order_by('-total_reviews', 'email'
                                                      ).filter(total_reviews__gt=0
                                                               ).first()

    return f"Top Reviewer: {top_reviewer.full_name} " \
           f"with {top_reviewer.total_reviews} published reviews." if top_reviewer else ""


def get_latest_article():
    articles = Article.objects.prefetch_related('authors__review_set__article')

    if not articles:
        return ""

    latest_article = articles.annotate(avg_rating=Avg('review__rating', default=0), reviews_count=Count('review__id')
                                       ).order_by('-published_on'
                                                  ).first()

    article_authors = ", ".join([author.full_name for author in latest_article.authors.all().order_by('full_name')])

    return f"The latest article is: {latest_article.title}. Authors: {article_authors}." \
           f" Reviewed: {latest_article.reviews_count} times. Average Rating: {latest_article.avg_rating:.2f}."


def get_top_rated_article():
    top_article = Article.objects.annotate(num_reviews=Count('review__id'),
                                           avg_rating=Avg('review__rating', default=0)
                                           ).order_by('-avg_rating', 'title').first()

    if top_article is None or top_article.num_reviews == 0:
        return ""

    return f"The top-rated article is: {top_article.title}, with an average rating of {top_article.avg_rating:.2f}, " \
           f"reviewed {top_article.num_reviews} times."


def ban_author(email=None):
    author = Author.objects.prefetch_related('review_set').filter(email=email).first()

    if not author:
        return 'No authors banned.'

    author.is_banned = True
    num_reviews = author.review_set.all().delete()
    author.save()

    return f"Author: {author.full_name} is banned! {num_reviews[0]} reviews deleted."

















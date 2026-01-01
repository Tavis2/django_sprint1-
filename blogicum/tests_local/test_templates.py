import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_template(client):
    response = client.get(reverse('blog:index'))
    assert 'blog/index.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_detail_template(client):
    response = client.get(reverse('blog:post_detail', args=[0]))
    assert 'blog/detail.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_category_template(client):
    response = client.get(reverse('blog:category_posts', args=['travel']))
    assert 'blog/category.html' in [t.name for t in response.templates]

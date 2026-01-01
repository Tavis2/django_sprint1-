import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_url(client):
    url = reverse('blog:index')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_detail_url(client):
    url = reverse('blog:post_detail', args=[0])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_category_url(client):
    url = reverse('blog:category_posts', args=['travel'])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_about_page(client):
    url = reverse('pages:about')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_rules_page(client):
    url = reverse('pages:rules')
    response = client.get(url)
    assert response.status_code == 200

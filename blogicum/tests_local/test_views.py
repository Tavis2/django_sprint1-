import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_index_context(client):
    response = client.get(reverse('blog:index'))
    assert 'posts' in response.context
    assert len(response.context['posts']) > 0


@pytest.mark.django_db
def test_post_detail_context(client):
    response = client.get(reverse('blog:post_detail', args=[0]))
    assert 'post' in response.context
    assert response.context['post']['id'] == 0


@pytest.mark.django_db
def test_category_context(client):
    slug = 'personal'
    response = client.get(reverse('blog:category_posts', args=[slug]))
    assert 'category' in response.context
    assert response.context['category'] == slug

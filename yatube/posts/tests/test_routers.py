from django.test import TestCase
from django.urls import reverse

from ..models import Post, User


SLUG = 'test-slug'
USERNAME = 'Joshua'


class PostsRoutersTests(TestCase):
    def test_routers_pages(self):
        self.user = User.objects.create_user(username=USERNAME)
        self.post = Post.objects.create(
            author=self.user,
            text='text'
        )
        cases = [
            ['index', [], '/'],
            ['group_list', [SLUG], f'/group/{SLUG}/'],
            ['profile', [USERNAME], f'/profile/{USERNAME}/'],
            ['post_detail', [self.post.pk], f'/posts/{ self.post.pk }/'],
            ['post_edit', [self.post.pk], f'/posts/{ self.post.pk }/edit/'],
            ['post_create', [], '/create/'],
            ['follow_index', [], '/follow/'],
            ['profile_follow', [USERNAME], f'/profile/{USERNAME}/follow/'],
            ['profile_unfollow', [USERNAME], f'/profile/{USERNAME}/unfollow/']
        ]
        for url1, args, url2 in cases:
            with self.subTest(url=url1, args=args):
                self.assertEqual(reverse('posts:' + url1, args=args), url2)

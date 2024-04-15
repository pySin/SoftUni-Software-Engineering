from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia("John", "Instagram", 45, "story")

    # Test initialize data
    def test_initial_data(self):
        self.assertEqual(self.social_media._username, "John")
        self.assertEqual(self.social_media._platform, "Instagram")
        self.assertEqual(self.social_media._followers, 45)
        self.assertEqual(self.social_media._content_type, "story")
        self.assertEqual(self.social_media._posts, [])

    # Test _platform property
    def test_if_platform_returns(self):
        platform = self.social_media.platform
        self.assertEqual(platform, "Instagram")

    def test_if_platform_assigns_properly(self):
        self.social_media.platform = "Twitter"
        self.assertEqual(self.social_media.platform, "Twitter")

    def test_if_platform_rises_if_not_allowed_social_media(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "Facebook"
        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))

    # Test followers property
    def test_if_followers_returns(self):
        followers = self.social_media.followers
        self.assertEqual(followers, 45)

    def test_if_followers_can_be_assigned(self):
        self.social_media.followers = 56
        self.assertEqual(self.social_media.followers, 56)

    def test_if_followers_rises_if_less_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -2
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    # Test create_post() function
    def test_if_create_post_adds_it_to_posts(self):
        self.social_media.create_post("It happened yesterday.")
        expected = {'content': "It happened yesterday.", 'likes': 0, 'comments': []}
        self.assertEqual(self.social_media._posts[0], expected)

    def test_create_post_success_message(self):
        result = self.social_media.create_post("It happened yesterday.")
        expected = f"New {self.social_media._content_type} post created by {self.social_media._username} " \
                   f"on {self.social_media._platform}."
        self.assertEqual(expected, result)

    # Test like_post() function
    def test_if_post_likes_registers_a_like(self):
        self.social_media.create_post("It happened yesterday.")
        self.social_media.like_post(0)
        self.assertEqual(self.social_media._posts[0]['likes'], 1)

    def test_post_like_success_message(self):
        self.social_media.create_post("It happened yesterday.")
        result = self.social_media.like_post(0)
        self.assertEqual(f"Post liked by {self.social_media._username}.", result)

    def test_post_like_rises_when_more_than_ten_likes(self):
        self.social_media.create_post("It happened yesterday.")
        self.social_media._posts[0]['likes'] = 10
        result = self.social_media.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")

    def test_post_like_invalid_post_index(self):
        self.social_media.create_post("It happened yesterday.")
        result = self.social_media.like_post(5)
        self.assertEqual("Invalid post index.", result)

    # Test comment_on_post() function
    def test_if_comment_on_post_adda_post(self):
        self.social_media.create_post("It happened yesterday.")
        self.social_media.comment_on_post(0, "Very nice post right there!")
        comment_added = self.social_media._posts[0]["comments"][0]["comment"]
        self.assertEqual("Very nice post right there!", comment_added)

    def test_comment_on_post_success_message(self):
        self.social_media.create_post("It happened yesterday.")
        result = self.social_media.comment_on_post(0, "Very nice post right there!")
        self.assertEqual(f"Comment added by {self.social_media._username} on the post.", result)

    def test_comment_on_post_for_short_comment(self):
        self.social_media.create_post("It happened yesterday.")
        result = self.social_media.comment_on_post(0, "Hi Bob!")
        self.assertEqual("Comment should be more than 10 characters.", result)












if __name__ == "__main__":
    main()

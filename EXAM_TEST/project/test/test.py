from unittest import TestCase, main

from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    def setUp(self):
        self.user = SocialMedia("anonimous", "Instagram", 100, "post")
        self._posts = []

    def test_correct_init(self):
        self.assertEqual("anonimous", self.user._username)
        self.assertEqual("Instagram", self.user._platform)
        self.assertEqual(100, self.user._followers)
        self.assertEqual("post", self.user._content_type)
        self.assertEqual([], self.user._posts)
        self.assertEqual(self.user._validate_and_set_platform("Instagram"), None)

    def test_validating_platform_with_invalid_platform_raises_value_error(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            self.user.platform = "Facebook"

        self.assertEqual(f"Platform should be one of {allowed_platforms}", str(ve.exception))

    def test_negative_followers_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.user.followers = -201
        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_creating_post_returns_message(self):
        new_post = {'content': "Python coding", 'likes': 0, 'comments': []}
        expected_result = "New post post created by anonimous on Instagram."
        self.assertEqual(expected_result, self.user.create_post("Python coding"))
        self.assertEqual(self.user._posts, [new_post])

    def test_liking_invalid_post_index_returns_message(self):
        new_post = {'content': "Python coding", 'likes': 0, 'comments': []}
        self.user._posts = [new_post]
        expected_result = "Invalid post index."
        result = self.user.like_post(1)
        self.assertEqual(result, expected_result)

    def test_liking_valid_post_index_with_max_likes_returns_message(self):
        new_post = {'content': "Python coding", 'likes': 10, 'comments': []}
        self.user._posts = [new_post]
        result = "Post has reached the maximum number of likes."

        self.assertEqual(result, self.user.like_post(0))

    def test_liking_valid_post_index_with_under_the_limit_likes_returns_message(self):
        new_post = {'content': "Python coding", 'likes': 8, 'comments': []}
        self.user._posts = [new_post]
        result = f"Post liked by {self.user._username}."

        self.assertEqual(result, self.user.like_post(0))
        self.assertEqual(9, new_post["likes"])

    def test_commenting_with_less_than_10_characters_returns_error_message(self):
        new_post = {'content': "Python coding", 'likes': 8, 'comments': []}
        self.user._posts = [new_post]
        result = "Comment should be more than 10 characters."

        self.assertEqual(result, self.user.comment_on_post(0, "good"))

    def test_commenting_with_more_than_10_characters_returns_success(self):
        new_post = {'content': "Python coding", 'likes': 8, 'comments': []}
        self.user._posts = [new_post]
        result = f"Comment added by {self.user._username} on the post."

        self.assertEqual(result, self.user.comment_on_post(0, "good post my friend"))

if __name__ == '__main__':
    main()
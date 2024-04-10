from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.social_media = SocialMedia("angel", "YouTube",  150, "snimki")

    def test_init(self):
        self.assertEqual("angel", self.social_media._username)
        self.assertEqual("YouTube", self.social_media._platform)
        self.assertEqual(150, self.social_media._followers)
        self.assertEqual("snimki", self.social_media._content_type)
        self.assertEqual([], self.social_media._posts)

    def test_followers_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_validate_set_platforms_expect_error(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "facebook"
        self.assertEqual(f"Platform should be one of {allowed_platforms}", str(ve.exception))

    def test_validate_platform_happy_case(self):
        self.social_media._validate_and_set_platform("YouTube")
        self.assertEqual(self.social_media._platform, "YouTube")

    def test_create_post(self):
        self.social_media.create_post("bla bla")
        self.assertEqual(f"New {self.social_media._content_type}"
                         f" post created by {self.social_media._username}"
                         f" on {self.social_media._platform}.",
                         self.social_media.create_post("bla bla"))

        self.assertEqual([{'comments': [], 'content': 'bla bla', 'likes': 0}, {'comments': [], 'content': 'bla bla', 'likes': 0}], self.social_media._posts)

    def test_like_post_invald_case_negative_index(self):
        self.assertEqual(self.social_media.like_post(-2), "Invalid post index.")

    def test_like_pos_invalid_case_positive_index(self):
        self.assertEqual(self.social_media.like_post(20), "Invalid post index.")

    def test_like_post_happy_case(self):
        self.social_media.create_post("teisi")
        self.assertEqual(f"Post liked by angel.", self.social_media.like_post(0))
        self.assertEqual(1, self.social_media._posts[0]["likes"])

    def test_like_post_if_max_number_of_likes_is_valid_case(self):
        self.social_media._posts.append({'content': "teisi", 'likes': 10, 'comments': []})
        self.assertEqual(f"Post has reached the maximum number of likes.", self.social_media.like_post(0))

    def test_comment_expect_invalid_case_need_more_characters(self):
        self.social_media.create_post("kolichka")
        self.assertEqual("Comment should be more than 10 characters.", self.social_media.comment_on_post(0, "lada"))

    def test_comment_happy_case(self):
        self.social_media.create_post("kolichka")
        self.assertEqual(f"Comment added by angel on the post.", self.social_media.comment_on_post(0, "kolata ti e bokluk"))

if __name__ == "__main__":
    main()
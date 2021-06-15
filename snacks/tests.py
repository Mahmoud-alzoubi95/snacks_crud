from django.test import TestCase
# Create your tests here.

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="Mahmoud",
             email="Mahmoud@email.com", 
             password="123"
        )

        self.snack = Snack.objects.create(
            title="first order", purchaser=self.user, discribtion="Burger meal 300g" 
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "first order")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "first order")
        self.assertEqual(f"{self.snack.purchaser}", "Mahmoud")
        self.assertEqual(self.snack.discribtion,"Burger meal 300g")


    def test_snack_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "first order")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snacks_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "purchaser: Mahmoud")
        self.assertTemplateUsed(response, "snacks_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("Create"),
            {
                "title": "Burger",
                "purchaser": self.user.id,
                "discribtion": "good snack",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snacks_detail", args="2"))
        self.assertContains(response, "Burger")



    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("update", args="1"),
            {"title": "Updated title","purchaser":self.user.id,"discribtion":"New discribtion"}
        )

        self.assertRedirects(response, reverse("snacks_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("delete", args="1"))
        self.assertEqual(response.status_code, 200)